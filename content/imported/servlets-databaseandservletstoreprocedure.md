---
title: Database and Servlet: Store procedure : Java examples (example source code) » Servlets » Database
nav: Database and Servlet: Stor...
description: Database and Servlet: Store procedure : Java examples (example source code) » Servlets » Database
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20060513092636/http://www.java2s.com/Code/Java/Servlets/DatabaseandServletStoreprocedure.htm
---
Database and Servlet: Store procedure

```java title=Example.java
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;
public class StoredProcServlet extends HttpServlet {
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
    String eventName = request.getParameter("name");
    String location = request.getParameter("location");
    String date = request.getParameter("date");
    List paramList = new ArrayList();
    paramList.add(eventName);
    paramList.add(location);
    paramList.add(date);
    try {
      addRaceEvent(paramList);
    } catch (SQLException sqle) {
      throw new ServletException(sqle.getMessage());
    }
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out.println("<html><head><title>Add an Event</title></head><body>");
    out.println("<h2>The Event named " + eventName
        + " has been added to the database</h2>");
    out.println("</body>");
    out.println("</html>");
    out.close();
  } //doGet
  public Connection getConnection() {
    Connection conn = null;
    try {
      conn = pool.getConnection();
    } catch (SQLException sqle) {
      throw new ServletException(sqle.getMessage());
    } finally {
      return conn;
    }
  }
  public void addRaceEvent(List values) throws SQLException {
    if (values == null)
      throw new SQLException("Invalid parameter in addRaceEvent method.");
    Connection conn = null;
    conn = getConnection();
    if (conn == null)
      throw new SQLException("Invalid Connection in addRaceEvent method");
    java.util.Iterator it = values.iterator();
    CallableStatement cs = null;
    //Create an instance of the CallableStatement
    cs = conn.prepareCall("{call addEvent (?,?,?)}");
    for (int i = 1; i <= values.size(); i++)
      cs.setString(i, (String) it.next());
    //Call the inherited PreparedStatement.executeUpdate() method
    cs.executeUpdate();
    // return the connection to the pool
    conn.close();
  }//addRaceEvent
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
8. Database transaction
9. Typical database commands
10. Process a raw SQL query; use ResultSetMetaData to format it
11. See Account
12. Guest Book Servlet
13. Dedicated Connection Servlet
14. Login Servlets
15. OCCI Connection Servlet
