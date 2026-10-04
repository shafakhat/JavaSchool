---
title: Create Sub Query With Entities
nav: Create Sub Query With Enti...
description: ", dept: " + ((getDepartment() == null) ? null : getDepartment().getName());
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20081209042710/http://www.java2s.com:80/Code/Java/JPA/CreateSubQueryWithEntities.htm
---
Create Sub Query With Entities

```java title=Example.java
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
@NamedQuery(name="findHighestPaidByDepartment",
    query="SELECT e " +
          "FROM Professor e " +
          "WHERE e.department = :dept AND " +
          "      e.salary = (SELECT MAX(e2.salary) " +
          "                  FROM Professor e2 " +
          "                  WHERE e2.department = :dept)")
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
File: ProfessorService.java
import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public Professor findHighestPaidByDepartment(Department dept) {
    try {
        return (Professor) em.createNamedQuery("findHighestPaidByDepartment")
                            .setParameter("dept", dept)
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
File: Main.java
import java.util.Collection;
import java.util.Date;
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
    util.checkData("select * from Professor");
    util.checkData("select * from Department");
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

JPA-SubQueryWithEntities.zip( 5,336 k)
1.  Simple Select statement
2.  Select Two Entities
3.  Get Two Properties From Entity
4.  Get String Properties From Entities
5.  Retrieve Inner Entity
6.  Retrieve in One to Many Mapping
7.  Reference Two Entities In Where Clause
8.  Retrieve Entity Fields
9.  Use OrderBy Clause
10.  Order By Two Columns
11.  Order By Descending
12.  EJB QL: Having clause
13.  All Operator in EJB QL
14.  EJB QL: Where Clause With SubQuery
15.  Using Exists clause
16.  Aggregate function: Count And Avg
17.  EJB QL: Concat Function With Substring
18.  Aggregate function: AVG
19.  Use Size Function To Check Collection
20.  Use In With One To One Mapping
21.  Not IN
22.  Not Exist With Subquery
23.  Not Empty
24.  Match Single Character And Multiple Characters
25.  MemberOf function
26.  OBJECT Funtion
27.  Left Join
28.  Join Two Entities in One To One Mapping
29.  Join Two Entities in Many To One Mapping
30.  Join Three Entities
31.  Join Fetch
32.  Using In function
33.  Group By With Count
34.  Escape wildcard
35.  Entity Join With Condition
36.  Empty Value
37.  Distinct function
38.  Count Entities
39.  Count Collection
40.  Conditional operator: AND
41.  Between...And
42.  AVG With GroupBy clause
43.  Any With Subquery
44.  Subquery in EJB QL
