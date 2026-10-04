---
title: Cast Result List To Generic Collection
nav: Cast Result List To Generi...
description: @OneToMany(targetEntity=Professor.class, mappedBy="department")
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20090528095054/http://www.java2s.com:80/Code/Java/JPA/CastResultListToGenericCollection.htm
---
Cast Result List To Generic Collection

```java title=Example.java
File: Department.java
import java.util.ArrayList;
import java.util.Collection;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
@Entity
public class Department {
    @Id @GeneratedValue(strategy=GenerationType.IDENTITY)
    private int id;
    private String name;
    @OneToMany(targetEntity=Professor.class, mappedBy="department")
    private Collection employees;
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
    public void setName(String deptName) {
        this.name = deptName;
    }
    public void addProfessor(Professor employee) {
        if (!getProfessors().contains(employee)) {
            getProfessors().add(employee);
            if (employee.getDepartment() != null) {
                employee.getDepartment().getProfessors().remove(employee);
            }
            employee.setDepartment(this);
        }
    }
    public Collection getProfessors() {
        return employees;
    }
    public String toString() {
        return "Department id: " + getId() +
               ", name: " + getName();
    }
}
File: Professor.java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
@Entity
public class Professor {
    @Id @GeneratedValue(strategy=GenerationType.IDENTITY)
    private int id;
    private String name;
    private long salary;
    @ManyToOne
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
    public void setName(String name) {
        this.name = name;
    }
    public long getSalary() {
        return salary;
    }
    public void setSalary(long salary) {
        this.salary = salary;
    }
    public Department getDepartment() {
        return department;
    }
    public void setDepartment(Department department) {
        this.department = department;
    }
    public String toString() {
        return "Professor id: " + getId() + " name: " + getName() +
               " with " + getDepartment();
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
  public Department createDepartment(String name) {
    Department dept = new Department();
    dept.setName(name);
    em.persist(dept);
    return dept;
  }
  public Collection<Department> findAllDepartments() {
    Query query = em.createQuery("SELECT d FROM Department d");
    return (Collection<Department>) query.getResultList();
  }
  public Professor createProfessor(String name, long salary) {
    Professor emp = new Professor();
    emp.setName(name);
    emp.setSalary(salary);
    em.persist(emp);
    return emp;
  }
  public Professor setProfessorDepartment(int empId, int deptId) {
    Professor emp = em.find(Professor.class, empId);
    Department dept = em.find(Department.class, deptId);
    dept.addProfessor(emp);
    return emp;
  }
  public Collection<Professor> findAllProfessors() {
    Query query = em.createQuery("SELECT e FROM Professor e");
    return (Collection<Professor>) query.getResultList();
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
    Professor emp = service.createProfessor("empName",100);
    Department dept = service.createDepartment("deptName");
    emp = service.setProfessorDepartment(emp.getId(),dept.getId());
    System.out.println(emp.getDepartment() + " with Professors:");
    System.out.println(emp.getDepartment().getProfessors());
    Collection<Professor> emps = service.findAllProfessors();
    if (emps.isEmpty()) {
        System.out.println("No Professors found ");
    } else {
        System.out.println("Found Professors:");
        for (Professor emp1 : emps) {
            System.out.println(emp1);
        }
    }
    Collection<Department> depts = service.findAllDepartments();
    if (depts.isEmpty()) {
        System.out.println("No Departments found ");
    } else {
        System.out.println("Found Departments:");
        for (Department dept1 : depts) {
            System.out.println(dept1 + " with " + dept1.getProfessors().size() + " employees");
        }
    }
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

JPA-CastResultListToGenericCollection.zip( 5,337 k)
1.  Using Entity Result
2.  Sql Resultset Mapping With Alias
3.  SQL Resultset Mapping: Two Entities
4.  SQL Resultset Mapping: One Entity
5.  Sql Resultset Mapping: Column Result
6.  Inheritance Result Mapping Two Subclasses
7.  Inheritance Result Mapping
