---
title: Enumerated Value Mapping
nav: Enumerated Value Mapping
description: EntityManagerFactory emf = Persistence.createEntityManagerFactory("JPAService");
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20090106060607/http://www.java2s.com:80/Code/Java/JPA/EnumeratedValueMappingEnumTypeSTRING.htm
---
Enumerated Value Mapping: EnumType.STRING

```java title=Example.java
File: Gender.java
public enum Gender {
  MALE, FEMALE
}
File: Student.java
import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.Id;
@Entity
public class Student {
  @Id
  private long id = 0;
  private String name;
  private Date dateOfBirth = new Date();
  @Enumerated(EnumType.STRING)
  private Gender gender;
  public Date getDateOfBirth() {
    return dateOfBirth;
  }
  public void setDateOfBirth(Date dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }
  public long getId() {
    return id;
  }
  public void setId(long id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public Gender getGender() {
    return gender;
  }
  public void setGender(Gender gender) {
    this.gender = gender;
  }
}
File: JPADAO.java
import java.util.Date;
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;
public class JPADAO {
  EntityManagerFactory emf = Persistence.createEntityManagerFactory("JPAService");
  EntityManager em = emf.createEntityManager();
  public void create() {
    em.getTransaction().begin();
    Student student = new Student();
    student.setId(1);
    student.setName("Joe");
    student.setDateOfBirth(new Date());
    student.setGender(Gender.FEMALE);
    em.persist(student);
    em.flush();
    em.getTransaction().commit();
  }
  public void search() {
    Query q = em.createQuery("select m from Student m");
    for (Student m : (List<Student>) q.getResultList()) {
      System.out.println(m.getName() + " (Birthday: " + m.getDateOfBirth() + ")");
    }
  }
  public void close() {
    em.close();
    emf.close();
  }
}
File: Main.java
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;
public class Main {
  public static void main(String[] a) throws Exception {
    JPADAO jpaDao = new JPADAO();
    jpaDao.create();
    jpaDao.search();
    jpaDao.close();
    Helper.checkData();
  }
}
/*
    [java] Table Name: STUDENT
    [java]  Row:
    [java]     Column Name: ID,
    [java]     Column Type: BIGINT:
    [java]     Column Value: 1
    [java]     Column Name: DATEOFBIRTH,
    [java]     Column Type: TIMESTAMP:
    [java]     Column Value: 2008-11-05 13:32:00.35
    [java]     Column Name: GENDER,
    [java]     Column Type: VARCHAR:
    [java]     Column Value: FEMALE
    [java]     Column Name: NAME,
    [java]     Column Type: VARCHAR:
    [java]     Column Value: Joe
*/
File: Helper.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
public class Helper {
  public static void checkData() throws Exception {
    Class.forName("org.hsqldb.jdbcDriver");
    Connection conn = DriverManager.getConnection("jdbc:hsqldb:data/tutorial", "sa", "");
    Statement st = conn.createStatement();
    ResultSet mrs = conn.getMetaData().getTables(null, null, null, new String[] { "TABLE" });
    while (mrs.next()) {
      String tableName = mrs.getString(3);
      System.out.println("\n\n\n\nTable Name: "+ tableName);
      ResultSet rs = st.executeQuery("select * from " + tableName);
      ResultSetMetaData metadata = rs.getMetaData();
      while (rs.next()) {
        System.out.println(" Row:");
        for (int i = 0; i < metadata.getColumnCount(); i++) {
          System.out.println("    Column Name: "+ metadata.getColumnLabel(i + 1)+ ",  ");
          System.out.println("    Column Type: "+ metadata.getColumnTypeName(i + 1)+ ":  ");
          Object value = rs.getObject(i + 1);
          System.out.println("    Column Value: "+value+"\n");
        }
      }
    }
  }
}
File: persistence.xml
<persistence xmlns="http://java.sun.com/xml/ns/persistence"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://java.sun.com/xml/ns/persistence http://java.sun.com/xml/ns/persistence/persistence" version="1.0">
  <persistence-unit name="JPAService" transaction-type="RESOURCE_LOCAL">
    <properties>
      <property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
      <property name="hibernate.hbm2ddl.auto" value="update"/>
      <property name="hibernate.connection.driver_class" value="org.hsqldb.jdbcDriver"/>
      <property name="hibernate.connection.username" value="sa"/>
      <property name="hibernate.connection.password" value=""/>
      <property name="hibernate.connection.url" value="jdbc:hsqldb:data/tutorial"/>
    </properties>
  </persistence-unit>
</persistence>
```

JPA-EnumeratedAndEnumTypeSTRING.zip( 5,290 k)
1.  Map Java Enum Type
2.  Enumerated EnumType ORDINAL
