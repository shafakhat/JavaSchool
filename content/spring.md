---
title: Spring Framework, Spring IO and Spring Boot
nav: Spring & Spring Boot
description: Spring dependency injection and AOP, the Spring IO platform, and Spring Boot auto-configuration - concepts plus working examples.
section: Advanced Java
order: 100
---

## The Spring family in one map

| Project | What it is |
|---|---|
| **Spring Framework** (core) | IoC container, AOP, data access, MVC, transactions - the original (2003) |
| **Spring IO** | An umbrella *platform/dependency descriptor* - curated compatible versions of many Spring projects (BOM-style), not a runtime you "start" |
| **Spring Boot** | Opinionated auto-configured way to *build* Spring apps (embedded server, starters, actuator) - since 2014, the default entry point |
| Spring Security / Data / Cloud / Batch... | Projects built *on* the core, versioned in the platform |

Mental model: **Core Spring** = the engine. **Spring IO** = the parts catalog that keeps versions compatible. **Spring Boot** = the car that ships assembled, key-ready.

## IoC & dependency injection (the core idea)

```java title=Services.java
import org.springframework.stereotype.Service;
import org.springframework.stereotype.Component;
import javax.sql.DataSource;

// POJOs - no framework base classes needed
@Component
public class JdbcUserRepo {
    private final DataSource ds;
    public JdbcUserRepo(DataSource ds) {   // constructor injection
        this.ds = ds;                      // Boot provides a pooled DataSource
    }
    public String nameById(int id) { /* ... */ return "ada"; }
}

@Service
public class UserService {
    private final JdbcUserRepo repo;
    public UserService(JdbcUserRepo repo) { // single constructor = autowired
        this.repo = repo;
    }
    public String greet(int id) {
        return "Hello, " + repo.nameById(id);
    }
}

@RestController
public class HelloController {
    private final UserService service;
    public HelloController(UserService service) { this.service = service; }

    @GetMapping("/hello/{id}")
    public String hello(@PathVariable int id) {
        return service.greet(id);
    }
}
```

- The **container** ( ApplicationContext) instantiates, wires and manages bean lifecycles.
- **Constructor injection** is the standard: final fields, no field-injection surprises, easy tests (`new UserService(fakeRepo)`).
- Scopes: `singleton` (default), `prototype`, plus web scopes in MVC.

## AOP & @Transactional (what proxies do)

```java title=OrderService.java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class OrderService {

    @Transactional                      // begin/commit/rollback via proxy
    public void placeOrder(Order o) {
        repo.save(o);
        inventory.decrement(o.sku());
        payments.charge(o.total());     // throw → automatic rollback
    }
}
```

Spring wraps the bean in a **proxy**: calls flow through advice (transaction, security, retry, metrics) then to your method. Pitfalls to know: self-invocation bypasses the proxy, private methods aren't intercepted, checked exceptions need `rollbackFor`.

## Spring Boot in 20 lines

```java title=DemoApplication.java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication                  // component scan + auto-config
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}

@RestController
class Api {
    @GetMapping("/ping")
    String ping() { return "pong @ " + java.time.LocalTime.now(); }
}
```

```yaml title=application.yml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:h2:mem:demo
  jpa:
    hibernate:
      ddl-auto: update
```

What Boot **auto-configures** from that one dependency set (via `@Conditional` rules on the classpath):

- embedded **Tomcat/Jetty** (no WAR deploy), **Jackson** for JSON, **Hikari** connection pool
- `DataSource`, `TransactionManager`, `JPA`/MyBatis when starters present
- **actuator** health/metrics endpoints, externalized **profiles** (`application-prod.yml`)
- **Spring IO**'s role shows up here: Boot releases are published as a BOM keeping every starter on compatible versions (`spring-boot-dependencies`).

## Testing Boot apps

```java title=ApiTest.java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class ApiTest {
    @Autowired TestRestTemplate rest;

    @Test
    void pingWorks() {
        String body = rest.getForObject("/ping", String.class);
        org.junit.jupiter.api.Assertions.assertTrue(body.startsWith("pong"));
    }
}
```

`@SpringBootTest` boots the real context (fast with H2/testcontainers); `@WebMvcTest` slices to controllers; plain JUnit + Mockito for units.

## Talking to a database (Spring Data style)

```java title=UserRepo.java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepo extends JpaRepository<User, Long> {
    // derived query - no implementation written:
    java.util.List<User> findByEmailEndingWith(String domain);
}
```

Repositories are generated at runtime; derived queries, `@Query` JPQL/SQL, specifications and projections cover the rest - with transactions managed by the container.

## Migration notes (legacy → Boot)

1. WAR + `web.xml` servlet app → add `spring-boot-starter-web`, move `web.xml` filters to `FilterRegistrationBean`.
2. XML `<beans>` context → `@Configuration` + component scan; keep XML via `@ImportResource` while strangling.
3. Struts/jQuery frontends → serve static assets + new MVC endpoints route by route (see [Struts](struts.html)).
4. Drop the app into Boot's embedded server; keep Oracle/MySQL drivers as starters.

Related: [Hibernate & JPA](hibernate-jpa.html) · [Servlets & JSP](servlets-jsp.html) · [Spring examples imported from the archive](spring-aspecthelloworldexample.html)
