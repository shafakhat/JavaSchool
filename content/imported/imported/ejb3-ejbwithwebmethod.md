---
title: EJB With Web Method
nav: EJB With Web Method
description: java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20090225212611/http://www.java2s.com:80/Code/Java/EJB3/EJBWithWebMethod.htm
---
EJB With Web Method

```java title=Example.java
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
File: Main.java
import javax.naming.InitialContext;
import bean.EmployeeServiceRemote;
public class Main {
  public static void main(String[] a) throws Exception {
    EmployeeServiceRemote service = null;
    // Context compEnv = (Context) new InitialContext().lookup("java:comp/env");
    // service = (HelloService)new
    // InitialContext().lookup("java:comp/env/ejb/HelloService");
    service = (EmployeeServiceRemote) new InitialContext().lookup("EmployeeBean/remote");
    service.doAction();
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
import javax.jws.WebService;
@Stateless(name = "EmployeeBeanEJB")
@WebService(serviceName = "EmployeeBeanWebService",
            targetNamespace = "http://www.java2s.com/ejb3/credit")
public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
  public EmployeeBean() {
  }
  @WebMethod(operationName = "CreditCheck")
  public boolean validateCC(String cc) {
    return true;
  }
  public void doAction() {
    System.out.println("Processing...");
  }
}
File: EmployeeServiceLocal.java
package bean;
import javax.ejb.Local;
import javax.ejb.Remote;
@Local
public interface EmployeeServiceLocal{
  public void doAction();
}
File: EmployeeServiceRemote.java
package bean;
import javax.ejb.Stateless;
import javax.jws.WebService;
public interface EmployeeServiceRemote {
  public void doAction();
}
```

EJB-EJBWithWebMethod.zip( 4,488 k)
1.  Turn Ejb To Web Service
2.  Web Method With Return Type And Parameters
3.  EJB Tutorial from JBoss: turn EJB to web service
4.  EJB Based Web Services
