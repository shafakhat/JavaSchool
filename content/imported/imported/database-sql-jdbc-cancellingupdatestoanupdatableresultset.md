---
title: Cancelling Updates to an Updatable Result Set
nav: Cancelling Updates to an U...
description: Connection connection = DriverManager.getConnection(url, username, password);
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20090715214952/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/CancellingUpdatestoanUpdatableResultSet.htm
---
Cancelling Updates to an Updatable Result Set

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
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
    Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE,
        ResultSet.CONCUR_UPDATABLE);
    ResultSet resultSet = stmt.executeQuery("SELECT * FROM my_table");
    // Move cursor to the row to update
    resultSet.first();
    // Update the value of column col_string on that row
    resultSet.updateString("col_string", "new data");
    // Discard the update to the row
    resultSet.cancelRowUpdates();
  }
}
```

1.  If database support updatable result sets
---  ---
2.  Using UpdatableResultSet to insert a new row
3.  Delete Row from Updatable ResultSet for MySQL
4.  Insert Row to Updatable ResultSet from MySQL
5.  Make updates in Updatable ResultSet
6.  Demo Updatable ResultSet
7.  Updatable resultset with Oracle Driver
8.  Determining If a Database Supports Updatable Result Sets: An updatable result set allows modification to data in a table through the result set.
9.  Creating an Updatable Result Set
10.  Determining If a Result Set Is Updatable
11.  Updating a Row in a Database Table Using an Updatable Result Set
12.  Inserting a Row into a Database Table Using an Updatable Result Set
13.  Deleting a Row from a Database Table Using an Updatable Result Set
14.  Refreshing a Row in an Updatable Result Set
