---
title: Container Managed Transaction
nav: Container Managed Transact...
description: public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20100212193130/http://java2s.com/Code/Java/EJB3/ContainerManagedTransactionRequired.htm
---
Container Managed Transaction: Required

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
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
@Stateless
public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
  @PersistenceContext(unitName = "EmployeeService")
  private EntityManager em;
  public EmployeeBean() {
  }
  @TransactionAttribute(TransactionAttributeType.REQUIRED)
  public void doAction() {
    Employee emp = new Employee();
    emp.setFirstName("first");
    em.persist(emp);
  }
  public <T> T mergeEntity(T entity) {
    return em.merge(entity);
  }
  public <T> T persistEntity(T entity) {
    em.persist(entity);
    return entity;
  }
  public <T> T refreshEntity(T entity) {
    em.refresh(entity);
    return entity;
  }
  public void removeEntity(Object entity) {
    em.remove(em.merge(entity));
  }
}
File: EmployeeServiceLocal.java
import javax.ejb.Local;
@Local
public interface EmployeeServiceLocal {
  public void doAction();
  <T> T mergeEntity(T entity);
  <T> T persistEntity(T entity);
  <T> T refreshEntity(T entity);
  void removeEntity(Object entity);
}
File: EmployeeServiceRemote.java
import javax.ejb.Remote;
@Remote
public interface EmployeeServiceRemote {
  public void doAction();
  <T> T mergeEntity(T entity);
  <T> T persistEntity(T entity);
  <T> T refreshEntity(T entity);
  void removeEntity(Object entity);
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
    // service = (HelloService)new
    // InitialContext().lookup("java:comp/env/ejb/HelloService");
    service = (EmployeeServiceRemote) new InitialContext().lookup("EmployeeBean/remote");
    service.doAction();
  }
}
```

EJB-MarkContainerManagedTransactionWithRequired.zip( 4,489 k)
1.  Container Managed Transaction
2.  Container Managed Transaction: TransactionAttributeType.SUPPORTS
3.  Transaction Management Type: BEAN
4.  Transaction Attribute Type: SUPPORTS
5.  Transaction Attribute Type: REQUIRES_NEW
6.  Use User Transaction In Client Side
7.  Inject Transaction As Resource
8.  Mark Stateful Session Bean As Transaction Attribute Type: REQUIRES_NEW
