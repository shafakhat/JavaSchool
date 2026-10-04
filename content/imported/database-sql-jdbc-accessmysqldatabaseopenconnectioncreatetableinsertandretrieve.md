---
title: Access MySQL Database
nav: Access MySQL Database
description: Access MySQL Database: open connection, create table, insert and retrieve
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20061026214616/http://www.java2s.com/Code/Java/Database-SQL-JDBC/AccessMySQLDatabaseopenconnectioncreatetableinsertandretrieve.htm
---
Access MySQL Database: open connection, create table, insert and retrieve

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class SimpleProgramToAccessOracleDatabase {
  public static Connection getConnection() throws Exception {
    // load the Oracle JDBC Driver
    Class.forName("oracle.jdbc.driver.OracleDriver");
    // define database connection parameters
    return DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:database", "userName",
        "password");
  }
  public static void main(String[] args) throws SQLException {
    Connection conn = null; // connection object
    Statement stmt = null; // statement object
    ResultSet rs = null; // result set object
    try {
      conn = getConnection(); // without Connection, can not do much
      // create a statement: This object will be used for executing
      // a static SQL statement and returning the results it produces.
      stmt = conn.createStatement();
      // start a transaction
      conn.setAutoCommit(false);
      // create a table called cats_tricks
      stmt.executeUpdate("CREATE TABLE cats_tricks " + "(name VARCHAR2(30), trick VARCHAR2(30))");
      // insert two new records to the cats_tricks table
      stmt.executeUpdate("INSERT INTO cats_tricks VALUES('mono', 'r')");
      stmt.executeUpdate("INSERT INTO cats_tricks VALUES('mono', 'j')");
      // commit the transaction
      conn.commit();
      // set auto commit to true (from now on every single
      // statement will be treated as a single transaction
      conn.setAutoCommit(true);
      // get all of the the records from the cats_tricks table
      rs = stmt.executeQuery("SELECT name, trick FROM cats_tricks");
      // iterate the result set and get one row at a time
      while (rs.next()) {
        String name = rs.getString(1); // 1st column in query
        String trick = rs.getString(2); // 2nd column in query
        System.out.println("name=" + name);
        System.out.println("trick=" + trick);
        System.out.println("==========");
      }
    } catch (ClassNotFoundException ce) {
      // if the driver class not found, then we will be here
      System.out.println(ce.getMessage());
    } catch (SQLException e) {
      // something went wrong, we are handling the exception here
      if (conn != null) {
        conn.rollback();
        conn.setAutoCommit(true);
      }
      System.out.println("--- SQLException caught ---");
      // iterate and get all of the errors as much as possible.
      while (e != null) {
        System.out.println("Message   : " + e.getMessage());
        System.out.println("SQLState  : " + e.getSQLState());
        System.out.println("ErrorCode : " + e.getErrorCode());
        System.out.println("---");
        e = e.getNextException();
      }
    } finally { // close db resources
      try {
        rs.close();
        stmt.close();
        conn.close();
      } catch (Exception e) {
      }
    }
  }
}
```

Related examples in the same category
---
2. Create Database for MySQL
3. Test MySQL JDBC Driver Installation
4. Create table for mysql database
5. Setup mysql datasource
6. Count rows in MySQL
7. Demo ResultSet for MySQL
8. Create Table With All Data Types In MySQL
9. Insert text file into MySQL
10. Read a Clob object from MySQL
11. How to serialize/de-serialize a Java object to the MySQL database.
12. Check JDBC Installation for MySQL
13. Demo MySql Transaction
14. Create database for MySql
