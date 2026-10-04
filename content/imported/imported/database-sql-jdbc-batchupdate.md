---
title: Batch Update : Java examples (example source code) » Database SQL JDBC » SQL Update
nav: Batch Update : Java exampl...
description: Batch Update : Java examples (example source code) » Database SQL JDBC » SQL Update
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20060513071636/http://www.java2s.com/Code/Java/Database-SQL-JDBC/BatchUpdate.htm
---
Batch Update : Java examples (example source code) » Database SQL JDBC » SQL Update

Batch Update

```java title=Example.java
/* From http://java.sun.com/docs/books/tutorial/index.html */
import java.sql.BatchUpdateException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class BatchUpdate {
  public static void main(String args[]) {
    String url = "jdbc:mySubprotocol:myDataSource";
    Connection con;
    Statement stmt;
    try {
      Class.forName("myDriver.ClassName");
    } catch (java.lang.ClassNotFoundException e) {
      System.err.print("ClassNotFoundException: ");
      System.err.println(e.getMessage());
    }
    try {
      con = DriverManager.getConnection(url, "myLogin", "myPassword");
      stmt = con.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE,
          ResultSet.CONCUR_UPDATABLE);
      con.setAutoCommit(false);
      stmt.addBatch("INSERT INTO COFFEES "
          + "VALUES('Amaretto', 49, 9.99, 0, 0)");
      stmt.addBatch("INSERT INTO COFFEES "
          + "VALUES('Hazelnut', 49, 9.99, 0, 0)");
      stmt.addBatch("INSERT INTO COFFEES "
          + "VALUES('Amaretto_decaf', 49, 10.99, 0, 0)");
      stmt.addBatch("INSERT INTO COFFEES "
          + "VALUES('Hazelnut_decaf', 49, 10.99, 0, 0)");
      int[] updateCounts = stmt.executeBatch();
      ResultSet uprs = stmt.executeQuery("SELECT * FROM COFFEES");
      System.out.println("Table COFFEES after insertion:");
      while (uprs.next()) {
        String name = uprs.getString("COF_NAME");
        int id = uprs.getInt("SUP_ID");
        float price = uprs.getFloat("PRICE");
        int sales = uprs.getInt("SALES");
        int total = uprs.getInt("TOTAL");
        System.out.print(name + " " + id + " " + price);
        System.out.println(" " + sales + " " + total);
      }
      uprs.close();
      stmt.close();
      con.close();
    } catch (BatchUpdateException b) {
      System.err.println("SQLException: " + b.getMessage());
      System.err.println("SQLState: " + b.getSQLState());
      System.err.println("Message: " + b.getMessage());
      System.err.println("Vendor: " + b.getErrorCode());
      System.err.print("Update counts: ");
      int[] updateCounts = b.getUpdateCounts();
      for (int i = 0; i < updateCounts.length; i++) {
        System.err.print(updateCounts[i] + " ");
      }
    } catch (SQLException ex) {
      System.err.println("SQLException: " + ex.getMessage());
      System.err.println("SQLState: " + ex.getSQLState());
      System.err.println("Message: " + ex.getMessage());
      System.err.println("Vendor: " + ex.getErrorCode());
    }
  }
}
```

Related examples in the same category
---
1. Create Coffees table
2. JDBC update
3. JDBC Update logic
4. SQL Batch
5. Get Metadata from prepareStatement
6. Batch Update: transation
7. Return generated keys
