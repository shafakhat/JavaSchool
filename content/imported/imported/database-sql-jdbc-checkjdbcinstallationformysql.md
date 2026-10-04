---
title: Check JDBC Installation for MySQL
nav: Check JDBC Installation fo...
description: Connection conn = DriverManager.getConnection(url, username, password);
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20061026214722/http://www.java2s.com/Code/Java/Database-SQL-JDBC/CheckJDBCInstallationforMySQL.htm
---
Check JDBC Installation for MySQL

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class CheckJDBCInstallation_MySQL {
  public static Connection getConnection() throws Exception {
    String driver = "org.gjt.mm.mysql.Driver";
    String url = "jdbc:mysql://localhost/databaseName";
    String username = "root";
    String password = "root";
    Class.forName(driver); // load MySQL driver
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
    // for MySQL database:
    // you may use the connection object
    // with query of "select 1"; if the
    // query returns the result, then it
    // is a valid connection object.
    return testConnection(conn, "select 1");
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
      //
      // something went wrong: connection is bad
      //
      return false;
    } finally {
      try {
        rs.close();
        stmt.close();
        conn.close();
      } catch (Exception e) {
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
6. Access MySQL Database: open connection, create table, insert and retrieve
7. Count rows in MySQL
8. Demo ResultSet for MySQL
9. Create Table With All Data Types In MySQL
10. Insert text file into MySQL
11. Read a Clob object from MySQL
12. How to serialize/de-serialize a Java object to the MySQL database.
13. Demo MySql Transaction
14. Create database for MySql
