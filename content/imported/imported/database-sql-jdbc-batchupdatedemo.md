---
title: Batch Update Demo
nav: Batch Update Demo
description: connection = DriverManager.getConnection(url, "username", "password");
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20060822142531/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/BatchUpdateDemo.htm
---
```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
public class MainClass {
  public static void main(String[] args) {
    Connection connection = null;
    Statement statement = null;
    try {
      Class.forName("com.mysql.jdbc.Driver").newInstance();
      String url = "jdbc:mysql://localhost/chapter04_jdbc21";
      connection = DriverManager.getConnection(url, "username", "password");
      statement = connection.createStatement();
      String update1 = "UPDATE employees SET email = 'a@a.com' WHERE email = 'a@b.com'";
      statement.addBatch(update1);
      String update2 = "UPDATE employees SET email = 'b@b.com' WHERE email = 'b@c.com'";
      statement.addBatch(update2);
      String update3 = "UPDATE employees SET email = 'c@c.com' WHERE email = 'c@d.com'";
      statement.addBatch(update3);
      statement.executeBatch();
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      if (statement != null) {
        try {
          statement.close();
        } catch (SQLException e) {
        } // nothing we can do
      }
      if (connection != null) {
        try {
          connection.close();
        } catch (SQLException e) {
        } // nothing we can do
      }
    }
  }
}
```

Related examples in the same category
---
1. Batch Update Insert
2.
3. Check Batch Update Result
4. Batch update for MySQL
5. Deal with batch update exception and results
6. Demo Prepared Statement Add Batch MySQL
