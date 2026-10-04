---
title: Applet and Oracle JDBC : Java examples (example source code) » Database SQL JDBC » Database Swing Applet
nav: Applet and Oracle JDBC : J...
description: Applet and Oracle JDBC : Java examples (example source code) » Database SQL JDBC » Database Swing Applet
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20060503130343/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/AppletandOracleJDBC.htm
---
Applet and Oracle JDBC : Java examples (example source code) » Database SQL JDBC » Database Swing Applet

Applet and Oracle JDBC

```java title=Example.java
/*
Java Programming with Oracle JDBC
by Donald Bales
ISBN: 059600088X
Publisher: O'Reilly
*/
import java.applet.Applet;
import java.awt.Graphics;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
public class TestApplet extends Applet {
  private Connection conn;
  private Timestamp created = new Timestamp(System.currentTimeMillis());
  public void init() {
    try {
      System.out
          .println("init(): loading OracleDriver for applet created at "
              + created.toString());
      Class.forName("oracle.jdbc.driver.OracleDriver");
      System.out.println("init(): getting connection");
      conn = DriverManager.getConnection(
          "jdbc:oracle:thin:@dssw2k01:1521:orcl", "scott", "tiger");
    } catch (ClassNotFoundException e) {
      System.err.println("init(): ClassNotFoundException: "
          + e.getMessage());
    } catch (SQLException e) {
      System.err.println("init(): SQLException: " + e.getMessage());
    }
  }
  public void start() {
    System.out.println("start(): ");
  }
  public void stop() {
    System.out.println("stop(): ");
  }
  public void paint(Graphics g) {
    System.out.println("paint(): querying the database");
    try {
      Statement stmt = conn.createStatement();
      ResultSet rset = stmt
          .executeQuery("select 'Hello '||initcap(USER) result from dual");
      while (rset.next())
        g.drawString(rset.getString(1), 10, 10);
      rset.close();
      stmt.close();
    } catch (SQLException e) {
      System.err.println("paint(): SQLException: " + e.getMessage());
    }
  }
  public void destroy() {
    System.out
        .println("destroy(): closing connection for applet created at "
            + created.toString());
    try {
      conn.close();
    } catch (SQLException e) {
      System.err.println("destroy: SQLException: " + e.getMessage());
    }
  }
}
//TestApplet.html
/*
<html>
<head>
</head>
<body>
<applet code=TestApplet archive=TestApplet.zip width=100 height=50></applet>
</body>
</html>
*/
```

Related examples in the same category
---
1. Java database and Swing
2. Accounts
3. Applet JDBC
4. RowSet Model based on TableModel (JTable)
5. JDBC Applet running in Netscape
6. JDBC Applet Policy
7. This is a demonstration JDBC applet
