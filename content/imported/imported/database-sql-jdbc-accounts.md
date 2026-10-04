---
title: Accounts : Java examples (example source code) » Database SQL JDBC » Database Swing Applet
nav: Accounts : Java examples (...
description: Accounts : Java examples (example source code) » Database SQL JDBC » Database Swing Applet
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20060503130617/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/Accounts.htm
---
Accounts : Java examples (example source code) » Database SQL JDBC » Database Swing Applet

Accounts

```java title=Example.java
/*
MySQL and Java Developer's Guide
Mark Matthews, Jim Cole, Joseph D. Gradecki
Publisher Wiley,
Published February 2003,
ISBN 0471269239
*/
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Vector;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
public class Accounts extends JFrame {
  private JButton getAccountButton, insertAccountButton, deleteAccountButton,
      updateAccountButton;
  private JList accountNumberList;
  private Connection connection;
  private JTextField accountIDText, usernameText, passwordText, tsText,
      activeTSText;
  private JTextArea errorText;
  public Accounts() {
    try {
      Class.forName("com.mysql.jdbc.Driver").newInstance();
    } catch (Exception e) {
      System.err.println("Unable to find and load driver");
      System.exit(1);
    }
  }
  private void loadAccounts() {
    Vector v = new Vector();
    try {
      Statement statement = connection.createStatement();
      ResultSet rs = statement.executeQuery("SELECT acc_id FROM acc_acc");
      while (rs.next()) {
        v.addElement(rs.getString("acc_id"));
      }
      rs.close();
    } catch (SQLException e) {
      displaySQLErrors(e);
    }
    accountNumberList.setListData(v);
  }
  private void buildGUI() {
    Container c = getContentPane();
    c.setLayout(new FlowLayout());
    accountNumberList = new JList();
    loadAccounts();
    accountNumberList.setVisibleRowCount(2);
    JScrollPane accountNumberListScrollPane = new JScrollPane(
        accountNumberList);
    //Do Get Account Button
    getAccountButton = new JButton("Get Account");
    getAccountButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          Statement statement = connection.createStatement();
          ResultSet rs = statement
              .executeQuery("SELECT * FROM acc_acc WHERE acc_id = "
                  + accountNumberList.getSelectedValue());
          if (rs.next()) {
            accountIDText.setText(rs.getString("acc_id"));
            usernameText.setText(rs.getString("username"));
            passwordText.setText(rs.getString("password"));
            tsText.setText(rs.getString("ts"));
            activeTSText.setText(rs.getString("act_ts"));
          }
        } catch (SQLException selectException) {
          displaySQLErrors(selectException);
        }
      }
    });
    //Do Insert Account Button
    insertAccountButton = new JButton("Insert Account");
    insertAccountButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          Statement statement = connection.createStatement();
          int i = statement
              .executeUpdate("INSERT INTO acc_acc VALUES("
                  + accountIDText.getText() + ", " + "'"
                  + usernameText.getText() + "', " + "'"
                  + passwordText.getText() + "', " + "0"
                  + ", " + "now())");
          errorText.append("Inserted " + i + " rows successfully");
          accountNumberList.removeAll();
          loadAccounts();
        } catch (SQLException insertException) {
          displaySQLErrors(insertException);
        }
      }
    });
    //Do Delete Account Button
    deleteAccountButton = new JButton("Delete Account");
    deleteAccountButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          Statement statement = connection.createStatement();
          int i = statement
              .executeUpdate("DELETE FROM acc_acc WHERE acc_id = "
                  + accountNumberList.getSelectedValue());
          errorText.append("Deleted " + i + " rows successfully");
          accountNumberList.removeAll();
          loadAccounts();
        } catch (SQLException insertException) {
          displaySQLErrors(insertException);
        }
      }
    });
    //Do Update Account Button
    updateAccountButton = new JButton("Update Account");
    updateAccountButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          Statement statement = connection.createStatement();
          int i = statement.executeUpdate("UPDATE acc_acc "
              + "SET username='" + usernameText.getText() + "', "
              + "password='" + passwordText.getText() + "', "
              + "act_ts = now() " + "WHERE acc_id = "
              + accountNumberList.getSelectedValue());
          errorText.append("Updated " + i + " rows successfully");
          accountNumberList.removeAll();
          loadAccounts();
        } catch (SQLException insertException) {
          displaySQLErrors(insertException);
        }
      }
    });
    JPanel first = new JPanel(new GridLayout(5, 1));
    first.add(accountNumberListScrollPane);
    first.add(getAccountButton);
    first.add(insertAccountButton);
    first.add(deleteAccountButton);
    first.add(updateAccountButton);
    accountIDText = new JTextField(15);
    usernameText = new JTextField(15);
    passwordText = new JTextField(15);
    tsText = new JTextField(15);
    activeTSText = new JTextField(15);
    errorText = new JTextArea(5, 15);
    errorText.setEditable(false);
    JPanel second = new JPanel();
    second.setLayout(new GridLayout(6, 1));
    second.add(accountIDText);
    second.add(usernameText);
    second.add(passwordText);
    second.add(tsText);
    second.add(activeTSText);
    JPanel third = new JPanel();
    third.add(new JScrollPane(errorText));
    c.add(first);
    c.add(second);
    c.add(third);
    setSize(500, 500);
    show();
  }
  public void connectToDB() {
    try {
      connection = DriverManager
          .getConnection("jdbc:mysql://192.168.1.25/accounts?user=spider&password=spider");
    } catch (SQLException connectException) {
      System.out.println(connectException.getMessage());
      System.out.println(connectException.getSQLState());
      System.out.println(connectException.getErrorCode());
    }
  }
  private void displaySQLErrors(SQLException e) {
    errorText.append("SQLException: " + e.getMessage() + "\n");
    errorText.append("SQLState:     " + e.getSQLState() + "\n");
    errorText.append("VendorError:  " + e.getErrorCode() + "\n");
  }
  private void init() {
    connectToDB();
  }
  public static void main(String[] args) {
    Accounts accounts = new Accounts();
    accounts.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    accounts.init();
    accounts.buildGUI();
  }
}
```

Related examples in the same category
---
1. Java database and Swing
2. Applet JDBC
3. RowSet Model based on TableModel (JTable)
4. Applet and Oracle JDBC
5. JDBC Applet running in Netscape
6. JDBC Applet Policy
7. This is a demonstration JDBC applet
