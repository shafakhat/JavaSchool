---
title: Applet JDBC : Java examples (example source code) » Database SQL JDBC » Database Swing Applet
nav: Applet JDBC : Java example...
description: Applet JDBC : Java examples (example source code) » Database SQL JDBC » Database Swing Applet
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20060503130610/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/AppletJDBC.htm
---
Applet JDBC : Java examples (example source code) » Database SQL JDBC » Database Swing Applet

Applet JDBC

```java title=Example.java
/*
MySQL and Java Developer's Guide
Mark Matthews, Jim Cole, Joseph D. Gradecki
Publisher Wiley,
Published February 2003,
ISBN 0471269239
*/
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Vector;
import javax.swing.JApplet;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JScrollPane;
public class AppletJDBCDrop extends JApplet implements ActionListener {
  private Connection connection;
  private JList tableList;
  private JButton dropButton;
  public void init() {
    Connection connection;
    try {
      Class.forName("com.mysql.jdbc.Driver").newInstance();
      connection = DriverManager
          .getConnection("jdbc:mysql://192.168.1.25/accounts?user=spider&password=spider");
    } catch (Exception connectException) {
      connectException.printStackTrace();
    }
    Container c = getContentPane();
    tableList = new JList();
    loadTables();
    c.add(new JScrollPane(tableList), BorderLayout.NORTH);
    dropButton = new JButton("Drop Table");
    dropButton.addActionListener(this);
    c.add(dropButton, BorderLayout.SOUTH);
  }
  public void actionPerformed(ActionEvent e) {
    try {
      Statement statement = connection.createStatement();
      ResultSet rs = statement.executeQuery("DROP TABLE "
          + tableList.getSelectedValue());
    } catch (SQLException actionException) {
    }
  }
  private void loadTables() {
    Vector v = new Vector();
    try {
      Statement statement = connection.createStatement();
      ResultSet rs = statement.executeQuery("SHOW TABLES");
      while (rs.next()) {
        v.addElement(rs.getString(1));
      }
      rs.close();
    } catch (SQLException e) {
    }
    v.addElement("acc_acc");
    v.addElement("acc_add");
    v.addElement("junk");
    tableList.setListData(v);
  }
}
/*
<html>
<applet code="Drop.class" width=200 height=200>
</applet>
</html>
*/
```

Related examples in the same category
---
1. Java database and Swing
2. Accounts
3. RowSet Model based on TableModel (JTable)
4. Applet and Oracle JDBC
5. JDBC Applet running in Netscape
6. JDBC Applet Policy
7. This is a demonstration JDBC applet
