---
title: Ejb With Generic Method
nav: Ejb With Generic Method
description: public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20090129105626/http://www.java2s.com:80/Code/Java/EJB3/EjbWithGenericMethod.htm
---
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
import javax.annotation.Resource;
import javax.ejb.Stateful;
import javax.ejb.TransactionManagement;
import javax.ejb.TransactionManagementType;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.PersistenceContextType;
import javax.transaction.UserTransaction;
@Stateful
@TransactionManagement(TransactionManagementType.BEAN)
public class EmployeeBean implements EmployeeServiceLocal, EmployeeServiceRemote {
  @PersistenceContext(unitName = "EmployeeService", type = PersistenceContextType.EXTENDED)
  private EntityManager em;
  @Resource
  private UserTransaction ut;
  public EmployeeBean() {
  }
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
  public void beginTrans()
    throws Exception {
    ut.begin();
  }
  public void commitTrans()
    throws Exception {
    ut.commit();
  }
  public void rollbackTrans()
    throws Exception {
    ut.rollback();
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
  void beginTrans() throws Exception;
  void commitTrans() throws Exception;
  void rollbackTrans() throws Exception;
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
  void beginTrans() throws Exception;
  void commitTrans() throws Exception;
  void rollbackTrans() throws Exception;
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
    service.beginTrans();
    service.doAction();
    service.commitTrans();
  }
}
```

EJB-EjbWithGenericMethod.zip( 4,489 k)
1.  Stateful Session Bean Lifecycle: PrePassivate
2.  Stateful Session Bean Lifecycle: PreDestroy
3.  Stateful Session Bean Lifecycle: PostConstruct
4.  Stateful Session Bean Lifecycle: PostActivate
5.  Stateful Session Bean And Shopping Cart
6.  Stateful Session Bean And Entity Manager
7.  Use Lifecycle Method To Manage Collection In Stateful Session Bean
8.  EJB Tutorial from JBoss: stateful session bean
9.  EJB Tutorial from JBoss: stateful session bean deployment descriptor
10.  Remove a Stateful Session Bean
11.  Remove Annotation
