---
title: EJB Based Web Services
nav: EJB Based Web Services
description: java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20090225211829/http://www.java2s.com:80/Code/Java/EJB3/EJBBasedWebServices.htm
---
EJB Based Web Services

```java title=Example.java
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
File: Main.java
import java.util.Date;
import javax.naming.InitialContext;
import bean.EmployeeServiceRemote;
public class Main {
  public static void main(String[] a) throws Exception {
    EmployeeServiceRemote service = null;
    // Context compEnv = (Context) new InitialContext().lookup("java:comp/env");
    // service = (HelloService)new InitialContext().lookup("java:comp/env/ejb/HelloService");
    service = (EmployeeServiceRemote) new InitialContext().lookup("EmployeeBean/remote");
    //service.doAction();
  }
}
File: Employee.java
package bean;
import javax.persistence.Entity;
import javax.persistence.EntityListeners;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.PostRemove;
@Entity
public class Employee implements java.io.Serializable {
  private int id;
  private String firstName;
  private String lastName;
  @Id
  @GeneratedValue
  public int getId() {
    return id;
  }
  @PostRemove
  public void postRemove()
  {
     System.out.println("@PostRemove");
  }
  public void setId(int id) {
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
}
File: EmployeeBean.java
package bean;
import javax.ejb.Stateless;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebResult;
import javax.jws.WebService;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
@WebService(name = "MyEmployee", serviceName = "MyEmployeeService")
//@Stateless
public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
  @PersistenceContext(unitName = "EmployeeService")
  private EntityManager entityManager;
  public EmployeeBean() {
  }
  @WebMethod
  public void createEmployee(@WebParam(name = "employee")Employee c) {
    entityManager.persist(c);
  }
  @WebMethod
  @WebResult(name = "Employee")
  public Employee findEmployee(@WebParam(name = "ID")int pKey) {
    return entityManager.find(Employee.class, pKey);
  }
}
File: EmployeeServiceLocal.java
package bean;
import javax.ejb.Local;
@Local
public interface EmployeeServiceLocal {
  public void createEmployee(Employee c);
  public Employee findEmployee(int id);
}
File: EmployeeServiceRemote.java
package bean;
import javax.ejb.Remote;
@Remote
public interface EmployeeServiceRemote {
  public void createEmployee(Employee c);
  public Employee findEmployee(int id);
}
```

EJB-EJBBasedWebServices.zip( 4,489 k)
1.  EJB With Web Method
2.  Turn Ejb To Web Service
3.  Web Method With Return Type And Parameters
4.  EJB Tutorial from JBoss: turn EJB to web service
