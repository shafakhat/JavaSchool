---
title: Delete Entity With Ejb
nav: Delete Entity With Ejb
description: public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20090119071857/http://java2s.com:80/Code/Java/EJB3/DeleteEntityWithEjb.htm
---
Delete Entity With Ejb

```java title=Example.java
File: EmployeeService.java
import java.util.Collection;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;
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
    em.persist(emp);
    emp = findEmployee(id);
    System.out.println(emp);
    em.flush();
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
  }
}
File: EmployeeServiceLocal.java
import java.util.Collection;
import javax.ejb.Local;
@Local
public interface EmployeeServiceLocal {
    public void doAction();
    public Employee createEmployee(int id, String name, long salary, byte[] pic) ;
    public void removeEmployee(int id);
    public Employee raiseEmployeeSalary(int id, long raise) ;
    public Employee findEmployee(int id);
    public Collection<Employee> findAllEmployees() ;
}
File: EmployeeServiceRemote.java
import java.util.Collection;
import javax.ejb.Remote;
@Remote
public interface EmployeeServiceRemote{
  public void doAction();
  public Employee createEmployee(int id, String name, long salary, byte[] pic) ;
  public void removeEmployee(int id);
  public Employee raiseEmployeeSalary(int id, long raise) ;
  public Employee findEmployee(int id);
  public Collection<Employee> findAllEmployees() ;
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
    service.createEmployee(159, "AAA", 45000, "asdf".getBytes());
    Employee emp = service.findEmployee(158);
    System.out.println(emp);
    service.removeEmployee(158);
    emp = service.findEmployee(158);
    System.out.println(emp);
  }
}
```

EJB-DeleteEntityWithEjb.zip( 4,489 k)
