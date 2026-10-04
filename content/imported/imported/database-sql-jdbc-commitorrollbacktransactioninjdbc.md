---
title: Commit or rollback transaction in JDBC
nav: Commit or rollback transac...
description: st.execute("INSERT INTO orders (username, order_date) VALUES ('java', '2007-12-13')",
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20090418001818/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/CommitorrollbacktransactioninJDBC.htm
---
```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class Main {
  public static void main(String[] args) throws Exception {
    String url = "jdbc:mysql://localhost/testdb";
    String username = "root";
    String password = "";
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = null;
    try {
      conn = DriverManager.getConnection(url, username, password);
      conn.setAutoCommit(false);
      Statement st = conn.createStatement();
      st.execute("INSERT INTO orders (username, order_date) VALUES ('java', '2007-12-13')",
          Statement.RETURN_GENERATED_KEYS);
      ResultSet keys = st.getGeneratedKeys();
      int id = 1;
      while (keys.next()) {
        id = keys.getInt(1);
      }
      PreparedStatement pst = conn.prepareStatement("INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)");
      pst.setInt(1, id);
      pst.setString(2, "1");
      pst.setInt(3, 10);
      pst.setDouble(4, 100);
      pst.execute();
      conn.commit();
      System.out.println("Transaction commit...");
    } catch (SQLException e) {
      if (conn != null) {
        conn.rollback();
        System.out.println("Connection rollback...");
      }
      e.printStackTrace();
    } finally {
      if (conn != null && !conn.isClosed()) {
        conn.close();
      }
    }
  }
}
```

1.  Creating connection to the MySQL database
---  ---
2.  Creating a Database in MySQL
3.  Creating a MySQL Database Table to store Java Types
4.  JDBC Mysql Connection String
5.  Inserting values in MySQL database table
6.  Use Oracle DataSource To Store MySql Connection
7.  Create Database for MySQL
8.  Test MySQL JDBC Driver Installation
9.  Create table for mysql database
10.  Setup mysql datasource
11.  Access MySQL Database: open connection, create table, insert and retrieve
12.  Count rows in MySQL
13.  Demo ResultSet for MySQL
14.  Create Table With All Data Types In MySQL
15.  Insert text file into MySQL
16.  Read a Clob object from MySQL
17.  How to serialize/de-serialize a Java object to the MySQL database.
18.  Check JDBC Installation for MySQL
19.  Demo MySql Transaction
20.  Retrieve auto-generated keys
21.  Move to absolute or relative row
22.  Issue 'create database' command ny using Statement
23.  Loading a Flat File to a MySQL Table, file is comma-separated
24.  Loading a Flat File to a MySQL Table, file is terminated by \r\n, use this statement
25.  Copy data from one table to another in a database
26.  Exporting a MySQL Table to a Flat File
