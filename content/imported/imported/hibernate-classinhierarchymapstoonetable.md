---
title: Class In Hierarchy Maps To One Table
nav: Class In Hierarchy Maps To...
description: .executeSQLCommand("create table CD(id varchar,title varchar,artist varchar,purchaseDate date,cost decimal(6,2),languages varchar, newfeatures varchar)");
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20100415063223/http://www.java2s.com:80/Tutorial/Java/0350__Hibernate/ClassInHierarchyMapsToOneTable.htm
---
File: Main.java

```java title=Example.java
import java.util.Iterator;
import java.util.List;
import org.hibernate.Session;
public class Main {
  public static void main(String[] args) throws Exception {
    HibernateUtil hibernateUtil = new HibernateUtil();
    hibernateUtil
        .executeSQLCommand("create table CD(id varchar,title varchar,artist varchar,purchaseDate date,cost decimal(6,2),languages varchar, newfeatures varchar)");
    Session session = hibernateUtil.getSession();
    CD cd = new CD();
    cd.setArtist("artist");
    cd.setTitle("title");
    String id = (String)session.save(cd);
    System.out.println(id);
    SpecialEditionCD scd = new SpecialEditionCD();
    scd.setNewfeatures("new");
    session.save(scd);
    InternationalCD icd = new InternationalCD();
    icd.setLanguages("ENG");
    session.save(icd);
    session.flush();
    session.close();
    hibernateUtil.checkData("select * from CD");
  }
}
```

File: CD.java

```java title=Example.java
import java.util.Date;
public class CD {
  String id;
  String title;
  String artist;
  Date purchaseDate;
  double cost;
  public CD() {
  }
  public Date getPurchaseDate() {
    return purchaseDate;
  }
  public void setPurchaseDate(Date purchaseDate) {
    this.purchaseDate = purchaseDate;
  }
  public CD(String title, String artist, Date purchaseDate, double cost) {
    this.title = title;
    this.artist = artist;
    this.purchaseDate = purchaseDate;
    this.cost = cost;
  }
  public void setId(String id) {
    this.id = id;
  }
  public String getId() {
    return id;
  }
  public void setTitle(String title) {
    this.title = title;
  }
  public String getTitle() {
    return title;
  }
  public void setArtist(String artist) {
    this.artist = artist;
  }
  public String getArtist() {
    return artist;
  }
  public void setCost(double cost) {
    this.cost = cost;
  }
  public double getCost() {
    return cost;
  }
}
```

File: hibernate.cfg.xml

```java title=Example.java
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
        <!-- Enable Hibernate's current session context -->
        <property name="current_session_context_class">org.hibernate.context.ManagedSessionContext</property>
        <property name="hibernate.cache.use_second_level_cache">false</property>
        <property name="hibernate.cache.use_query_cache">false</property>
        <!-- Disable the second-level cache  -->
        <property name="cache.provider_class">org.hibernate.cache.NoCacheProvider</property>
        <!-- Echo all executed SQL to stdout -->
        <property name="show_sql">true</property>
        <!-- Mapping files -->
        <mapping resource="CD.hbm.xml"/>
    </session-factory>
</hibernate-configuration>
```

File: HibernateUtil.java

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
public class HibernateUtil {
  Session session;
  Statement st;
  Configuration config;
  public HibernateUtil() throws Exception{
    config = new Configuration().configure();
    SessionFactory sessionFactory = config.buildSessionFactory();
    session = sessionFactory.openSession();
    // Load the JDBC driver.
    Class.forName("org.hsqldb.jdbcDriver");
    System.out.println("Driver Loaded.");
    // Establish the connection to the database.
    String url = "jdbc:hsqldb:data/tutorial";
    Connection conn = DriverManager.getConnection(url, "sa", "");
    System.out.println("Got Connection.");
    st = conn.createStatement();
  }
  public Configuration getConfiguration(){
    return config;
  }
  public Session getSession(){
    return session;
  }
  public void executeSQLCommand(String sql) throws Exception {
    st.executeUpdate(sql);
  }
  public void checkData(String sql) throws Exception {
    ResultSet rs = st.executeQuery(sql);
    ResultSetMetaData metadata = rs.getMetaData();
    for (int i = 0; i < metadata.getColumnCount(); i++) {
      System.out.print("\t"+ metadata.getColumnLabel(i + 1));
    }
    System.out.println("\n----------------------------------");
    while (rs.next()) {
      for (int i = 0; i < metadata.getColumnCount(); i++) {
        Object value = rs.getObject(i + 1);
        if (value == null) {
          System.out.print("\t       ");
        } else {
          System.out.print("\t"+value.toString().trim());
        }
      }
      System.out.println("");
    }
  }
}
```

File: InternationalCD.java

```java title=Example.java
import java.util.*;
public class InternationalCD extends CD {
  private String languages;
  public InternationalCD() {
  }
  public InternationalCD(String title, String artist, Date purchaseDate, double cost, String language) {
    super(title, artist, purchaseDate, cost);
    languages = language;
  }
  public void setLanguages(String s) {
    languages = s;
  }
  public String getLanguages() {
    return languages;
  }
}
```

File: SpecialEditionCD.java

```java title=Example.java
import java.util.*;
public class SpecialEditionCD extends CD {
  private String newfeatures;
  public SpecialEditionCD() {
  }
    public SpecialEditionCD(String title, String artist, Date purchaseDate, double cost, String features) {
      super(title, artist, purchaseDate, cost);
      newfeatures = features;
    }
  public void setNewfeatures(String s) {
    newfeatures = s;
  }
  public String getNewfeatures() {
    return newfeatures;
  }
}
```

File: CD.hbm.xml

```java title=Example.java
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE hibernate-mapping
    PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
    "http://hibernate.sourceforge.net/hibernate-mapping-2.0.dtd">
<hibernate-mapping>
  <class name="CD" table="cd">
    <id name="Id" type="string" unsaved-value="null">
      <column name="ID" sql-type="text" not-null="true"/>
      <generator class="uuid.hex"/>
    </id>
    <property name="title"/>
    <property name="artist"/>
    <property name="purchaseDate" type="date"/>
    <property name="cost" type="double"/>
  </class>
    <class name="SpecialEditionCD" table="cd">
        <id name="id" type="string" unsaved-value="0">
          <generator  class="uuid.hex"/>
        </id>
        <property name="title"/>
    <property name="artist"/>
    <property name="purchaseDate" type="date"/>
    <property name="cost" type="double"/>
        <property name="newfeatures" type="string"/>
    </class>
    <class name="InternationalCD" table="cd">
        <id name="id" type="string" unsaved-value="0">
           <generator class="uuid.hex"/>
        </id>
      <property name="title"/>
    <property name="artist"/>
    <property name="purchaseDate" type="date"/>
    <property name="cost" type="double"/>
        <property name="languages"/>
</class>
</hibernate-mapping>
```

Download: HibernateClassInHierarchyMapsToOneTable.zip( 4,864 k)
