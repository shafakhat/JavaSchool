---
title: Define And Use Compound Primary Key
nav: Define And Use Compound Pr...
description: EntityManagerFactory emf = Persistence.createEntityManagerFactory("ProfessorService");
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20081231212114/http://www.java2s.com:80/Code/Java/JPA/DefineAndUseCompoundPrimaryKey.htm
---
Define And Use Compound Primary Key

```java title=Example.java
File: Main.java
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
public class Main {
  public static void main(String[] a) throws Exception {
    JPAUtil util = new JPAUtil();
    EntityManagerFactory emf = Persistence.createEntityManagerFactory("ProfessorService");
    EntityManager em = emf.createEntityManager();
    ProfessorService service = new ProfessorService(em);
    em.getTransaction().begin();
    service.createProfessor("country", 1, "name", 100);
    Professor emp = service.findProfessor("country", 1);
    System.out.println("Found " + emp);
    System.out.println("Professors:");
    for (Professor emp1 : service.findAllProfessors()) {
      System.out.print(emp1);
    }
    util.checkData("select * from Professor");
    em.getTransaction().commit();
    em.close();
    emf.close();
  }
}
File: JPAUtil.java
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
public class JPAUtil {
  Statement st;
  public JPAUtil() throws Exception{
    Class.forName("org.hsqldb.jdbcDriver");
    System.out.println("Driver Loaded.");
    String url = "jdbc:hsqldb:data/tutorial";
    Connection conn = DriverManager.getConnection(url, "sa", "");
    System.out.println("Got Connection.");
    st = conn.createStatement();
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
File: Professor.java
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.IdClass;
@Entity
@IdClass(ProfessorId.class)
public class Professor {
    @Id private String country;
    @Id
    @Column(name="EMP_ID")
    private int id;
    private String name;
    private long salary;
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getCountry() {
        return country;
    }
    public void setCountry(String country) {
        this.country = country;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public long getSalary() {
        return salary;
    }
    public void setSalary(long salary) {
        this.salary = salary;
    }
    public String toString() {
        return "Professor id: " + getId() + " name: " + getName() +
               " country: " + getCountry();
    }
}
File: ProfessorId.java
import java.io.Serializable;
public class ProfessorId implements Serializable {
  private String country;
  private int id;
  public ProfessorId() {
  }
  public ProfessorId(String country, int id) {
    this.country = country;
    this.id = id;
  }
  public String getCountry() {
    return country;
  }
  public int getId() {
    return id;
  }
  public boolean equals(Object o) {
    return ((o instanceof ProfessorId) && country.equals(((ProfessorId) o).getCountry()) && id == ((ProfessorId) o)
        .getId());
  }
  public int hashCode() {
    return country.hashCode() + id;
  }
}
File: ProfessorService.java
import java.util.Collection;
import javax.persistence.EntityManager;
import javax.persistence.Query;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public Professor createProfessor(String country, int id, String name, long salary) {
    Professor emp = new Professor();
    emp.setCountry(country);
    emp.setId(id);
    emp.setName(name);
    emp.setSalary(salary);
    em.persist(emp);
    return emp;
  }
  public Professor findProfessor(String country, int id) {
    return em.find(Professor.class, new ProfessorId(country, id));
  }
  public Collection<Professor> findAllProfessors() {
    Query query = em.createQuery("SELECT e FROM Professor e");
    return (Collection<Professor>) query.getResultList();
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

JPA-DefineAndUseCompoundPrimaryKey.zip( 5,335 k)
1.  Using System MiliSeconds As Key
2.  Use UUID As Primary Key
3.  Using Primary Key Column as Joined Column
4.  Set Primary Key Joined Column For Secondary Table
5.  Set IdClass for Compound Key
6.  Set Primary Key By Yourself
7.  Sequence Id Generation
8.  Relationship On Id
9.  Not Nullable ID
10.  Mark Entity ID As Generated Value From Table
11.  JPA can Create Sequence Table For You
