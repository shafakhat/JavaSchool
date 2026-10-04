---
title: Cached Connection Servlet : Java examples (example source code) » Servlets » Database
nav: Cached Connection Servlet ...
description: Cached Connection Servlet : Java examples (example source code) » Servlets » Database
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20060513092733/http://www.java2s.com/Code/Java/Servlets/CachedConnectionServlet.htm
---
Cached Connection Servlet

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
import java.util.MissingResourceException;
import java.util.ResourceBundle;
import java.util.Vector;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class CachedConnectionServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Cached Connection Servlet</title>");
    out.println("</head>");
    out.println("<body>");
    // let's turn on verbose output
    CacheConnection.setVerbose(true);
    // now let's get a cached connection
    Connection connection = CacheConnection.checkOut();
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
    // let's return the conection
    CacheConnection.checkIn(connection);
    out.println("Hello " + userName + "!<p>");
    out.println("You're using a cached connection!<p>");
    out.println("</body>");
    out.println("</html>");
  }
  public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException {
    doGet(request, response);
  }
}
class CacheConnection {
  private static boolean verbose = false;
  private static int numberConnections = 0;
  private static Vector cachedConnections = new Vector();
  private static Thread monitor = null;
  private static long MAX_IDLE = 1000 * 60 * 60;
  synchronized public static Connection checkOut() {
    return checkOut("Database");
  }
  synchronized public static Connection checkOut(String baseName) {
    boolean found = false;
    CachedConnection cached = null;
    if (verbose) {
      System.out.println("There are "
          + Integer.toString(numberConnections)
          + " connections in the cache");
      System.out.println("Searching for a connection not in use...");
    }
    for (int i = 0; !found && i < numberConnections; i++) {
      if (verbose) {
        System.out.println("Vector entry " + Integer.toString(i));
      }
      cached = (CachedConnection) cachedConnections.get(i);
      if (!cached.isInUse() && cached.getBaseName().equals(baseName)) {
        if (verbose) {
          System.out.println("found cached entry "
              + Integer.toString(i) + " for " + baseName);
        }
        found = true;
      }
    }
    if (found) {
      cached.setInUse(true);
    } else {
      if (verbose) {
        System.out.println("Cached entry not found ");
        System.out.println("Allocating new entry for " + baseName);
      }
      cached = new CachedConnection(Database.getConnection(baseName),
          true, baseName);
      cachedConnections.add(cached);
      numberConnections++;
    }
    if (monitor == null) {
      monitor = new Thread(new Runnable() {
        public void run() {
          while (numberConnections > 0) {
            runMonitor();
          }
          monitor = null;
          if (verbose) {
            System.out.println("CacheConnection monitor stopped");
          }
        }
      });
      monitor.setDaemon(true);
      monitor.start();
    }
    return cached.getConnection();
  }
  synchronized public static void checkIn(Connection c) {
    boolean found = false;
    boolean closed = false;
    CachedConnection cached = null;
    Connection conn = null;
    int i = 0;
    if (verbose) {
      System.out.println("Searching for connection to set not in use...");
    }
    for (i = 0; !found && i < numberConnections; i++) {
      if (verbose) {
        System.out.println("Vector entry " + Integer.toString(i));
      }
      cached = (CachedConnection) cachedConnections.get(i);
      conn = cached.getConnection();
      if (conn == c) {
        if (verbose) {
          System.out.println("found cached entry "
              + Integer.toString(i));
        }
        found = true;
      }
    }
    if (found) {
      try {
        closed = conn.isClosed();
      } catch (SQLException ignore) {
        closed = true;
      }
      if (!closed)
        cached.setInUse(false);
      else {
        cachedConnections.remove(i);
        numberConnections--;
      }
    } else if (verbose) {
      System.out.println("In use Connection not found!!!");
    }
  }
  synchronized private static void checkUse() {
    CachedConnection cached = null;
    Connection conn = null;
    int i = 0;
    long now = System.currentTimeMillis();
    long then = 0;
    for (i = numberConnections - 1; i > -1; i--) {
      if (verbose) {
        System.out
            .println("CacheConnection monitor checking vector entry "
                + Integer.toString(i) + " for use...");
      }
      cached = (CachedConnection) cachedConnections.get(i);
      if (!cached.isInUse()) {
        then = cached.getLastUsed();
        if ((now - then) > MAX_IDLE) {
          if (verbose) {
            System.out.println("Cached entry "
                + Integer.toString(i)
                + " idle too long, being destroyed");
          }
          conn = cached.getConnection();
          try {
            conn.close();
          } catch (SQLException e) {
            System.err.println("Unable to close connection: "
                + e.getMessage());
          }
          cachedConnections.remove(i);
          numberConnections--;
        }
      }
    }
  }
  private static void runMonitor() {
    checkUse();
    if (numberConnections > 0) {
      if (verbose) {
        System.out.println("CacheConnection monitor going to sleep");
      }
      try {
        // 1000 milliseconds/second x 60 seconds/minute x 5 minutes
        monitor.sleep(1000 * 60 * 5);
      } catch (InterruptedException ignore) {
        if (verbose) {
          System.out
              .println("CacheConnection monitor's sleep was interrupted");
        }
      }
    }
  }
  public void finalize() throws Throwable {
    CachedConnection cached = null;
    for (int i = 0; i < numberConnections; i++) {
      cached = (CachedConnection) cachedConnections.get(i);
      if (cached.getConnection() != null) {
        if (verbose) {
          System.out.println("Closing connection on Vector entry "
              + Integer.toString(i));
        }
        try {
          cached.getConnection().close();
        } catch (SQLException ignore) {
          System.err.println("Can't close connection!!!");
        }
      }
    }
    numberConnections = 0;
  }
  public static void setVerbose(boolean v) {
    verbose = v;
  }
}
class CachedConnection {
  private boolean inUse;
  private Connection conn;
  private long lastUsed;
  private String baseName;
  public CachedConnection() {
    conn = null;
    inUse = false;
    lastUsed = System.currentTimeMillis();
    baseName = "Database";
  }
  public CachedConnection(Connection conn, boolean inUse) {
    this.conn = conn;
    this.inUse = inUse;
    this.lastUsed = System.currentTimeMillis();
    this.baseName = "Database";
  }
  public CachedConnection(Connection conn, boolean inUse, String baseName) {
    this.conn = conn;
    this.inUse = inUse;
    this.lastUsed = System.currentTimeMillis();
    this.baseName = baseName;
  }
  public Connection getConnection() {
    return conn;
  }
  public void setConnection(Connection conn) {
    this.conn = conn;
  }
  public boolean getInUse() {
    return inUse;
  }
  public boolean isInUse() {
    return inUse;
  }
  public void setInUse(boolean inUse) {
    if (!inUse)
      lastUsed = System.currentTimeMillis();
    this.inUse = inUse;
  }
  public String getBaseName() {
    return baseName;
  }
  public void setBaseName(String baseName) {
    this.baseName = baseName;
  }
  public long getLastUsed() {
    return lastUsed;
  }
}
class Database {
  private static boolean verbose = false;
  public static final Connection getConnection(String baseName) {
    Connection conn = null;
    String driver = null;
    String url = null;
    String username = null;
    String password = null;
    try {
      ResourceBundle resb = ResourceBundle.getBundle(baseName);
      driver = resb.getString("database.driver");
      url = resb.getString("database.url");
      username = resb.getString("database.username");
      password = resb.getString("database.password");
      Class.forName(driver);
    } catch (MissingResourceException e) {
      System.err.println("Missing Resource: " + e.getMessage());
      return conn;
    } catch (ClassNotFoundException e) {
      System.err.println("Class not found: " + e.getMessage());
      return conn;
    }
    try {
      if (verbose) {
        System.out.println("baseName=" + baseName);
        System.out.println("driver=" + driver);
        System.out.println("url=" + url);
        System.out.println("username=" + username);
        System.out.println("password=" + password);
      }
      conn = DriverManager.getConnection(url, username, password);
    } catch (SQLException e) {
      System.err.println(e.getMessage());
      System.err.println("in Database.getConnection");
      System.err.println("on getConnection");
      conn = null;
    } finally {
      return conn;
    }
  }
  public static void setVerbose(boolean v) {
    verbose = v;
  }
}
```

Related examples in the same category
---
1. Servlets Database Query
2. Using JDBC in Servlets
3. Transaction Connection Servlet
4. Session Login JDBC
5. JDBC and Servlet
6. Database and Servlet: Database MetaData
7. Database and Servlet: Store procedure
8. Database transaction
9. Typical database commands
10. Process a raw SQL query; use ResultSetMetaData to format it
11. See Account
12. Guest Book Servlet
13. Dedicated Connection Servlet
14. Login Servlets
15. OCCI Connection Servlet
