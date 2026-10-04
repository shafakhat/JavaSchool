---
title: ID For Two Entities From One Table
nav: ID For Two Entities From O...
description: @TableGenerator(name = "Address_Gen", table = "ID_GEN", pkColumnName = "GEN_NAME", valueColumnName = "GEN_VAL", pkColumnValue = "Addr_Gen", initialValue = 10000, allocati
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20090124012740/http://java2s.com:80/Code/Java/JPA/IDForTwoEntitiesFromOneTable.htm
---
```java title=Example.java
File: Address.java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.TableGenerator;
@Entity
public class Address {
  @TableGenerator(name = "Address_Gen", table = "ID_GEN", pkColumnName = "GEN_NAME", valueColumnName = "GEN_VAL", pkColumnValue = "Addr_Gen", initialValue = 10000, allocationSize = 100)
  @Id
  @GeneratedValue(strategy = GenerationType.TABLE, generator = "Address_Gen")
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
    return "Address id: " + getId() + ", street: " + getStreet() + ", city: " + getCity()
        + ", state: " + getState() + ", zip: " + getZip();
  }
}
File: Professor.java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.TableGenerator;
@Entity
public class Professor {
  @TableGenerator(name = "Emp_Gen", table = "ID_GEN", pkColumnName = "GEN_NAME", valueColumnName = "GEN_VAL")
  @Id
  @GeneratedValue(strategy = GenerationType.TABLE, generator = "Emp_Gen")
  private int id;
  private String name;
  private long salary;
  @OneToOne
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
  public long getSalary() {
    return salary;
  }
  public void setSalary(long salary) {
    this.salary = salary;
  }
  public Address getAddress() {
    return address;
  }
  public void setAddress(Address address) {
    this.address = address;
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
  public Professor createProfessor(String name, long salary,
          String street, String city, String state, String zip) {
      Professor emp = new Professor();
      emp.setName(name);
      emp.setSalary(salary);
      Address addr = new Address();
      addr.setStreet(street);
      addr.setCity(city);
      addr.setState(state);
      addr.setZip(zip);
      emp.setAddress(addr);
      em.persist(emp);
      em.persist(addr);
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
    Professor emp = service.createProfessor("name", 100,
        "street", "city", "state", "zip");
    em.getTransaction().commit();
    System.out.println("Persisted " + emp);
    util.checkData("select * from Professor");
    util.checkData("select * from ADDRESS");
    util.checkData("select * from ID_GEN");
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

JPA-IDForTwoEntitiesFromOneTable.zip( 5,336 k)
1.  Use Table Generator To Generate ID
2.  Set Initial Value Of Table Generator
3.  ID Generation Type: TABLE
4.  ID Generation Type: IDENTITY
5.  ID Generation Type AUTO
6.  Create Your Own Table For Table Generator
