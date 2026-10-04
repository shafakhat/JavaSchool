---
title: Java JDBC
nav: JDBC
description: Connect Java to a database with JDBC - driver setup, queries, prepared statements and transactions.
section: Core Java
order: 70
---

## What is JDBC?

**JDBC** (Java Database Connectivity) is the standard API for running SQL from Java. It works the same way for PostgreSQL, MySQL, SQLite or Oracle - only the driver and URL change.

```text title=The JDBC chain
 your code -> JDBC API (java.sql) -> Driver (jar) -> database server
```

## Setup

1. Add the driver JAR to your classpath (Maven example for PostgreSQL):

```xml title=pom.xml (Maven)
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.4</version>
</dependency>
```

Common connection URLs:

| Database | URL pattern |
|---|---|
| PostgreSQL | `jdbc:postgresql://localhost:5432/mydb` |
| MySQL | `jdbc:mysql://localhost:3306/mydb` |
| SQLite | `jdbc:sqlite:data.db` (file-based, no server) |

## The classic 6 steps

```java title=FirstQuery.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class FirstQuery {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "app";
        String pass = "secret";

        // 1-2. open connection (driver auto-loads via SPI)
        try (Connection conn = DriverManager.getConnection(url, user, pass);
             // 3. create a statement
             Statement st = conn.createStatement();
             // 4. execute a query
             ResultSet rs = st.executeQuery("SELECT id, name FROM users ORDER BY id")) {

            // 5. walk the result set
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                System.out.println(id + " -> " + name);
            }
        } catch (Exception e) {
            // 6. always close resources - try-with-resources does it for us
            System.out.println("failed: " + e.getMessage());
        }
    }
}
```

Every resource (`Connection`, `Statement`, `ResultSet`) implements `AutoCloseable`, so **always** use try-with-resources - leaked connections kill databases in production.

## PreparedStatement - the right way

Never build SQL by string concatenation with user input - it's the #1 SQL injection hole:

```java title=PreparedDemo.java
import java.sql.*;

public class PreparedDemo {
    public static void main(String[] args) {
        String url = "jdbc:sqlite:app.db";
        String unsafeName = "o'brien'; DROP TABLE users;--";

        try (Connection conn = DriverManager.getConnection(url)) {
            createSchema(conn);

            // WRONG - injection + breaks on quotes
            // String badSql = "INSERT INTO users(name) VALUES('" + unsafeName + "')";

            // RIGHT - placeholders, values bound separately
            String sql = "INSERT INTO users(name, age) VALUES(?, ?)";
            try (PreparedStatement ps = conn.prepareStatement(sql)) {
                ps.setString(1, unsafeName);   // 1-based parameter index
                ps.setInt(2, 34);
                int inserted = ps.executeUpdate();   // returns affected row count
                System.out.println("inserted rows: " + inserted);
            }

            // reading with placeholders too
            try (PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE age > ?")) {
                ps.setInt(1, 30);
                try (ResultSet rs = ps.executeQuery()) {
                    while (rs.next()) {
                        System.out.println("user: " + rs.getString("name") + ", age " + rs.getInt("age"));
                    }
                }
            }
        } catch (SQLException e) {
            System.out.println("error: " + e.getMessage());
        }
    }

    static void createSchema(Connection conn) throws SQLException {
        try (Statement st = conn.createStatement()) {
            st.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER
                )
                """);
        }
    }
}
```

| Method | Use for |
|---|---|
| `executeQuery(sql)` | SELECT - returns `ResultSet` |
| `executeUpdate(sql)` | INSERT/UPDATE/DELETE - returns row count |
| `execute(sql)` | anything (returns boolean: has ResultSet?) |

## Data mapping cheat sheet

| JDBC method | SQL type |
|---|---|
| `getInt` / `setInt` | INTEGER |
| `getLong` / `setLong` | BIGINT |
| `getDouble` / `setDouble` | DOUBLE / FLOAT |
| `getString` / `setString` | VARCHAR / TEXT |
| `getBoolean` / `setBoolean` | BOOLEAN |
| `getTimestamp` / `setTimestamp` | TIMESTAMP |
| `getObject(col, LocalDate.class)` | DATE (modern style) |

## Transactions

```java title=Transaction.java
import java.sql.*;

public class Transaction {
    public static void main(String[] args) {
        String url = "jdbc:sqlite:bank.db";

        try (Connection conn = DriverManager.getConnection(url)) {
            try (Statement st = conn.createStatement()) {
                st.execute("CREATE TABLE IF NOT EXISTS acct(id INTEGER PRIMARY KEY, bal INTEGER)");
                st.execute("DELETE FROM acct");
                st.execute("INSERT INTO acct VALUES(1, 1000)");
                st.execute("INSERT INTO acct VALUES(2, 1000)");
            }

            conn.setAutoCommit(false);            // 1. begin transaction
            try (PreparedStatement from = conn.prepareStatement("UPDATE acct SET bal = bal - ? WHERE id = ?");
                 PreparedStatement to = conn.prepareStatement("UPDATE acct SET bal = bal + ? WHERE id = ?")) {

                from.setInt(1, 300); from.setInt(2, 1); from.executeUpdate();
                to.setInt(1, 300);   to.setInt(2, 2);   to.executeUpdate();

                conn.commit();                    // 2. all good -> persist
                System.out.println("transfer committed");
            } catch (SQLException e) {
                conn.rollback();                  // 3. something broke -> undo everything
                System.out.println("rolled back: " + e.getMessage());
            }

            try (Statement st = conn.createStatement();
                 ResultSet rs = st.executeQuery("SELECT id, bal FROM acct")) {
                while (rs.next()) System.out.println("acct " + rs.getInt(1) + " = " + rs.getInt(2));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

Rules: turn **off** auto-commit, do the work, `commit()` on success, `rollback()` on failure - and restore auto-commit when done.

## Batch operations

Inserting thousands of rows one by one is slow - batch them:

```java title=Batch.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Batch {
    public static void main(String[] args) throws SQLException {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:app.db");
             PreparedStatement ps = conn.prepareStatement("INSERT INTO users(name, age) VALUES(?, ?)")) {

            conn.setAutoCommit(false);
            for (int i = 1; i <= 1000; i++) {
                ps.setString(1, "user-" + i);
                ps.setInt(2, 18 + (i % 40));
                ps.addBatch();                       // queue it
                if (i % 100 == 0) ps.executeBatch(); // flush every 100
            }
            ps.executeBatch();
            conn.commit();
            System.out.println("batch done");
        }
    }
}
```

## Metadata (optional)

```java title=Meta.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Meta {
    public static void main(String[] args) throws Exception {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:app.db");
             Statement st = conn.createStatement();
             ResultSet rs = st.executeQuery("SELECT * FROM users")) {

            var meta = rs.getMetaData();
            System.out.println("columns: " + meta.getColumnCount());
            for (int i = 1; i <= meta.getColumnCount(); i++) {
                System.out.println("  " + meta.getColumnName(i) + " : " + meta.getColumnTypeName(i));
            }
        }
    }
}
```

## Modern notes

- **Prefer a DataSource / connection pool** (HikariCP) over `DriverManager` in production.
- **Never** hardcode credentials - use environment variables or a secrets manager.
- Consider higher-level layers (jOOQ, JPA/Hibernate) once raw JDBC gets repetitive - but every Java dev should know raw JDBC first.

> **Remember:** PreparedStatement = security + performance (plan caching). String-concatenated SQL = SQL injection. This is not optional knowledge.

Next: [Keywords reference](keywords.html).
