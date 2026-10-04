---
title: Check JDBC Installation for Oracle
nav: Check JDBC Installation fo...
description: String url = "jdbc:oracle:thin:@localhost:1521:databaseName";
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20061027010728/http://www.java2s.com/Code/Java/Database-SQL-JDBC/CheckJDBCInstallationforOracle.htm
---
Check JDBC Installation for Oracle

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class CheckJDBCInstallation_Oracle {
  public static Connection getConnection() throws Exception {
    String driver = "oracle.jdbc.driver.OracleDriver";
    String url = "jdbc:oracle:thin:@localhost:1521:databaseName";
    String username = "name";
    String password = "pass";
    Class.forName(driver); // load Oracle driver
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
  /**
   * Test Validity of JDBC Installation
   *
   * @param conn
   *          a JDBC connection object
   * @return true if a given connection object is a valid one; otherwise return
   *         false.
   * @throws Exception
   *           Failed to determine if a given connection is valid.
   */
  public static boolean isValidConnection(Connection conn) throws Exception {
    if (conn == null) {
      // null connection object is not valid
      return false;
    }
    if (conn.isClosed()) {
      // closed connection object is not valid
      return false;
    }
    // for Oracle database:
    // you may use the connection object
    // with query of "select 1 from dual";
    // if the query returns the result, then
    // it is a valid connection object.
    return testConnection(conn, "select 1 from dual");
  }
  /**
   * Test Validity of a Connection
   *
   * @param conn
   *          a JDBC connection object
   * @param query
   *          a sql query to test against database connection
   * @return true if a given connection object is a valid one; otherwise return
   *         false.
   */
  public static boolean testConnection(Connection conn, String query) {
    ResultSet rs = null;
    Statement stmt = null;
    try {
      stmt = conn.createStatement();
      if (stmt == null) {
        return false;
      }
      rs = stmt.executeQuery(query);
      if (rs == null) {
        return false;
      }
      if (rs.next()) {
        // connection object is valid: we were able to
        // connect to the database and return something useful.
        return true;
      }
      // there is no hope any more for the validity
      // of the connection object
      return false;
    } catch (Exception e) {
      return false;
    } finally {
      // close database resources
      try {
        rs.close();
        stmt.close();
      } catch (Exception e) {
        // ignore
      }
    }
  }
  public static void main(String[] args) {
    Connection conn = null;
    try {
      conn = getConnection();
      System.out.println("conn=" + conn);
      System.out.println("valid connection = " + isValidConnection(conn));
    } catch (Exception e) {
      // handle the exception
      e.printStackTrace();
      System.exit(1);
    } finally {
      // release database resources
      try {
        conn.close();
      } catch (Exception e) {
        // ignore
      }
    }
  }
}
```

Related examples in the same category
---
6. Test Oracle JDBC Driver Installation
7. Create Employee Table Oracle
8. Count row in Oracle
9. Get Column Names From ResultSet for Oracle
10. Demo ResultSet Oracle
11. All data types for Oracle
12. Get Column Privileges Oracle
13. Test OCINet 8 App
14. Test SSL
15. Test Data Encryption Integrity
16. Test DataSource LookUp
17. OracleDataSource Demo
18. Register custome type to Oracle
19. Insert custom type to Oracle
