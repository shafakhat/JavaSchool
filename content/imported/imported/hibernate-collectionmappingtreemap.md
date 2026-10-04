---
title: Collection Mapping
nav: Collection Mapping
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20070501194046/http://www.java2s.com:80/Code/Java/Hibernate/CollectionMappingTreeMap.htm
---
Collection Mapping: TreeMap

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-mapping
    PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
    "http://hibernate.sourceforge.net/hibernate-mapping-2.0.dtd">
<hibernate-mapping>
    <class name="Console" table="console">
        <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
        <map name="games" table="game_instructions" sort="GameComparator" cascade="all">
            <key column="parent_id"/>
            <index-many-to-many column="game_id" class="Game"/>
            <many-to-many column="instructions_id" class="Instructions"/>
        </map>
        <property name="name" type="string"/>
    </class>
    <class name="Game" table="game">
        <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
        <property name="name" type="string"/>
    </class>
    <class name="Instructions" table="instructions">
        <id name="id" unsaved-value="0">
            <generator class="increment"/>
        </id>
        <property name="info" type="string"/>
    </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
import java.util.*;
public class Console {
  private int id;
  private String name;
  private Map games;
  public Console() {
  }
  public Console(String name) {
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
  public void setGames(Map m) {
    games = m;
  }
  public Map getGames() {
    return games;
  }
}
/////////////////////////////////////////////////////////////////////////
public class Game {
  private int id;
  private String name;
  public Game() {
  }
  public Game(String name) {
    this.name = name;
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
    public boolean equals(Object obj) {
        if (obj == null) return false;
        if (!this.getClass().equals(obj.getClass())) return false;
        Game obj2 = (Game)obj;
        if ((this.id == obj2.getId()) &&
            this.name.equals(obj2.getName())) {
            return true;
        }
    return false;
    }
    public int hashCode() {
        int tmp = 0;
        tmp = (id + name).hashCode();
        return tmp;
    }
}
/////////////////////////////////////////////////////////////////////////
import java.util.*;
public class GameComparator implements Comparator {
  public int compare(Object o1, Object o2) {
        Game game1 = (Game)o1;
        Game game2 = (Game)o2;
       return game1.getName().compareTo(game2.getName());
    }
    public boolean equals(Object obj) {
        if (obj == null) return false;
        if (!this.getClass().equals(obj.getClass())) return false;
    return true;
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
        <mapping resource="Console.hbm.xml"/>
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
      HibernateUtil.setup("create table console (id int, name varchar);");
      HibernateUtil.setup("create table game (id int, name varchar);");
      HibernateUtil.setup("create table instructions (id int, info varchar );");
      HibernateUtil.setup("create table game_instructions (parent_id int,game_id int,instructions_id int);");
      Session session = HibernateUtil.currentSession();
      Console sp = new Console("Console");
      TreeMap p = new TreeMap(new GameComparator());
      Game g = new Game("Game 1");
      Game g2 = new Game("Game 2");
      p.put(g, new Instructions("Instructions for Game 1"));
      p.put(g2, new Instructions("Instructions for Game 2"));
      sp.setGames(p);
      session.save(g);
      session.save(g2);
      session.flush();
      session.save(sp);
      session.flush();
      session.flush();
      session.close();
      HibernateUtil.checkData("select * from console");
      HibernateUtil.checkData("select * from game");
      HibernateUtil.checkData("select * from instructions");
      HibernateUtil.checkData("select * from game_instructions");
   }
}
```

Download: HibernateCollectionTreeMap.zip ( 4,581 K )
Related examples in the same category
