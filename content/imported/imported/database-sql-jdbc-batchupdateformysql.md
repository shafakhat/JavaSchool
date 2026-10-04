---
title: Batch update for MySQL
nav: Batch update for MySQL
description: Connection conn = DriverManager.getConnection(url, username, password);
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20061016100004/http://www.java2s.com/Code/Java/Database-SQL-JDBC/BatchupdateforMySQL.htm
---
```java title=Example.java
import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.BatchUpdateException;
public class TestBatchUpdate {
  public static Connection getConnection() throws Exception {
    String driver = "org.gjt.mm.mysql.Driver";
    String url = "jdbc:mysql://localhost/octopus";
    String username = "root";
    String password = "root";
    Class.forName(driver);
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
  public static void main(String args[]) {
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;
    try {
      conn = getConnection();
      stmt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
      conn.setAutoCommit(false);
      stmt.addBatch("INSERT INTO batch_table(id, name) VALUES('11', 'A')");
      stmt.addBatch("INSERT INTO batch_table(id, name) VALUES('22', 'B')");
      stmt.addBatch("INSERT INTO batch_table(id, name) VALUES('33', 'C')");
      int[] updateCounts = stmt.executeBatch();
      conn.commit();
      rs = stmt.executeQuery("SELECT * FROM batch_table");
      while (rs.next()) {
        String id = rs.getString("id");
        String name = rs.getString("name");
        System.out.println("id=" + id + "  name=" + name);
      }
    } catch (BatchUpdateException b) {
      System.err.println("SQLException: " + b.getMessage());
      System.err.println("SQLState: " + b.getSQLState());
      System.err.println("Message: " + b.getMessage());
      System.err.println("Vendor error code: " + b.getErrorCode());
      System.err.print("Update counts: ");
      int[] updateCounts = b.getUpdateCounts();
      for (int i = 0; i < updateCounts.length; i++) {
        System.err.print(updateCounts[i] + " ");
      }
    } catch (SQLException ex) {
      System.err.println("SQLException: " + ex.getMessage());
      System.err.println("SQLState: " + ex.getSQLState());
      System.err.println("Message: " + ex.getMessage());
      System.err.println("Vendor error code: " + ex.getErrorCode());
    } catch (Exception e) {
      System.err.println("Exception: " + e.getMessage());
    } finally {
      try {
        rs.close();
        stmt.close();
        conn.close();
      } catch (Exception ignore) {
      }
    }
  }
}
```

Related examples in the same category
---
4. Batch Update Demo
5. Deal with batch update exception and results
6. Demo Prepared Statement Add Batch MySQL
