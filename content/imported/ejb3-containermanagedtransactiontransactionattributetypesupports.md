---
title: Container Managed Transaction
nav: Container Managed Transact...
description: Container Managed Transaction: TransactionAttributeType.SUPPORTS
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20090504172407/http://www.java2s.com:80/Code/Java/EJB3/ContainerManagedTransactionTransactionAttributeTypeSUPPORTS.htm
---
Container Managed Transaction: TransactionAttributeType.SUPPORTS

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
File: EmployeeBean.java
import javax.ejb.Stateful;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
@Stateful
public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
  public EmployeeBean() {
  }
  @TransactionAttribute(TransactionAttributeType.SUPPORTS)
  public void doAction() {
     System.out.println("Processing...");
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

EJB-ContainerManagedTransaction.zip( 4,488 k)
1.  Container Managed Transaction
2.  Transaction Management Type: BEAN
3.  Transaction Attribute Type: SUPPORTS
4.  Transaction Attribute Type: REQUIRES_NEW
5.  Use User Transaction In Client Side
6.  Inject Transaction As Resource
7.  Mark Statful Session Bean As Transaction Attribute Type: REQUIRES_NEW
8.  Container Managed Transaction: Required
