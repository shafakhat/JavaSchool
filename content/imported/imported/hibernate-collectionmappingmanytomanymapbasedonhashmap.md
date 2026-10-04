---
title: Collection Mapping
nav: Collection Mapping
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20070117030941/http://www.java2s.com:80/Code/Java/Hibernate/CollectionMappingManyToManymapbasedonHashMap.htm
---
Collection Mapping: Many-To-Many map based on HashMap

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
public class Benefit {
  private int id;
  private int cost;
  public Benefit() {
  }
  public Benefit(int c) {
    cost = c;
  }
  public void setId(int i) {
    id = i;
  }
  public int getId() {
    return id;
  }
  public void setCost(int i) {
    cost = i;
  }
  public int getCost() {
    return cost;
  }
}
/////////////////////////////////////////////////////////////////////////
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-mapping
    PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
    "http://hibernate.sourceforge.net/hibernate-mapping-2.0.dtd">
<hibernate-mapping>
    <class name="Employee" table="employee">
        <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
        <map name="benefits" table="employee_benefit" cascade="all">
            <key column="parent_id"/>
            <index column="benefit_name" type="string"/>
            <many-to-many column="benefit_id" class="Benefit"/>
        </map>
        <property name="name" type="string"/>
    </class>
    <class name="Benefit" table="benefit">
        <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
        <property name="cost" type="int"/>
    </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
import java.util.*;
public class Employee {
  private int id;
  private String name;
  private Map benefits;
  public Employee() {
  }
  public void setId(int i) {
    id = i;
  }
  public int getId() {
    return id;
  }
  public void setName(String s) {
    name = s;
  }
  public String getName() {
    return name;
  }
  public void setBenefits(Map m) {
    benefits = m;
  }
  public Map getBenefits() {
    return benefits;
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
        <mapping resource="Employee.hbm.xml"/>
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
      HibernateUtil.setup("create table employee (id int,name varchar);");
      HibernateUtil.setup("create table benefit (id int,cost int);");
      HibernateUtil.setup("create table employee_benefit (parent_id int,benefit_name varchar,benefit_id int);");
      Session session = HibernateUtil.currentSession();
      Employee sp = new Employee();
      Employee sp3 = new Employee();
      sp.setName("Joe");
      HashMap p = new HashMap();
      p.put("health", new Benefit(200));
      p.put("dental", new Benefit(300));
      sp.setBenefits(p);
      sp3.setName("Jim");
      sp3.setBenefits(p);
      session.save(sp);
      session.save(sp3);
      session.flush();
      HibernateUtil.closeSession();
      session = HibernateUtil.currentSession();
      Employee sp2 = (Employee)session.load(Employee.class, new Integer(sp.getId()));
      Map p2 = sp2.getBenefits();
      System.out.println(((Benefit)p2.get("health")).getCost());
      System.out.println(((Benefit)p2.get("dental")).getCost());
      session.flush();
      session.close();
      HibernateUtil.checkData("select * from employee");
      HibernateUtil.checkData("select * from benefit");
      HibernateUtil.checkData("select * from employee_benefit");
   }
}
```

Download: HibernateCollectionMappingMappingAnObjectMapMany-To-Many_Element.zip ( 4,581 K )
Related examples in the same category
