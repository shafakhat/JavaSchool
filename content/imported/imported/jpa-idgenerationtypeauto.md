---
title: ID Generation Type AUTO
nav: ID Generation Type AUTO
description: return "Professor id: " + getId() + " name: " + getName() + " salary: " + getSalary();
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20090126060642/http://www.java2s.com:80/Code/Java/JPA/IDGenerationTypeAUTO.htm
---
```java title=Example.java
File: Professor.java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
@Entity
public class Professor {
  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private int id;
  private String name;
  private long salary;
  public Professor() {
  }
  public Professor(int id) {
    this.id = id;
  }
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
  public long getSalary() {
    return salary;
  }
  public void setSalary(long salary) {
    this.salary = salary;
  }
  public String toString() {
    return "Professor id: " + getId() + " name: " + getName() + " salary: " + getSalary();
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
  public Professor createProfessor(String name, long salary) {
    Professor emp = new Professor();
    emp.setName(name);
    emp.setSalary(salary);
    em.persist(emp);
    return emp;
  }
  public void removeProfessor(int id) {
    Professor emp = findProfessor(id);
    if (emp != null) {
      em.remove(emp);
    }
  }
  public Professor raiseProfessorSalary(int id, long raise) {
    Professor emp = em.find(Professor.class, id);
    if (emp != null) {
      emp.setSalary(emp.getSalary() + raise);
    }
    return emp;
  }
  public Professor findProfessor(int id) {
    return em.find(Professor.class, id);
  }
  public Collection<Professor> findAllProfessors() {
    Query query = em.createQuery("SELECT e FROM Professor e");
    return (Collection<Professor>) query.getResultList();
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
    Professor emp = service.createProfessor("AAA", 45000);
    em.getTransaction().commit();
    System.out.println("Persisted " + emp);
    util.checkData("select * from Professor");
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

JPA-IDGenerationTypeAUTO.zip( 5,333 k)
1.  Use Table Generator To Generate ID
2.  Set Initial Value Of Table Generator
3.  ID Generation Type: TABLE
4.  ID Generation Type: IDENTITY
5.  ID For Two Entities From One Table
6.  Create Your Own Table For Table Generator
