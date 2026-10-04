---
title: Column Formula
nav: Column Formula
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20070110034614/http://www.java2s.com:80/Code/Java/Hibernate/ColumnFormulaStringConcatenate.htm
---
Column Formula: String Concatenate

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-mapping PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
"http://hibernate.sourceforge.net/hibernate-mapping-2.0.dtd">
<hibernate-mapping>
    <class  name="Account" table="account">
        <id name="id" type="string" unsaved-value="null">
            <generator  class="uuid.hex"/>
        </id>
        <property   name="accountnum"/>
        <property   name="firstname"/>
        <property   name="lastname"/>
        <property   name="balance"/>
        <property   name="fullname" formula="concat(firstname, ' ', lastname)"/>
    </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
import java.io.*;
public class Account {
  private String id;
  private String accountnum;
  private double balance;
  private String firstname;
  private String lastname;
  private String fullname;
  public Account() {
  }
  public void setId(String s) {
    id = s;
  }
  public String getId() {
    return id;
  }
  public void setAccountnum(String s) {
    accountnum = s;
  }
  public String getAccountnum() {
    return accountnum;
  }
  public void setBalance(double b) {
    balance = b;
  }
  public double getBalance() {
    return balance;
  }
  public void setFirstname(String s) {
    firstname = s;
  }
  public String getFirstname() {
    return firstname;
  }
  public void setLastname(String s) {
    lastname = s;
  }
  public String getLastname() {
    return lastname;
  }
  public void setFullname(String s) {
    fullname = s;
  }
  public String getFullname() {
    return fullname;
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
        <mapping resource="Account.hbm.xml"/>
    </session-factory>
</hibernate-configuration>
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
        if(value == null){
            System.out.print("       ");
        }else{
            System.out.print(value.toString().trim()+"   ");
        }
      }
        System.out.println("       ");
    }
    }
}
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
import java.util.*;
import org.hibernate.*;
import org.hibernate.cfg.*;
import org.hibernate.criterion.*;
import org.hibernate.event.*;
import org.hibernate.event.def.*;
public class Main {
   public static void main(String[] args) throws Exception {
      HibernateUtil.setup("create table account(id varchar,accountnum varchar,firstname varchar,lastname varchar,balance double);");
      Session session = HibernateUtil.currentSession();
      Account account = new Account();
      account.setFirstname("Joe");
      account.setLastname("Smith");
      account.setAccountnum("39084");
      account.setBalance(4054.00);
      session.save(account);
      session.flush();
      Account account2 = (Account)session.load(Account.class, account.getId());
      System.out.println(account2.getFullname());
      session.flush();
      session.close();
      HibernateUtil.checkData("select * from account");
   }
}
/////////////////////////////////////////////////////////////////////////
log4j.rootCategory=WARN, console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%-4r [%t] %-5p %c %x - %m%n
log4j.appender.stdout.Target=System.out
```

Download: HibernateColumnFormulaConcatenate.zip ( 4,578 K )
Related examples in the same category
