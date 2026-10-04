---
title: AVG With GroupBy clause
nav: AVG With GroupBy clause
description: EntityManagerFactory emf = Persistence.createEntityManagerFactory("ProfessorService");
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20081209042629/http://www.java2s.com:80/Code/Java/JPA/AVGWithGroupByclause.htm
---
AVG With GroupBy clause

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
    service.executetQuery("SELECT d.name, AVG(e.salary) FROM Department d JOIN d.employees e GROUP BY d.name");
    util.checkData("select * from Professor");
    em.getTransaction().commit();
    em.close();
    emf.close();
  }
}
File: Address.java
import javax.persistence.Entity;
import javax.persistence.Id;
@Entity
public class Address {
    @Id
    private int id;
    private String street;
    private String city;
    private String state;
    private String zip;
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
    public String toString() {
        return "Address id: " + getId() +
               ", street: " + getStreet() +
               ", city: " + getCity() +
               ", state: " + getState() +
               ", zip: " + getZip();
    }
}
File: Department.java
import java.util.HashSet;
import java.util.Set;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
@Entity
public class Department {
    @Id
    private int id;
    private String name;
    @OneToMany(mappedBy="department")
    private Set<Professor> employees = new HashSet<Professor>();
    public int getId() {
        return id;
    }
    public void setId(int deptNo) {
        this.id = deptNo;
    }
    public String getName() {
        return name;
    }
    public void setName(String deptName) {
        this.name = deptName;
    }
    public Set<Professor> getProfessors() {
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
File: Phone.java
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;
@Entity
public class Phone {
    @Id
    private long id;
    private String number;
    private String type;
    @OneToOne Professor employee;
    public long getId() {
        return id;
    }
    public void setId(long id) {
        this.id = id;
    }
    public String getNumber() {
        return number;
    }
    public void setNumber(String phoneNo) {
        this.number = phoneNo;
    }
    public String getType() {
        return type;
    }
    public void setType(String phoneType) {
        this.type = phoneType;
    }
    public Professor getProfessor() {
        return employee;
    }
    public void setProfessor(Professor employee) {
        this.employee = employee;
    }
    public String toString() {
        return "Phone id: " + getId() +
               ", no: " + getNumber() +
               ", type: " + getType();
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
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
@Entity
public class Professor {
    @Id
    private int id;
    private String name;
    private long salary;
    @Temporal(TemporalType.DATE)
    private Date startDate;
    @OneToOne
    private Address address;
    @OneToMany(mappedBy="employee")
    private Collection<Phone> phones = new ArrayList<Phone>();
    @ManyToOne
    private Department department;
    @ManyToOne
    private Professor manager;
    @OneToMany(mappedBy="manager")
    private Collection<Professor> directs = new ArrayList<Professor>();
    @ManyToMany(mappedBy="employees")
    private Collection<Project> projects = new ArrayList<Project>();
    public int getId() {
        return id;
    }
    public void setId(int empNo) {
        this.id = empNo;
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
    public Date getStartDate() {
        return startDate;
    }
    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }
    public Collection<Phone> getPhones() {
        return phones;
    }
    public void addPhone(Phone phone) {
        if (!getPhones().contains(phone)) {
            getPhones().add(phone);
            if (phone.getProfessor() != null) {
                phone.getProfessor().getPhones().remove(phone);
            }
            phone.setProfessor(this);
        }
    }
    public Department getDepartment() {
        return department;
    }
    public void setDepartment(Department department) {
        if (this.department != null) {
            this.department.getProfessors().remove(this);
        }
        this.department = department;
        this.department.getProfessors().add(this);
    }
    public Collection<Professor> getDirects() {
        return directs;
    }
    public void addDirect(Professor employee) {
        if (!getDirects().contains(employee)) {
            getDirects().add(employee);
            if (employee.getManager() != null) {
                employee.getManager().getDirects().remove(employee);
            }
            employee.setManager(this);
        }
    }
    public Professor getManager() {
        return manager;
    }
    public void setManager(Professor manager) {
        this.manager = manager;
    }
    public Collection<Project> getProjects() {
        return projects;
    }
    public void addProject(Project project) {
        if (!getProjects().contains(project)) {
            getProjects().add(project);
        }
        if (!project.getProfessors().contains(this)) {
            project.getProfessors().add(this);
        }
    }
    public Address getAddress() {
        return address;
    }
    public void setAddress(Address address) {
        this.address = address;
    }
    public String toString() {
        return "Professor " + getId() +
               ": name: " + getName() +
               ", salary: " + getSalary() +
               ", phones: " + getPhones() +
               ", managerNo: " + ((getManager() == null) ? null : getManager().getId()) +
               ", deptNo: " + ((getDepartment() == null) ? null : getDepartment().getId());
    }
}
File: ProfessorService.java
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.Query;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public List executetQuery(String queryString) {
    Query query = em.createQuery(queryString);
    return query.getResultList();
  }
  public void executeUpdate(String updateString) {
    em.createQuery(updateString).executeUpdate();
  }
}
File: Project.java
import java.util.ArrayList;
import java.util.Collection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Inheritance;
import javax.persistence.ManyToMany;
@Entity
@Inheritance
public class Project {
    @Id
    protected int id;
    protected String name;
    @ManyToMany
    protected Collection<Professor> employees = new ArrayList<Professor>();
    public int getId() {
        return id;
    }
    public void setId(int projectNo) {
        this.id = projectNo;
    }
    public String getName() {
        return name;
    }
    public void setName(String projectName) {
        this.name = projectName;
    }
    public Collection<Professor> getProfessors() {
        return employees;
    }
    public void addProfessor(Professor employee) {
        if (!getProfessors().contains(employee)) {
            getProfessors().add(employee);
        }
        if (!employee.getProjects().contains(this)) {
            employee.getProjects().add(this);
        }
    }
    public String toString() {
        return getClass().getName().substring(getClass().getName().lastIndexOf('.')+1) +
                " no: " + getId() +
                ", name: " + getName();
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

JPA-EJBQLAVGWithGroupBy.zip( 5,340 k)
1.  Simple Select statement
2.  Select Two Entities
3.  Get Two Properties From Entity
4.  Get String Properties From Entities
5.  Retrieve Inner Entity
6.  Retrieve in One to Many Mapping
7.  Reference Two Entities In Where Clause
8.  Retrieve Entity Fields
9.  Create Sub Query With Entities
10.  Use OrderBy Clause
11.  Order By Two Columns
12.  Order By Descending
13.  EJB QL: Having clause
14.  All Operator in EJB QL
15.  EJB QL: Where Clause With SubQuery
16.  Using Exists clause
17.  Aggregate function: Count And Avg
18.  EJB QL: Concat Function With Substring
19.  Aggregate function: AVG
20.  Use Size Function To Check Collection
21.  Use In With One To One Mapping
22.  Not IN
23.  Not Exist With Subquery
24.  Not Empty
25.  Match Single Character And Multiple Characters
26.  MemberOf function
27.  OBJECT Funtion
28.  Left Join
29.  Join Two Entities in One To One Mapping
30.  Join Two Entities in Many To One Mapping
31.  Join Three Entities
32.  Join Fetch
33.  Using In function
34.  Group By With Count
35.  Escape wildcard
36.  Entity Join With Condition
37.  Empty Value
38.  Distinct function
39.  Count Entities
40.  Count Collection
41.  Conditional operator: AND
42.  Between...And
43.  Any With Subquery
44.  Subquery in EJB QL
