---
title: Database and Servlet: Database MetaData : Java examples (example source code) » Servlets » Database
nav: Database and Servlet: Data...
description: Database and Servlet: Database MetaData : Java examples (example source code) » Servlets » Database
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20060513092706/http://www.java2s.com/Code/Java/Servlets/DatabaseandServletDatabaseMetaData.htm
---
Database and Servlet: Database MetaData

```java title=Example.java
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;
public class DbMetaServlet extends HttpServlet {
  DataSource pool;
  public void init() throws ServletException {
    Context env = null;
    try {
      env = (Context) new InitialContext().lookup("java:comp/env");
      pool = (DataSource) env.lookup("jdbc/oracle-8i-athletes");
      if (pool == null)
        throw new ServletException(
            "'oracle-8i-athletes' is an unknown DataSource");
    } catch (NamingException ne) {
      throw new ServletException(ne);
    }
  }
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    String sql = "select * from aTable";
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;
    ResultSetMetaData rsm = null;
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out
        .println("<html><head><title>Discover a ResultSet</title></head><body>");
    out.println("<h2>Here is Info about the returned ResultSet</h2>");
    out.println("<table border='1'><tr>");
    try {
      //Get a connection from the pool
      conn = pool.getConnection();
      //Create a Statement with which to run some SQL
      stmt = conn.createStatement();
      //Execute the SQL
      rs = stmt.executeQuery(sql);
      //Get a ResultSetMetaData object from the ResultSet
      rsm = rs.getMetaData();
      int colCount = rsm.getColumnCount();
      //print column names
      printMeta(rsm, "name", out, colCount);
      //print column index
      printMeta(rsm, "index", out, colCount);
      //print column type
      printMeta(rsm, "column type", out, colCount);
      //print column display size
      printMeta(rsm, "column display", out, colCount);
    } catch (Exception e) {
      throw new ServletException(e.getMessage());
    } finally {
      try {
        stmt.close();
        conn.close();
      } catch (SQLException sqle) {
      }
    }
    out.println("</table></body></html>");
    out.close();
  } //doGet
  private void printMeta(ResultSetMetaData metaData, String type,
      java.io.PrintWriter out, int colCount) throws SQLException {
    if (metaData == null || type == null || out == null)
      throw new IllegalArgumentException(
          "Illegal args passed to printMeta()");
    out.println("<tr>");
    if (type.equals("table")) {
      out.println("<td><strong>Table name</strong></td>");
      for (int i = 1; i <= colCount; ++i) {
        out.println("<td>" + metaData.getTableName(i) + "</td>");
      }
    } else if (type.equals("name")) {
      out.println("<td><strong>Column name</strong></td>");
      for (int i = 1; i <= colCount; ++i) {
        out.println("<td>" + metaData.getColumnName(i) + "</td>");
      }
    } else if (type.equals("index")) {
      out.println("<td><strong>Column index</strong></td>");
      for (int i = 1; i <= colCount; ++i) {
        out.println("<td>" + i + "</td>");
      }
    } else if (type.equals("column type")) {
      out.println("<td><strong>Column type</strong></td>");
      for (int i = 1; i <= colCount; ++i) {
        out.println("<td>" + metaData.getColumnTypeName(i) + "</td>");
      }
    } else if (type.equals("column display")) {
      out.println("<td><strong>Column display size</strong></td>");
      for (int i = 1; i <= colCount; ++i) {
        out
            .println("<td>" + metaData.getColumnDisplaySize(i)
                + "</td>");
      }
    }
    out.println("</tr>");
  }//printMeta
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
7. Database and Servlet: Store procedure
8. Database transaction
9. Typical database commands
10. Process a raw SQL query; use ResultSetMetaData to format it
11. See Account
12. Guest Book Servlet
13. Dedicated Connection Servlet
14. Login Servlets
15. OCCI Connection Servlet
