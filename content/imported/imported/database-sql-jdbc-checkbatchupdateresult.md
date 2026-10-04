---
title: Check Batch Update Result
nav: Check Batch Update Result
description: stmt.addBatch("INSERT INTO survey(id, name) VALUES('11', 'Alex')");
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20061016095959/http://www.java2s.com/Code/Java/Database-SQL-JDBC/CheckBatchUpdateResult.htm
---
```java title=Example.java
import java.sql.BatchUpdateException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class Main {
  public static void main(String[] args) throws Exception {
    Connection conn = getMySqlConnection();
    ResultSet rs = null;
    Statement stmt = null;
    try {
        conn = getMySqlConnection();
        stmt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE,
                                    ResultSet.CONCUR_UPDATABLE);
        conn.setAutoCommit(false);
        stmt.addBatch("INSERT INTO survey(id, name) VALUES('11', 'Alex')");
        stmt.addBatch("INSERT INTO survey(id, name) VALUES('22', 'Mary')");
        stmt.addBatch("INSERT INTO survey(id, name) VALUES('33', 'Bob')");
        int[] updateCounts = stmt.executeBatch();
        System.out.println(updateCounts);
        conn.commit();
        rs = stmt.executeQuery("SELECT * FROM survey");
        while (rs.next()) {
            String id = rs.getString("id");
            String name = rs.getString("name");
            System.out.println("id="+id +"  name="+name);
        }
    }
    catch(BatchUpdateException b) {
        System.err.println("SQLException: " + b.getMessage());
        System.err.println("SQLState: " + b.getSQLState());
        System.err.println("Message: " + b.getMessage());
        System.err.println("Vendor error code: " + b.getErrorCode());
        System.err.print("Update counts: ");
        int [] updateCounts = b.getUpdateCounts();
        for (int i = 0; i < updateCounts.length; i++) {
            System.err.print(updateCounts[i] + " ");
        }
    }
    catch(SQLException ex) {
        System.err.println("SQLException: " + ex.getMessage());
        System.err.println("SQLState: " + ex.getSQLState());
        System.err.println("Message: " + ex.getMessage());
        System.err.println("Vendor error code: " + ex.getErrorCode());
    }
    catch(Exception e) {
        e.printStackTrace();
        System.err.println("Exception: " + e.getMessage());
    }
    finally {
        rs.close();
        stmt.close();
        conn.close();
    }
  }
  private static Connection getHSQLConnection() throws Exception {
    Class.forName("org.hsqldb.jdbcDriver");
    System.out.println("Driver Loaded.");
    String url = "jdbc:hsqldb:data/tutorial";
    return DriverManager.getConnection(url, "sa", "");
  }
  public static Connection getMySqlConnection() throws Exception {
    String driver = "org.gjt.mm.mysql.Driver";
    String url = "jdbc:mysql://localhost/demo2s";
    String username = "oost";
    String password = "oost";
    Class.forName(driver);
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
  public static Connection getOracleConnection() throws Exception {
    String driver = "oracle.jdbc.driver.OracleDriver";
    String url = "jdbc:oracle:thin:@localhost:1521:caspian";
    String username = "mp";
    String password = "mp2";
    Class.forName(driver); // load Oracle driver
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
}
```

Download: CheckBatchUpdateResult.zip ( 3,849 K )
---
Related examples in the same category
3. Batch Update Demo
4. Batch update for MySQL
5. Deal with batch update exception and results
6. Demo Prepared Statement Add Batch MySQL
