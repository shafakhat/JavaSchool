---
title: BiDirection One To One Mappoing
nav: BiDirection One To One Map...
description: return "Address id: " + getId() + ", street: " + getStreet() + ", city: " + getCity()
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20090119164051/http://www.java2s.com:80/Code/Java/JPA/BiDirectionOneToOneMappoing.htm
---
```java title=Example.java
File: Address.java
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;
@Entity
public class Address {
  @Id
  private int id;
  private String street;
  private String city;
  private String state;
  private String zip;
  @OneToOne(cascade=CascadeType.ALL)
  private Student student;
  public int getId() {
    return id;
  }
  public void setId(int id) {
    this.id = id;
  }
  public String getStreet() {
    return street;
  }
  public void setStreet(String address) {
    this.street = address;
  }
  public String getCity() {
    return city;
  }
  public void setCity(String city) {
    this.city = city;
  }
  public String getState() {
    return state;
  }
  public void setState(String state) {
    this.state = state;
  }
  public String getZip() {
    return zip;
  }
  public void setZip(String zip) {
    this.zip = zip;
  }
  public Student getStudent() {
    return student;
  }
  public void setStudent(Student student) {
    this.student = student;
  }
  public String toString() {
    return "Address id: " + getId() + ", street: " + getStreet() + ", city: " + getCity()
        + ", state: " + getState() + ", zip: " + getZip();
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
import java.util.List;
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
    Address address = new Address();
    address.setCity("city");
    address.setStudent(student);
  //em.persist(address);
    student.setAddress(address);
    em.persist(student);
    em.flush();
    em.getTransaction().commit();
    Query query = em.createQuery("SELECT e FROM Address e");
    List<Address> list = (List<Address>) query.getResultList();
    System.out.println(list.get(0).getStudent());
    em.close();
    emf.close();
    Helper.checkData();
  }
}
File: Student.java
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;
@Entity
public class Student {
  @Id
  private int id;
  private String name;
  @OneToOne(cascade=CascadeType.ALL)
  private Address address;
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
  public Address getAddress() {
    return address;
  }
  public void setAddress(Address address) {
    this.address = address;
  }
  public String toString() {
    return "\n\nID:" + id + "\nName:" + name + "\n\n";
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

JPA-BiDirectionOneToOneMappoing.zip( 5,289 k)
1.  Mark Entity RelationShip As One To One
2.  One To One Unidirectional Mapping
3.  One To One Mapping Based On Table Based ID
4.  One To One MappedBy
5.  One To One Mapping: Lazy load
6.  One To One Bidirectional
7.  Retrieve One To One Mapped Entity
