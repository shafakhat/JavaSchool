---
title: Create More than one Named Queries for an Entity
nav: Create More than one Named...
description: ", dept: " + ((getDepartment() == null) ? null : getDepartment().getName());
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20081221015118/http://www.java2s.com:80/Code/Java/JPA/CreateMorethanoneNamedQueriesforanEntity.htm
---
Create More than one Named Queries for an Entity

```java title=Example.java
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
    public String getName() {
        return name;
    }
    public Collection<Professor> getProfessors() {
        return employees;
    }
    public String toString() {
        return "Department no: " + getId() +
               ", name: " + getName();
    }
}
File: Professor.java
import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
@Entity
@NamedQueries({
  @NamedQuery(name="Professor.findAll",
              query="SELECT e FROM Professor e"),
  @NamedQuery(name="Professor.findByPrimaryKey",
              query="SELECT e FROM Professor e WHERE e.id = :id"),
  @NamedQuery(name="Professor.findByName",
              query="SELECT e FROM Professor e WHERE e.name = :name")
})
public class Professor {
    @Id
    private int id;
    private String name;
    private long salary;
    @Temporal(TemporalType.DATE)
    private Date startDate;
    @ManyToOne
    private Professor manager;
    @OneToMany(mappedBy="manager")
    private Collection<Professor> directs;
    @ManyToOne
    private Department department;
    @ManyToMany
    private Collection<Project> projects;
    public Professor() {
        projects = new ArrayList<Project>();
        directs = new ArrayList<Professor>();
    }
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public long getSalary() {
        return salary;
    }
    public Date getStartDate() {
        return startDate;
    }
    public Department getDepartment() {
        return department;
    }
    public Collection<Professor> getDirects() {
        return directs;
    }
    public Professor getManager() {
        return manager;
    }
    public Collection<Project> getProjects() {
        return projects;
    }
    public String toString() {
        return "Professor " + getId() +
               ": name: " + getName() +
               ", salary: " + getSalary() +
               ", dept: " + ((getDepartment() == null) ? null : getDepartment().getName());
    }
}
File: ProfessorService.java
import java.util.Collection;
import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public Professor findProfessorByName(String name) {
    try {
      return (Professor) em.createNamedQuery("Professor.findByName").setParameter("name", name)
          .getSingleResult();
    } catch (NoResultException e) {
      return null;
    }
  }
}
File: Project.java
import java.util.ArrayList;
import java.util.Collection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
@Entity
public class Project {
    @Id
    protected int id;
    protected String name;
    @ManyToMany(mappedBy="projects")
    private Collection<Professor> employees;
    public Project() {
        employees = new ArrayList<Professor>();
    }
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public Collection<Professor> getProfessors() {
        return employees;
    }
    public String toString() {
        return "Project id: " + getId() + ", name: " + getName();
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
    Professor l = service.findProfessorByName("empName");
    util.checkData("select * from Professor");
    util.checkData("select * from Department");
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

JPA-NamedQueries.zip( 5,335 k)
1.  Create Named Query With Entity
2.  Named Query Without Parameter
3.  Named Query With Two Parameters
4.  Query Hints Example
