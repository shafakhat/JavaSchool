---
title: Check if cursor is in the first row
nav: Check if cursor is in the ...
description: Check if cursor is in the first row : ResultSet Scrollable « Database SQL JDBC « Java
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20091021042607/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/Checkifcursorisinthefirstrow.htm
---
Check if cursor is in the first row : ResultSet Scrollable « Database SQL JDBC « Java

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class Main {
  public static void main(String[] args) throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection connection = DriverManager
        .getConnection("jdbc:mysql://localhost/testdb", "root", "");
    Statement statement = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,
        ResultSet.CONCUR_READ_ONLY);
    ResultSet resultSet = statement.executeQuery("SELECT * FROM products");
    if (resultSet.isBeforeFirst()) {
      System.out.println("beginning");
    }
    connection.close();
  }
}
```

1.  Determining If a Database Supports Scrollable Result Sets
---  ---
2.  Create a scrollable result sets
3.  Get Number Of Rows in a Scrollable ResultSet from MySQL
4.  Demo Scrollable ResultSet from MySQL
5.  Scrollable resultset
6.  Get the fetch size of a statement
7.  Set the fetch size on the statement
8.  Change the fetch size on the result set
9.  Move cursor to the last record
10.  Move cursor to the first row
11.  Move cursor to the last row
12.  Move cursor to the end, after the last row
13.  Move cursor backward
14.  Move the cursor back and forth with absolute index
15.  Move cursor to the beginning, before the first row
16.  Move cursor to the second last row with absolute position
17.  Move cursor down 5 rows from the current row. If this moves cursor beyond the last row, cursor is put after the last row
18.  Move cursor up 3 rows from the current row. If this moves cursor beyond the first row, cursor is put before the first row
19.  Get the current position of cursor
20.  Move cursor in scrollable result sets
21.  If cursor is in the last row
22.  Moving the Cursor in a Scrollable Result Set
23.  Getting the Cursor Position in a Scrollable Result Set
24.  Getting the Number of Rows in a Table Using a Scrollable Result Set
25.  Create an insensitive scrollable result set
26.  Create a sensitive scrollable result set
