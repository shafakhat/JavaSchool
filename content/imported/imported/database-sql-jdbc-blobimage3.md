---
title: Blob
nav: Blob
description: private JButton getAccountButton, updateAccountButton, insertAccountButton,
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20070113113748/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/Blobimage3.htm
---
Blob: image 3

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
import java.awt.Graphics2D;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.geom.AffineTransform;
import java.awt.image.BufferedImage;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.util.Vector;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
public class IDlook extends JFrame {
  private JButton getAccountButton, updateAccountButton, insertAccountButton,
      nextButton, previousButton, lastButton, firstButton;
  private JList accountNumberList;
  private JTextField accountIDText, nailFileText, thumbIDText;
  private JTextArea errorText;
  private Connection connection;
  private Statement statement;
  private ResultSet rs;
  private ImageIcon icon = null;
  private ImageIcon iconThumbnail = null;
  JLabel photographLabel;
  public IDlook() {
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
      rs = statement.executeQuery("SELECT * FROM thumbnail");
      while (rs.next()) {
        v.addElement(rs.getString("acc_id"));
      }
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
          rs.beforeFirst();
          while (rs.next()) {
            if (rs.getString("acc_id").equals(
                accountNumberList.getSelectedValue()))
              break;
          }
          if (!rs.isAfterLast()) {
            accountIDText.setText(rs.getString("acc_id"));
            thumbIDText.setText(rs.getString("thumb_id"));
            icon = new ImageIcon(rs.getBytes("pic"));
            createThumbnail();
            photographLabel.setIcon(iconThumbnail);
          }
        } catch (SQLException selectException) {
          displaySQLErrors(selectException);
        }
      }
    });
    //Do Update Account Button
    updateAccountButton = new JButton("Update Account");
    updateAccountButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          byte[] bytes = new byte[50000];
          FileInputStream fs = new FileInputStream(nailFileText
              .getText());
          BufferedInputStream bis = new BufferedInputStream(fs);
          bis.read(bytes);
          rs.updateBytes("thumbnail.pic", bytes);
          rs.updateRow();
          bis.close();
          accountNumberList.removeAll();
          loadAccounts();
        } catch (SQLException insertException) {
          displaySQLErrors(insertException);
        } catch (Exception generalE) {
          generalE.printStackTrace();
        }
      }
    });
    //Do insert Account Button
    insertAccountButton = new JButton("Insert Account");
    insertAccountButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          byte[] bytes = new byte[50000];
          FileInputStream fs = new FileInputStream(nailFileText
              .getText());
          BufferedInputStream bis = new BufferedInputStream(fs);
          bis.read(bytes);
          rs.moveToInsertRow();
          rs.updateInt("thumb_id", Integer.parseInt(thumbIDText
              .getText()));
          rs.updateInt("acc_id", Integer.parseInt(accountIDText
              .getText()));
          rs.updateBytes("pic", bytes);
          rs.updateObject("sysobject", null);
          rs.updateTimestamp("ts", new Timestamp(0));
          rs.updateTimestamp("act_ts", new Timestamp(
              new java.util.Date().getTime()));
          rs.insertRow();
          bis.close();
          accountNumberList.removeAll();
          loadAccounts();
        } catch (SQLException insertException) {
          displaySQLErrors(insertException);
        } catch (Exception generalE) {
          generalE.printStackTrace();
        }
      }
    });
    photographLabel = new JLabel();
    photographLabel.setHorizontalAlignment(JLabel.CENTER);
    photographLabel.setVerticalAlignment(JLabel.CENTER);
    photographLabel.setVerticalTextPosition(JLabel.CENTER);
    photographLabel.setHorizontalTextPosition(JLabel.CENTER);
    JPanel first = new JPanel(new GridLayout(4, 1));
    first.add(accountNumberListScrollPane);
    first.add(getAccountButton);
    first.add(updateAccountButton);
    first.add(insertAccountButton);
    accountIDText = new JTextField(15);
    thumbIDText = new JTextField(15);
    errorText = new JTextArea(5, 15);
    errorText.setEditable(false);
    JPanel second = new JPanel();
    second.setLayout(new GridLayout(2, 1));
    second.add(thumbIDText);
    second.add(accountIDText);
    JPanel third = new JPanel();
    third.add(new JScrollPane(errorText));
    nailFileText = new JTextField(25);
    c.add(first);
    c.add(second);
    c.add(third);
    c.add(nailFileText);
    c.add(photographLabel);
    setSize(500, 500);
    show();
  }
  public void connectToDB() {
    try {
      connection = DriverManager
          .getConnection("jdbc:mysql://192.168.1.25/identification?user=spider&password=spider");
      statement = connection.createStatement(
          ResultSet.TYPE_SCROLL_INSENSITIVE,
          ResultSet.CONCUR_UPDATABLE);
    } catch (SQLException connectException) {
      System.out.println(connectException.getMessage());
      System.out.println(connectException.getSQLState());
      System.out.println(connectException.getErrorCode());
      System.exit(1);
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
  private void createThumbnail() {
    int maxDim = 350;
    try {
      Image inImage = icon.getImage();
      double scale = (double) maxDim / (double) inImage.getHeight(null);
      if (inImage.getWidth(null) > inImage.getHeight(null)) {
        scale = (double) maxDim / (double) inImage.getWidth(null);
      }
      int scaledW = (int) (scale * inImage.getWidth(null));
      int scaledH = (int) (scale * inImage.getHeight(null));
      BufferedImage outImage = new BufferedImage(scaledW, scaledH,
          BufferedImage.TYPE_INT_RGB);
      AffineTransform tx = new AffineTransform();
      if (scale < 1.0d) {
        tx.scale(scale, scale);
      }
      Graphics2D g2d = outImage.createGraphics();
      g2d.drawImage(inImage, tx, null);
      g2d.dispose();
      iconThumbnail = new ImageIcon(outImage);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  public static void main(String[] args) {
    IDlook id = new IDlook();
    id.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    id.init();
    id.buildGUI();
  }
}
```

Related examples in the same category
---
1. Insert picture to MySQL
2. Demo Display Binary Data From Database
3. Materialize binary data onto client
4. Blob: JDBC deals with Binary Data
5. Blob and JDBC: Image
6. Blob: Image 2
