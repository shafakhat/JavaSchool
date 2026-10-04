---
title: Detachment With Triggered Lazy Loading
nav: Detachment With Triggered ...
description: EntityManagerFactory emf = Persistence.createEntityManagerFactory("ProfessorService");
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20090605074211/http://www.java2s.com:80/Code/Java/JPA/DetachmentWithTriggeredLazyLoading.htm
---
Detachment With Triggered Lazy Loading

```java title=Example.java
File: Main.java
import java.util.Collection;
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
    service.findAll();
    util.checkData("select * from Professor");
    util.checkData("select * from Department");
    em.getTransaction().commit();
    em.close();
    emf.close();
  }
}
File: Department.java
import java.util.ArrayList;
import java.util.Collection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
@Entity
public class Department {
    @Id
    private int id;
    private String name;
    @OneToMany(mappedBy="department")
    private Collection<Professor> employees;
    public Department() {
        employees = new ArrayList<Professor>();
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
    public Collection<Professor> getProfessors() {
        return employees;
    }
    public String toString() {
        return "Department no: " + getId() +
               ", name: " + getName();
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
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
@Entity
public class Professor {
    @Id
    private int id;
    private String name;
    private long salary;
    @ManyToOne(fetch=FetchType.LAZY)
    private Department department;
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public long getSalary() {
        return salary;
    }
    public Department getDepartment() {
        return department;
    }
    public void setDepartment(Department dept) {
        this.department = dept;
    }
    public String toString() {
        return "Professor " + getId() +
               ": name: " + getName() +
               ", salary: " + getSalary();
    }
}
File: ProfessorService.java
import java.util.List;
import javax.persistence.EntityManager;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public List findAll() {
    List<Professor> emps = em.createQuery("SELECT e FROM Professor e")
                  .getResultList();
    for (Professor emp : emps) {
        if (emp.getDepartment() != null) {
            System.out.println(emp.getDepartment().getName());
        }
    }
    return emps;
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

JPA-DetachmentWithTriggeredLazyLoading.zip( 5,335 k)
1.  Detachment With Eager Loading
