---
title: Container Managed Transaction
nav: Container Managed Transact...
description: public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20090503054932/http://www.java2s.com:80/Code/Java/EJB3/ContainerManagedTransaction.htm
---
Container Managed Transaction

```java title=Example.java
File: EmployeeService.java
import java.util.Collection;
import javax.annotation.Resource;
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import javax.ejb.TransactionManagement;
import javax.ejb.TransactionManagementType;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;
import javax.transaction.UserTransaction;
@Stateless
public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
  @PersistenceContext(unitName="EmployeeService")
  EntityManager em;
  public EmployeeService() {
  }
  public Employee createEmployee(int id, String name, long salary, byte[] pic) {
    Employee emp = new Employee(id);
    emp.setName(name);
    emp.setSalary(salary);
    emp.setPicture(pic);
    em.persist(emp);
    emp = findEmployee(id);
    System.out.println(emp);
    return emp;
  }
  public void removeEmployee(int id) {
    Employee emp = findEmployee(id);
    if (emp != null) {
      em.remove(emp);
    }
  }
  public Employee raiseEmployeeSalary(int id, long raise) {
    Employee emp = em.find(Employee.class, id);
    if (emp != null) {
      emp.setSalary(emp.getSalary() + raise);
    }
    return emp;
  }
  public Employee findEmployee(int id) {
    return em.find(Employee.class, id);
  }
  public Collection<Employee> findAllEmployees() {
    Query query = em.createQuery("SELECT e FROM Employee e");
    return (Collection<Employee>) query.getResultList();
  }
  public void doAction(){
    Employee emp = new Employee(1);
    emp.setName("name");
    emp.setSalary(100);
    emp.setPicture("pic".getBytes());
    em.persist(emp);
    emp = findEmployee(1);
    System.out.println(emp);
  }
}
File: EmployeeServiceLocal.java
import javax.ejb.Local;
@Local
public interface EmployeeServiceLocal {
    public void doAction();
  public Employee createEmployee(int id, String name, long salary, byte[] pic) ;
}
File: EmployeeServiceRemote.java
import javax.ejb.Remote;
@Remote
public interface EmployeeServiceRemote{
  public Employee createEmployee(int id, String name, long salary, byte[] pic) ;
  public void doAction();
}
File: Employee.java
import static javax.persistence.FetchType.LAZY;
import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.Table;
@Entity
//@Table(name="EMP", schema="HR")
@Table(name="EMP")
public class Employee implements Serializable {
  @Id
  @Column(name = "EMP_ID")
  private int id;
  @Column(name = "COMM")
  private String name;
  @Column(name = "SAL")
  private long salary;
  @Basic(fetch=LAZY)
  @Lob @Column(name="PIC")
  private byte[] picture;
  public Employee() {
  }
  public Employee(int id) {
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
  public byte[] getPicture() {
    return picture;
  }
  public void setPicture(byte[] picture) {
    this.picture = picture;
  }
  public String toString() {
    return "Employee id: " + getId() + " name: " + getName() + " salary: " + getSalary();
  }
}
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
File: Main.java
import javax.naming.InitialContext;
public class Main {
  public static void main(String[] a) throws Exception {
    EmployeeServiceRemote service = null;
    // Context compEnv = (Context) new InitialContext().lookup("java:comp/env");
    // service = (HelloService)new InitialContext().lookup("java:comp/env/ejb/HelloService");
    service = (EmployeeServiceRemote) new InitialContext().lookup("EmployeeService/remote");
    service.createEmployee(158, "AAA", 45000, "asdf".getBytes());
    service.doAction();
  }
}
```

EJB-ContainerManageTransaction.zip( 4,490 k)
1.  Container Managed Transaction: TransactionAttributeType.SUPPORTS
2.  Transaction Management Type: BEAN
3.  Transaction Attribute Type: SUPPORTS
4.  Transaction Attribute Type: REQUIRES_NEW
5.  Use User Transaction In Client Side
6.  Inject Transaction As Resource
7.  Mark Statful Session Bean As Transaction Attribute Type: REQUIRES_NEW
8.  Container Managed Transaction: Required
