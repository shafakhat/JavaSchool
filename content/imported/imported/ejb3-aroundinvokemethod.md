---
title: Around InvokeMethod
nav: Around InvokeMethod
description: public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20090204180036/http://www.java2s.com:80/Code/Java/EJB3/AroundInvokeMethod.htm
---
Around InvokeMethod

```java title=Example.java
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
File: EmployeeService.java
import javax.ejb.Stateless;
import javax.interceptor.Interceptors;
@Stateless
public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
  public EmployeeService() {
  }
  @Interceptors(Profiler.class)
  public void doAction() {
    System.out.println("do Action");
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
File: Profiler.java
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
public class Profiler {
  @AroundInvoke
  public Object profile(InvocationContext invocation) throws Exception {
    long startTime = System.currentTimeMillis();
    try {
      return invocation.proceed();
    } finally {
      long endTime = System.currentTimeMillis() - startTime;
      System.out.println("Method " + invocation.getMethod() + " took " + endTime + " (ms)");
    }
  }
}
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
File: Main.java
import java.util.Date;
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
```

EJB-AroundInvokeMethod.zip( 4,489 k)
1.  Get Ejb Info From InvocationContext
2.  Get Set Parameters In InvocationContext
3.  Use Interceptors To Check Permission
4.  EJB Tutorial from JBoss: Callback Listener
5.  EJB Tutorial from JBoss: Interceptor
6.  Mark Interceptors For A Remote Method
7.  annotation override interceptor
8.  interceptor stateless
