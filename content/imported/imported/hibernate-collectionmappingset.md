---
title: Collection Mapping
nav: Collection Mapping
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20061025123842/http://www.java2s.com:80/Code/Java/Hibernate/CollectionMappingSet.htm
---
Collection Mapping: Set

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
public class GameScore {
  private int id;
  private String name;
  private int score;
  public GameScore() {
  }
  public GameScore(String name, int score) {
    this.name = name;
    this.score = score;
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
  public void setScore(int i) {
    score = i;
  }
  public int getScore() {
    return score;
  }
    public boolean equals(Object obj) {
        if (obj == null) return false;
        if (!this.getClass().equals(obj.getClass())) return false;
        GameScore obj2 = (GameScore)obj;
        if ((this.id == obj2.getId()) &&
            (this.name.equals(obj2.getName())) &&
            (this.score == obj2.getScore())
            ) {
            return true;
        }
    return false;
    }
    public int hashCode() {
        int tmp = 0;
        tmp = (id + name + score).hashCode();
        return tmp;
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
        <mapping resource="HighScores.hbm.xml"/>
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
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-mapping
    PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
    "http://hibernate.sourceforge.net/hibernate-mapping-2.0.dtd">
<hibernate-mapping>
    <class name="HighScores" table="highscores">
         <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
        <set name="games" cascade="all">
            <key column="parent_id"/>
            <one-to-many class="GameScore"/>
        </set>
        <property name="name" type="string"/>
    </class>
    <class name="GameScore" table="gamescores">
         <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
          <property name="name"/>
          <property name="score"/>
    </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
import java.util.*;
public class HighScores {
  private int id;
  private String name;
  private Set games;
  public HighScores() {
  }
  public HighScores(String name) {
    this.name = name;
  }
  public void setId(int i) {
    id = i;
  }
  public int getId() {
    return id;
  }
  public void setName(String n) {
    name = n;
  }
  public String getName() {
    return name;
  }
  public void setGames(Set games) {
    this.games = games;
  }
  public Set getGames() {
    return games;
  }
}
/////////////////////////////////////////////////////////////////////////
public class Instructions {
  private int id;
  private String info;
  public Instructions() {
  }
  public Instructions(String info) {
    this.info = info;
  }
  public void setId(int i) {
    id = i;
  }
  public int getId() {
    return id;
  }
  public void setInfo(String s) {
    info = s;
  }
  public String getInfo() {
    return info;
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
      HibernateUtil.setup("create table HighScores (id int,name varchar);");
      HibernateUtil.setup("create table gamescores (id int,name varchar,score int,parent_id int);");
      Session session = HibernateUtil.currentSession();
      HighScores sp = new HighScores("HighScores Name");
      HashSet set = new HashSet();
      set.add(new GameScore("GameScore Name 1", 3));
      set.add(new GameScore("GameScore Name 2", 2));
      sp.setGames(set);
      session.save(sp);
      session.flush();
      session.close();
      HibernateUtil.checkData("select * from HighScores");
      HibernateUtil.checkData("select * from gamescores");
   }
}
```

Download: HibernateCollectionMappingSet.zip ( 4,580 K )
Related examples in the same category
