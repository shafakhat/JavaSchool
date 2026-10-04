---
title: Create Your Own Table For Table Generator
nav: Create Your Own Table For ...
description: Connection conn = DriverManager.getConnection("jdbc:hsqldb:data/tutorial", "sa", "");
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20090126060657/http://www.java2s.com:80/Code/Java/JPA/CreateYourOwnTableForTableGenerator.htm
---
Create Your Own Table For Table Generator

```java title=Example.java
File: Student.java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.TableGenerator;
@Entity
public class Student {
  @Id
  @TableGenerator(name = "EmpPkGen",
      table = "ID_GEN",
      pkColumnName = "GEN_NAME",
      pkColumnValue = "Emp_Gen",
      valueColumnName = "GEN_VAL",
      initialValue = 0,
      allocationSize = 100
   )
  @GeneratedValue(strategy=GenerationType.TABLE)
/*create table id_gen (
    gen_name varchar(80),
    gen_val integer,
    constraint pk_id_gen
        primary key (gen_name)
);
*/
  private int id;
  transient private String name;
  public int getId() {
    return id;
  }
  public void setId(int id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public String toString() {
    return "\n\nID:" + id + "\nName:" + name + "\n\n";
  }
}
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
File: Main.java
import java.sql.Timestamp;
import java.util.List;
import java.util.UUID;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;
public class Main {
  static EntityManagerFactory emf = Persistence.createEntityManagerFactory("JPAService");
  static EntityManager em = emf.createEntityManager();
  public static void main(String[] a) throws Exception {
    em.getTransaction().begin();
    Student student = new Student();
    student.setName("Joe");
    em.persist(student);
    em.flush();
    em.getTransaction().commit();
    Query query = em.createQuery("SELECT e FROM Student e");
    List<Student> list = (List<Student>) query.getResultList();
    System.out.println(list);
    em.close();
    emf.close();
    Helper.checkData();
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

JPA-CreateYourOwnTableForTableGenerator.zip( 5,288 k)
1.  Use Table Generator To Generate ID
2.  Set Initial Value Of Table Generator
3.  ID Generation Type: TABLE
4.  ID Generation Type: IDENTITY
5.  ID Generation Type AUTO
6.  ID For Two Entities From One Table
