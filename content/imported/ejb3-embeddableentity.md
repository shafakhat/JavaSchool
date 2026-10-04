---
title: Embeddable Entity
nav: Embeddable Entity
description: public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20090204180843/http://www.java2s.com:80/Code/Java/EJB3/EmbeddableEntity.htm
---
```java title=Example.java
File: EmployeeService.java
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
@Stateless
public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
  @PersistenceContext(unitName="EmployeeService")
  EntityManager em;
  public EmployeeService() {
  }
  public void doAction(){
    Employee cust = new Employee();
    cust.setFirstName("B");
    cust.setLastName("B");
    Address address = new Address();
    address.setStreet("Street");
    address.setCity("Boston");
    address.setState("MA");
    cust.setAddress(address);
    em.persist(cust);
    em.flush();
    System.out.println("saved");
  }
}
File: EmployeeServiceLocal.java
import java.util.Collection;
import javax.ejb.Local;
@Local
public interface EmployeeServiceLocal {
    public void doAction();
}
File: EmployeeServiceRemote.java
import java.util.Collection;
import javax.ejb.Remote;
@Remote
public interface EmployeeServiceRemote{
  public void doAction();
}
File: Address.java
import javax.persistence.Column;
import javax.persistence.Embeddable;
@Embeddable
public class Address implements java.io.Serializable {
   private String street;
   private String city;
   private String state;
   @Column(name="STREET")
   public String getStreet() { return street; }
   public void setStreet(String street) { this.street = street; }
   @Column(name="CITY")
   public String getCity() { return city; }
   public void setCity(String city) { this.city = city; }
   @Column(name="STATE")
   public String getState() { return state; }
   public void setState(String state) { this.state = state; }
}
File: Employee.java
import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
@Entity
public class Employee implements java.io.Serializable {
  private long id;
  private String firstName;
  private String lastName;
  private Address address;
  @Id
  @GeneratedValue
  public long getId() {
    return id;
  }
  public void setId(long id) {
    this.id = id;
  }
  public String getFirstName() {
    return firstName;
  }
  public void setFirstName(String first) {
    this.firstName = first;
  }
  public String getLastName() {
    return lastName;
  }
  public void setLastName(String last) {
    this.lastName = last;
  }
  @Embedded
  @AttributeOverrides( { @AttributeOverride(name = "street", column = @Column(name = "STREET")),
      @AttributeOverride(name = "city", column = @Column(name = "CITY")),
      @AttributeOverride(name = "state", column = @Column(name = "STATE")) })
  public Address getAddress() {
    return address;
  }
  public void setAddress(Address address) {
    this.address = address;
  }
}
File: Main.java
import java.util.Collection;
import javax.naming.InitialContext;
public class Main {
  public static void main(String[] a) throws Exception {
    EmployeeServiceRemote service = null;
    // Context compEnv = (Context) new InitialContext().lookup("java:comp/env");
    // service = (HelloService)new InitialContext().lookup("java:comp/env/ejb/HelloService");
    service = (EmployeeServiceRemote) new InitialContext().lookup("EmployeeService/remote");
    service.doAction();
  }
}
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
```

EJB-EmbeddableEntity.zip( 4,489 k)
1.  Entity With Date
2.  Get List Of Employees From Ejb
3.  Flush Data In EJB
4.  Use PersistenceUnit
5.  Use PersistenceContext annotation to Link Persistence Context
6.  Set Flush Mode
7.  Set Column Name For Entity Attribute
8.  Retrieve Data From Ejb
9.  Persistence Context Type: TRANSACTION
10.  Persistence Context Type: EXTENDED
