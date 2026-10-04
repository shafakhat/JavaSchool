---
title: Context Injection
nav: Context Injection
description: public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20090421175427/http://www.java2s.com:80/Code/Java/EJB3/ContextInjection.htm
---
Context Injection

```java title=Example.java
File: AnotherBean.java
import javax.ejb.Stateless;
@Stateless
public class AnotherBean implements AnotherBeanLocal {
  public void doAnother(){
    System.out.println("from another bean");
  }
}
File: AnotherBeanLocal.java
public interface AnotherBeanLocal {
  public void doAnother();
}
File: Employee.java
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
import javax.annotation.Resource;
import javax.ejb.EJB;
import javax.ejb.SessionContext;
import javax.ejb.Stateless;
@Stateless
@EJB(name = "audit", beanInterface = AnotherBeanLocal.class)
public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
  @Resource SessionContext context;
  public EmployeeBean() {
  }
  public void doAction() {
    System.out.println("doAction");
    AnotherBeanLocal a = (AnotherBeanLocal) context.lookup("audit");;
    a.doAnother();
  }
}
File: EmployeeServiceLocal.java
import java.util.Map;
import javax.ejb.Local;
@Local
public interface EmployeeServiceLocal {
  public void doAction();
}
File: EmployeeServiceRemote.java
import javax.ejb.Remote;
@Remote
public interface EmployeeServiceRemote {
  public void doAction();
}
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
File: Main.java
import javax.ejb.EJB;
import javax.naming.InitialContext;
public class Main {
  public static void main(String[] a) throws Exception {
    EmployeeServiceRemote service = null;
    // Context compEnv = (Context) new InitialContext().lookup("java:comp/env");
    // service = (HelloService)new InitialContext().lookup("java:comp/env/ejb/HelloService");
    service = (EmployeeServiceRemote) new InitialContext().lookup("EmployeeBean/remote");
    service.doAction();
  }
}
```

EJB-ContextInjection.zip( 4,489 k)
1.  Initialize javax.naming.InitialContext with System.getProperties
2.  Use Context To Lookup Another Ejb
3.  Explicityly Set Context with JNDI
