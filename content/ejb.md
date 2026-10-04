---
title: Enterprise JavaBeans (EJB)
nav: EJB
description: What EJB is - session beans, transactions, pooling, and where it stands versus CDI and Spring in modern Java EE.
section: Advanced Java
order: 120
---

## What EJB is for

**Enterprise JavaBeans** is the classic Jakarta EE (ex J2EE) component model for transactional business logic: the container gives you **transactions, pooling, security, remoting and timers** declaratively, so bean code stays a POJO-ish class. EJB 3.x made beans dramatically simpler (annotations, no home/remote boilerplate of the 2.x era).

```text title=EJB 3.x flavours
@Stateless   pooled, transactional workhorse (services, DAOs)
@Stateful    per-client conversational state (wizards, carts)
@Singleton   one instance, app-wide (config, counters)
@MessageDriven  driven by JMS messages (async consumers)
```

Modern reality check: many shops replaced EJB with **CDI + JTA + JAX-RS/Spring**, but EJB still runs huge banking/government systems - and `@Stateless` beans coexist happily with Jakarta REST endpoints in the same WAR.

## A stateless session bean

```java title=OrderService.java
import jakarta.ejb.*;
import jakarta.transaction.Transactional;   // or container defaults

@Stateless                                  // pooled, TX_REQUIRED by default
public class OrderService {

    @Resource(lookup = "java:comp/env/jdbc/shop")
    private javax.sql.DataSource ds;        // container injects resources

    // A new transaction starts when the method is entered (TX_REQUIRED);
    // commit on normal return, rollback on system/runtime exception.
    public long placeOrder(String sku, int qty) {
        // ... JDBC / JPA work using ds or an EntityManager ...
        try (var c = ds.getConnection(); var st = c.createStatement()) {
            st.executeUpdate(
                "INSERT INTO orders(sku, qty) VALUES ('" + sku + "', " + qty + ")");
        } catch (Exception e) {
            throw new RuntimeException(e);   // container rolls the TX back
        }
        return System.currentTimeMillis() % 100000;
    }

    @Remove                                   // client calls done - destroy instance
    public void finish() { /* stateful beans only care */ }
}
```

The container **pools** instances across clients (stateless = no per-client fields, despite the name meaning "no conversational state"), intercepts calls to start/commit transactions, and enforces method permissions.

## Stateful vs singleton vs MDB

```java title=Variants.java
import jakarta.ejb.*;
import jakarta.jms.MessageListener;
import jakarta.jms.Message;

@Stateful
public class CheckoutWizard {            // one instance per session
    private String cartId;
    public void step1() { cartId = "c-42"; }   // state survives between calls
    @Remove public void finish() { /* container drops bean */ }
}

@Singleton
@Startup                                  // create at deploy
public class AppConfig {
    @Resource private javax.sql.DataSource ds;   // serialized startup OK
    @PostConstruct void init() { /* load config once */ }
}

@MessageDriven(activationConfig = {
    @ActivationConfigProperty(propertyName = "destinationType",
        propertyValue = "jakarta.jms.Queue")})
public class OrderQueue implements MessageListener {
    @Override
    public void onMessage(Message m) { /* async, TX per message */ }
}
```

## What the container gives you (declaratively)

| Feature | How |
|---|---|
| Transactions | `@TransactionAttribute(REQUIRED/REQUIRES_NEW/...)` on methods |
| Security | `@RolesAllowed("admin")`, `@DeclareRoles` |
| Timers | `@Timeout`, `@Schedule(second="0", minute="*/5")` |
| Remoting | `@Remote` interfaces / remote JNDI (legacy) |
| Async | `@Asynchronous` + `Future<T>` return |
| Pooling/lifecycle | `@PostConstruct`, `@PreDestroy`, pool sizes in server config |

```java title=Schedule.java
import jakarta.ejb.*;
import java.util.Date;

@Singleton
public class Reports {
    @Schedule(hour = "2", minute = "0", persistent = false)
    void nightly() {
        System.out.println("nightly report at " + new Date());
    }

    @Asynchronous
    public java.util.concurrent.Future<String> rebuild() {
        return new javax.ejb.AsyncResult<>("done");
    }
}
```

## EJB vs CDI vs Spring - choosing vocabulary

| Need | Classic EE | Leaner EE | Spring |
|---|---|---|---|
| DI + events | EJB (indirect) | **CDI** (`@Inject`, observers) | IoC container |
| Transactions | EJB TX attributes | **JTA** + CDI interceptor | `@Transactional` |
| REST API | EJB + JAX-RS | **JAX-RS/Jakarta REST** | `@RestController` |
| Messaging | MDB | JMS + CDI | `@JmsListener` |
| Simplicity | heavy container | WildFly/Payara | Spring Boot embedded |

Rule of thumb: new Jakarta EE code → **CDI beans + JTA + REST**, reaching for `@Stateless` when you want EJB's TX/pooling semantics; stay on EJB while maintaining EE apps; Spring Boot elsewhere.

## Talking to EJBs

```java title=Client.java
import javax.naming.InitialContext;

public class Client {
    public static void main(String[] args) throws Exception {
        InitialContext ctx = new InitialContext();
        // local view (same app)
        OrderService svc = (OrderService)
            ctx.lookup("java:module/OrderService");
        long id = svc.placeOrder("ISBN-1", 2);

        // remote (another JVM) would use @Remote + global JNDI name
        System.out.println("order " + id);
    }
}
```

In practice you inject instead: `@EJB private OrderService svc;` or, for plain CDI injection of remote beans, `@Remote` + EJB client jars / REST variants.

Related: [Servlets & JSP](servlets-jsp.html) · [Spring comparison](spring.html) · [J2EE/J2EE-level examples imported from the archive](j2ee-afullstrutsapplication.html)
