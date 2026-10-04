---
title: Cascade Type PERSIST
nav: Cascade Type PERSIST
description: Connection conn = DriverManager.getConnection(url, "sa", "");
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20090504061426/http://www.java2s.com:80/Code/Java/JPA/CascadeTypePERSIST.htm
---
Cascade Type PERSIST

```java title=Example.java
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
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
@Entity
public class Professor {
    @Id
    private int id;
    private String name;
    @ManyToOne(cascade=CascadeType.PERSIST)
    Address address;
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
    public Address getAddress() {
        return address;
    }
    public void setAddress(Address address) {
        this.address = address;
    }
    public String toString() {
        return "Professor id: " + getId() + " name: " + getName() +
               " with " + getAddress();
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
  public Professor createProfessorAndAddress(int id, String name, int addrId, String street,
      String city, String state) {
    Professor emp = new Professor();
    emp.setId(id);
    emp.setName(name);
    Address addr = new Address();
    addr.setId(addrId);
    addr.setStreet(street);
    addr.setCity(city);
    addr.setState(state);
    emp.setAddress(addr);
    em.persist(emp);
    return emp;
  }
  public Collection<Professor> findAllProfessors() {
    Query query = em.createQuery("SELECT e FROM Professor e");
    return (Collection<Professor>) query.getResultList();
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
    service.createProfessorAndAddress(1, "name", 1, "street", "city", "state");
    for (Professor emp : service.findAllProfessors()) {
      System.out.print(emp);
    }
    util.checkData("select * from Professor");
    util.checkData("select * from Address");
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

JPA-CascadeTypePERSIST.zip( 5,335 k)
1.  Use Cascade.All to save linked entities automatically
2.  Many To One Mapping Cascade Type REFRESH
3.  Many To One Cascasde Persist
4.  Many To One Cascade Remove
5.  Many To One Mapping Cascade Merge
6.  Cascade Type REMOVE
