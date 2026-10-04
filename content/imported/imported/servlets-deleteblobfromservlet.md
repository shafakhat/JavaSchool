---
title: Delete Blob From Servlet
nav: Delete Blob From Servlet
description: public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException,
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20070115143200/http://www.java2s.com:80/Code/Java/Servlets/DeleteBlobFromServlet.htm
---
Delete Blob From Servlet

```java title=Example.java
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class DeleteBlobFromServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException,
      ServletException {
    Connection conn = null;
    PreparedStatement pstmt = null;
    String id = "0001";
    ServletOutputStream out = response.getOutputStream();
    response.setContentType("text/html");
    out.println("<html><head><title>Delete Photo</title></head>");
    try {
      conn = getHSQLConnection();
      pstmt = conn.prepareStatement("delete from MyPictures where id = ?");
      pstmt.setString(1, id);
      pstmt.executeUpdate();
      out.println("<body><h3>deleted photo with id=" + id + "</h3></body></html>");
    } catch (Exception e) {
      out.println("<body><h1>Error=" + e.getMessage() + "</h1></body></html>");
    } finally {
      try {
        pstmt.close();
        conn.close();
      } catch (SQLException e) {
        e.printStackTrace();
      }
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
    String url = "jdbc:oracle:thin:@localhost:1521:databaseName";
    String username = "username";
    String password = "password";
    Class.forName(driver); // load Oracle driver
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
}
```

Related examples in the same category
---
3. Cached Connection Servlet
4. Transaction Connection Servlet
5. Session Login JDBC
6. JDBC and Servlet
7. Database and Servlet: Database MetaData
8. Database and Servlet: Store procedure
9. Database transaction
10. Typical database commands
11. Process a raw SQL query; use ResultSetMetaData to format it
12. See Account
13. Guest Book Servlet
14. Dedicated Connection Servlet
15. Login Servlets
16. OCCI Connection Servlet
17. Get Column Names From ResultSet
18. Display Clob Servlet
19. Delete Clob From Servlet
20. Display Blob Servlet
21. Delete Clob From Oracle in a Servlet
22. Insert Clob to MySql Servlet
23. Update Clob data stored in MySql from a Servlet
