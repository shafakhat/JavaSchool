---
title: Discriminator Value in entity hierarchy
nav: Discriminator Value in ent...
description: public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20081201073609/http://www.java2s.com:80/Code/Java/EJB3/DiscriminatorValueinentityhierarchy.htm
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
    Person p = new Person();
    p.setFirstName("P");
    p.setLastName("P");
    em.persist(p);
    Customer cust = new Customer();
    cust.setFirstName("C");
    cust.setLastName("C");
    cust.setStreet("Street");
    cust.setCity("City");
    cust.setState("State");
    cust.setZip("11111");
    em.persist(cust);
    Employee employee = new Employee();
    employee.setFirstName("E");
    employee.setLastName("E");
    employee.setStreet("1st Street");
    employee.setCity("E City");
    employee.setState("E State");
    employee.setZip("33333");
    employee.setEmployeeId(15);
    em.persist(employee);
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
File: Employee.java
import javax.persistence.DiscriminatorColumn;
import javax.persistence.DiscriminatorType;
import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Inheritance;
import javax.persistence.InheritanceType;
import javax.persistence.Table;
@Entity
public class Employee extends Customer {
   private int employeeId;
   public int getEmployeeId() { return employeeId; }
   public void setEmployeeId(int id) { employeeId = id; }
}
@Entity
@DiscriminatorValue("CUST")
class Customer extends Person {
   private String street;
   private String city;
   private String state;
   private String zip;
   public String getStreet() { return street; }
   public void setStreet(String street) { this.street = street; }
   public String getCity() { return city; }
   public void setCity(String city) { this.city = city; }
   public String getState() { return state; }
   public void setState(String state) { this.state = state; }
   public String getZip() { return zip; }
   public void setZip(String zip) { this.zip = zip; }
}
@Entity
@Table(name="PERSON_HIERARCHY")
@Inheritance(strategy=InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name="DISCRIMINATOR",
                     discriminatorType=DiscriminatorType.STRING)
@DiscriminatorValue("PERSON")
class Person implements java.io.Serializable
{
   private int id;
   private String firstName;
   private String lastName;
   @Id @GeneratedValue
   public int getId() { return id; }
   public void setId(int id) { this.id = id; }
   public String getFirstName() { return firstName; }
   public void setFirstName(String first) { this.firstName = first; }
   public String getLastName() { return lastName; }
   public void setLastName(String last) { this.lastName = last; }
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

EJB-MarkDiscriminatorValue.zip( 4,490 k)
1.  Mark Ejb Method With Our Own Annotation
