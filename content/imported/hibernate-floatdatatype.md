---
title: Float Data Type
nav: Float Data Type
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20070504045357/http://www.java2s.com:80/Code/Java/Hibernate/FloatDataType.htm
---
```java title=Example.java
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
import java.util.*;
import java.sql.*;
import org.hibernate.*;
import org.hibernate.cfg.*;
import org.hibernate.criterion.*;
import org.hibernate.event.*;
import org.hibernate.event.def.*;
public class Main {
   public static void main(String[] args) throws Exception {
      HibernateUtil.setup("create table books(id int, title VARCHAR, author VARCHAR,isbn VARCHAR not null, pagecount int, copyright int, cost numeric(12,2));");
      Session session = HibernateUtil.currentSession();
      Book book = new Book();
      book.setTitle("Title");
      book.setIsbn("000000000000000");
      book.setAuthor("name");
      book.setCopyright(9);
      book.setPages(330);
      book.setCost(29.99f);
      session.save(book);
      session.flush();
      session.close();
      HibernateUtil.checkData("select * from books");
   }
}
/////////////////////////////////////////////////////////////////////////
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
public class HibernateUtil {
    public static final SessionFactory sessionFactory;
    static {
        try {
            // Create the SessionFactory from hibernate.cfg.xml
            sessionFactory = new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            // Make sure you log the exception, as it might be swallowed
            System.err.println("Initial SessionFactory creation failed." + ex);
            throw new ExceptionInInitializerError(ex);
        }
    }
    public static final ThreadLocal session = new ThreadLocal();
    public static Session currentSession() throws HibernateException {
        Session s = (Session) session.get();
        // Open a new Session, if this thread has none yet
        if (s == null) {
            s = sessionFactory.openSession();
            // Store it in the ThreadLocal variable
            session.set(s);
        }
        return s;
    }
    public static void closeSession() throws HibernateException {
        Session s = (Session) session.get();
        if (s != null)
            s.close();
        session.set(null);
    }
    static Connection conn;
    static Statement st;
  public static void setup(String sql) {
    try {
      // Step 1: Load the JDBC driver.
      Class.forName("org.hsqldb.jdbcDriver");
      System.out.println("Driver Loaded.");
      // Step 2: Establish the connection to the database.
      String url = "jdbc:hsqldb:data/tutorial";
      conn = DriverManager.getConnection(url, "sa", "");
      System.out.println("Got Connection.");
      st = conn.createStatement();
      st.executeUpdate(sql);
    } catch (Exception e) {
      System.err.println("Got an exception! ");
      e.printStackTrace();
      System.exit(0);
    }
  }
  public static void checkData(String sql) {
    try {
      HibernateUtil.outputResultSet(st
          .executeQuery(sql));
//      conn.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
    public static void outputResultSet(ResultSet rs) throws Exception{
    ResultSetMetaData metadata = rs.getMetaData();
    int numcols = metadata.getColumnCount();
    String[] labels = new String[numcols];
    int[] colwidths = new int[numcols];
    int[] colpos = new int[numcols];
    int linewidth;
      for (int i = 0; i < numcols; i++) {
        labels[i] = metadata.getColumnLabel(i + 1); // get its label
        System.out.print(labels[i]+"  ");
    }
      System.out.println("------------------------");
    while (rs.next()) {
        for (int i = 0; i < numcols; i++) {
        Object value = rs.getObject(i + 1);
        System.out.print(value.toString().trim()+"   ");
      }
    }
    }
}
/////////////////////////////////////////////////////////////////////////
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-configuration PUBLIC
    "-//Hibernate/Hibernate Configuration DTD//EN"
    "http://hibernate.sourceforge.net/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <!-- Database connection settings -->
        <property name="connection.driver_class">org.hsqldb.jdbcDriver</property>
        <property name="connection.url">jdbc:hsqldb:data/tutorial</property>
        <property name="connection.username">sa</property>
        <property name="connection.password"></property>
        <!-- JDBC connection pool (use the built-in) -->
        <property name="connection.pool_size">1</property>
        <!-- SQL dialect -->
        <property name="dialect">org.hibernate.dialect.HSQLDialect</property>
        <!-- Echo all executed SQL to stdout -->
        <property name="show_sql">true</property>
        <!-- Mapping files -->
        <mapping resource="Book.hbm.xml"/>
    </session-factory>
</hibernate-configuration>
/////////////////////////////////////////////////////////////////////////
public class Book{
  private int id;
  private String title;
  private String author;
  private String isbn;
  private int pages;
  private int copyright;
  private float cost;
  public Book() {
  }
  public void setId(int i) {
    id = i;
  }
  public int getId() {
    return id;
  }
  public void setTitle(String s) {
    title = s;
  }
  public String getTitle() {
    return title;
  }
  public void setAuthor(String s) {
    author = s;
  }
  public String getAuthor() {
    return author;
  }
  public void setIsbn(String s) {
    isbn = s;
  }
  public String getIsbn() {
    return isbn;
  }
  public void setPages(int i) {
    pages = i;
  }
  public int getPages() {
    return pages;
  }
  public void setCopyright(int i) {
    copyright = i;
  }
  public int getCopyright() {
    return copyright;
  }
  public void setCost(float f) {
    cost = f;
  }
  public float getCost() {
    return cost;
  }
}
/////////////////////////////////////////////////////////////////////////
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE hibernate-mapping PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
"http://hibernate.sourceforge.net/hibernate-mapping-2.0.dtd">
<hibernate-mapping>
<class name="Book" table="books">
   <id name="id" type="int" unsaved-value="0">
      <generator  class="increment"/>
   </id>
   <property   name="title"/>
   <property   name="author"/>
   <property   name="isbn" not-null="true"/>
   <property   name="pages" type="integer" column="pagecount" />
   <property   name="copyright"/>
   <property   name="cost">
      <column     name="cost" sql-type="NUMERIC(12,2)"/>
   </property>
</class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
```

Download: HibernateFloatDataType.zip ( 4,577 K )
---
Related examples in the same category
1. Java Type VS Hibernate Type
