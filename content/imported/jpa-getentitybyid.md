---
title: Get Entity by ID
nav: Get Entity by ID
description: return "Professor id: " + getId() + " name: " + getName() + " salary: " + getSalary();
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20090222193759/http://www.java2s.com:80/Code/Java/JPA/GetEntitybyID.htm
---
Get Entity by ID

```java title=Example.java
File: Professor.java
import javax.persistence.Entity;
import javax.persistence.Id;
@Entity
public class Professor {
    @Id
    private int id;
    private String name;
    private long salary;
    public Professor() {}
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
  public Professor createProfessor(int id, String name, long salary) {
    Professor emp = new Professor(id);
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
import java.util.Collection;
import java.util.Iterator;
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
    Professor emp = service.createProfessor(1, "name", 100);
    emp = service.createProfessor(2, "name 2", 100);
    Integer userId = 1;
    emp = em.find(Professor.class, userId);
    if (emp == null) {
      System.out.println(userId + " not found! ");
    } else {
      System.out.println("Found " + emp);
    }
    for (Object o : em.createQuery("SELECT u FROM Professor u").getResultList()) {
      System.out.println(o);
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

JPA-GetEntitybyID.zip( 5,333 k)
1.  Find Object By Class
2.  Find One Object
3.  Find All Objects
