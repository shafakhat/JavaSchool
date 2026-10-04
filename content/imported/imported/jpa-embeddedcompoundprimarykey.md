---
title: Embedded Compound Primary Key
nav: Embedded Compound Primary ...
description: return "Professor id: " + getId() + " name: " + getName() + " country: " + getCountry();
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20090926070742/http://www.java2s.com:80/Code/Java/JPA/EmbeddedCompoundPrimaryKey.htm
---
```java title=Example.java
File: Professor.java
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
@Entity
public class Professor {
  @EmbeddedId
  private ProfessorId id;
  private String name;
  private long salary;
  public Professor() {
  }
  public Professor(String country, int id) {
    this.id = new ProfessorId(country, id);
  }
  public int getId() {
    return id.getId();
  }
  public String getCountry() {
    return id.getCountry();
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
    return "Professor id: " + getId() + " name: " + getName() + " country: " + getCountry();
  }
}
File: ProfessorId.java
import java.io.Serializable;
import javax.persistence.Column;
import javax.persistence.Embeddable;
@Embeddable
public class ProfessorId implements Serializable{
  private String country;
  @Column(name = "EMP_ID")
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
    Professor emp = new Professor(country, id);
    emp.setName(name);
    emp.setSalary(salary);
    em.persist(emp);
    return emp;
  }
  public Professor findProfessor(String country, int id) {
    return (Professor) em.createQuery(
        "SELECT e FROM Professor e WHERE e.id.country = ?1 AND e.id.id = ?2")
        .setParameter(1, country).setParameter(2, id).getSingleResult();
  }
  public Collection<Professor> findAllProfessors() {
    Query query = em.createQuery("SELECT e FROM Professor e");
    return (Collection<Professor>) query.getResultList();
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
      System.out.println(emp1);
    }
    util.checkData("select * from Professor");
    em.getTransaction().commit();
    em.close();
    emf.close();
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

JPA-EmbeddedCompoundPrimaryKey.zip( 5,335 k)
