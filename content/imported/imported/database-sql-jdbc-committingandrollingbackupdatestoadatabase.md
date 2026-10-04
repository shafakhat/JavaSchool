---
title: Committing and Rolling Back Updates to a Database
nav: Committing and Rolling Bac...
description: Connection connection = DriverManager.getConnection(url, username, password);
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20100213225255/http://java2s.com/Code/Java/Database-SQL-JDBC/CommittingandRollingBackUpdatestoaDatabase.htm
---
```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
public class Main {
  public static void main(String[] argv) throws Exception {
    String driverName = "com.jnetdirect.jsql.JSQLDriver";
    Class.forName(driverName);
    String serverName = "127.0.0.1";
    String portNumber = "1433";
    String mydatabase = serverName + ":" + portNumber;
    String url = "jdbc:JSQLConnect://" + mydatabase;
    String username = "username";
    String password = "password";
    Connection connection = DriverManager.getConnection(url, username, password);
    // Disable auto commit
    connection.setAutoCommit(false);
    // Do SQL updates...
    // Commit updates
    connection.commit();
  }
}
```

1.  Connect to more than one database
---  ---
2.  Verify database setup
3.  Debug Database connection
4.  Create Connection With Properties
5.  Set save point
6.  JDBC Simple Connection
7.  Load some drivers
8.  Encapsulate the Connection-related operations that every JDBC program seems to use
9.  Test of loading a driver and connecting to a database
10.  Load MySQL JDBC Driver
11.  Oracle JDBC Driver load
12.  Oracle JDBC Driver load test: NewInstance
13.  Test Register Oracle JDBC Driver
14.  Install Oracle Driver and Execute Resultset
15.  Test Thin Net8 App
16.  Specify a CharSet when connecting to a DBMS
17.  Listing All Available Parameters for Creating a JDBC Connection
18.  String java.sql.DriverPropertyInfo.name (Get name of property)
19.  boolean java.sql.DriverPropertyInfo.required (Is property value required?)
20.  String java.sql.DriverPropertyInfo.value (Get current value)
21.  String java.sql.DriverPropertyInfo.description (Get description of property)
22.  String[] java.sql.DriverPropertyInfo.choices (Get possible choices for property; if null, value can be any string)
23.  Determining If a Database Supports Transactions
24.  Disable auto commit mode in JDBC
25.  Print warnings on a Connection to STDERR.
26.  Print warnings on a Connection to a specified PrintWriter.
