---
title: Hibernate and JPA
nav: Hibernate & JPA
description: Object-relational mapping in Java - JPA entities, Hibernate sessions, relationships, JPQL, caching and the N+1 problem.
section: Advanced Java
order: 110
---

## JPA is the spec, Hibernate the implementation

**JPA** (Jakarta Persistence) = annotations + `EntityManager` + JPQL standard. **Hibernate** = the reference implementation and more (hql refinements, second-level cache, criteria polish, batch tools). You code to JPA; you tune with Hibernate.

```text title=stack
your code ── @Entity / EntityManager / Repository
             │ JPA API (jakarta.persistence)
             │ Hibernate (or EclipseLink, OpenJPA...)
             └── JDBC ── PostgreSQL / MySQL / Oracle ...
```

## Your first entity

```java title=Book.java
import jakarta.persistence.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "books", indexes = @Index(columnList = "isbn", unique = true))
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 200)
    private String title;

    @Enumerated(EnumType.STRING)          // store name, not ordinal!
    private Format format = Format.PAPER;

    @Column(length = 13)
    private String isbn;

    @ManyToOne(fetch = FetchType.LAZY)    // many books -> one author
    @JoinColumn(name = "author_id")
    private Author author;

    public enum Format { PAPER, EBOOK, AUDIO }

    protected Book() {}                   // JPA needs a no-arg constructor

    public Book(String title) { this.title = title; }

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
}
```

Golden rules: **IDs always**, `protected` no-arg constructor, enums as `STRING`, `LAZY` by default for associations, defensive `equals/hashCode` on identity if you put entities in sets.

## Working with the Session (EntityManager)

```java title=Repos.java
import jakarta.persistence.*;
import java.util.List;

public class Demo {
    public static void main(String[] args) {
        EntityManagerFactory emf =
            Persistence.createEntityManagerFactory("bookstore");
        EntityManager em = emf.createEntityManager();

        em.getTransaction().begin();
        Book b = new Book("Effective Java");
        b.setIsbn("9780134685991");
        em.persist(b);                          // INSERT
        em.getTransaction().commit();

        Book found = em.find(Book.class, 1L);   // SELECT by id (1st-level cache)
        em.getTransaction().begin();
        found.setTitle("Effective Java (3rd)"); // dirty checking -> UPDATE
        em.getTransaction().commit();

        em.close();                             // detaches everything
        emf.close();
    }
}
```

- **First-level cache** = the session: same PK → same instance while it lives.
- **Dirty checking**: you modify the object, Hibernate schedules the UPDATE at flush - no explicit `update()` call.
- `detach/clear/evict` for long-lived sessions; `merge` reattaches copies.

## Relationships

| Mapping | Annotation | Notes |
|---|---|---|
| many→one | `@ManyToOne` | own FK column; default EAGER in spec (prefer LAZY) |
| one→many | `@OneToMany(mappedBy=...)` | inverse side, owns the FK elsewhere |
| one→one | `@OneToOne` | `optional=false` + `@MapsId` for shared keys |
| many→many | `@ManyToMany` | usually better as explicit join entity |

```java title=Author.java
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Author {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    @OneToMany(mappedBy = "author", cascade = CascadeType.PERSIST,
               orphanRemoval = true)
    private List<Book> books = new ArrayList<>();
    // getters...
}
```

`cascade` flows operations down (save author → save books); it is **not** the same as `fetch` (when data loads). Confusing them is the #1 ORM bug.

## JPQL vs native SQL

```java title=Queries.java
import jakarta.persistence.*;
import java.util.List;

public class Queries {
    void run(EntityManager em) {
        // JPQL - entity/attribute names, dialect independent
        List<Book> jpa = em.createQuery(
                "SELECT b FROM Book b WHERE b.format = :fmt ORDER BY b.title",
                Book.class)
            .setParameter("fmt", Book.Format.EBOOK)
            .getResultList();

        // Criteria API - type-safe dynamic queries
        var cb = em.getCriteriaBuilder();
        var q = cb.createQuery(Book.class);
        var root = q.from(Book.class);
        q.select(root).where(cb.like(root.get("title"), "%Java%"));

        // Native SQL when you need vendor features
        List<Object[]> raw = em.createNativeQuery(
                "SELECT title, COUNT(*) FROM books GROUP BY title")
            .getResultList();
    }
}
```

## The N+1 problem

```text title=the classic trap
SELECT * FROM author;              -- 1 query
SELECT * FROM book WHERE author=1  -- N queries...
SELECT * FROM book WHERE author=2     ...one per author
```

Fixes (pick one):

```java title=Fixes.java
// 1. join fetch (JPQL)
"SELECT a FROM Author a JOIN FETCH a.books"

// 2. entity graph on the repository method
@EntityGraph(attributePaths = "books")
List<Author> findAllWithBooks();

// 3. batch size (Hibernate)
@BatchSize(size = 20)  // on Book or hibernate.default_batch_fetch_size
```

Always verify with SQL logging in tests: one statement per entity batch is the goal.

## Caching & tuning

- **L1** (session): always on, per-session identity.
- **L2** (shared, optional): `@Cacheable` regions - Ehcache/Caffeine; invalidate carefully.
- **Query cache**: only with L2; caches result *ids* - easy to stale.
- Dialect, `connection.pool_size`, `hibernate.jdbc.batch_size` for inserts, `show_sql=false` in prod.

Related: [Spring Data access](spring.html) · [JDBC fundamentals](jdbc.html) · [JPA examples imported from the archive](hibernate-criteriaonetomanyassociationscriteria.html)
