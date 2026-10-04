---
title: Dedicated Connection Servlet : Java examples (example source code) » Servlets » Database
nav: Dedicated Connection Servl...
description: Dedicated Connection Servlet : Java examples (example source code) » Servlets » Database
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20060513092716/http://www.java2s.com/Code/Java/Servlets/DedicatedConnectionServlet.htm
---
Dedicated Connection Servlet : Java examples (example source code) » Servlets » Database

Dedicated Connection Servlet

```java title=Example.java
/*
Java Programming with Oracle JDBC
by Donald Bales
ISBN: 059600088X
Publisher: O'Reilly
*/
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.UnavailableException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class DedicatedConnectionServlet extends HttpServlet {
  Connection connection;
  long connected;
  public void init(ServletConfig config) throws ServletException {
    super.init(config);
    try {
      // load the driver
      Class.forName("oracle.jdbc.driver.OracleDriver").newInstance();
    } catch (ClassNotFoundException e) {
      throw new UnavailableException(
          "DedicatedConnection.init() ClassNotFoundException: "
              + e.getMessage());
    } catch (IllegalAccessException e) {
      throw new UnavailableException(
          "DedicatedConnection.init() IllegalAccessException: "
              + e.getMessage());
    } catch (InstantiationException e) {
      throw new UnavailableException(
          "DedicatedConnection.init() InstantiationException: "
              + e.getMessage());
    }
    try {
      // establish a connection
      connection = DriverManager.getConnection(
          "jdbc:oracle:thin:@dssw2k01:1521:orcl", "scott", "tiger");
      connected = System.currentTimeMillis();
    } catch (SQLException e) {
      throw new UnavailableException(
          "DedicatedConnection.init() SQLException: "
              + e.getMessage());
    }
  }
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head>");
    out.println("<title>A Dedicated Connection</title>");
    out.println("</head>");
    out.println("<body>");
    Statement statement = null;
    ResultSet resultSet = null;
    String userName = null;
    try {
      // test the connection
      statement = connection.createStatement();
      resultSet = statement
          .executeQuery("select initcap(user) from sys.dual");
      if (resultSet.next())
        userName = resultSet.getString(1);
    } catch (SQLException e) {
      out.println("DedicatedConnection.doGet() SQLException: "
          + e.getMessage() + "<p>");
    } finally {
      if (resultSet != null)
        try {
          resultSet.close();
        } catch (SQLException ignore) {
        }
      if (statement != null)
        try {
          statement.close();
        } catch (SQLException ignore) {
        }
    }
    out.println("Hello " + userName + "!<p>");
    out.println("This Servlet's database connection was created on "
        + new java.util.Date(connected) + "<p>");
    out.println("</body>");
    out.println("</html>");
  }
  public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException {
    doGet(request, response);
  }
  public void destroy() {
    // close the connection
    if (connection != null)
      try {
        connection.close();
      } catch (SQLException ignore) {
      }
  }
}
```

Related examples in the same category
---
1. Servlets Database Query
2. Using JDBC in Servlets
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
14. Login Servlets
15. OCCI Connection Servlet
