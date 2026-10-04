---
title: Entity bean lifecycle
nav: Entity bean lifecycle
description: public class EmployeeService implements EmployeeServiceLocal, EmployeeServiceRemote {
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20090921025138/http://www.java2s.com:80/Code/Java/EJB3/EntitybeanlifecyclePostPersist.htm
---
Entity bean lifecycle: PostPersist

```java title=Example.java
File: EmployeeService.java
import java.util.List;
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
    Employee employee = new Employee();
    employee.setFirstName("E");
    employee.setLastName("E");
    em.persist(employee);
    em.flush();
    System.out.println("saved");
    List list = em.createQuery("FROM Employee p").getResultList();
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
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.PostPersist;
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
  @PostPersist
  public void postPersist()
  {
     System.out.println("@PostPersist");
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
File: persistence.xml
<persistence xmlns="http://java.sun.com/xml/ns/persistence"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://java.sun.com/xml/ns/persistence http://java.sun.com/xml/ns/persistence/persistence" version="1.0">
  <persistence-unit name="EmployeeService" > <!-- transaction-type="JTA" -->
        <jta-data-source>java:/DefaultDS</jta-data-source>
        <properties>
         <property name="hibernate.hbm2ddl.auto" value="create-drop"/>
        </properties>
<!--
    <properties>
      <property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
      <property name="hibernate.hbm2ddl.auto" value="update"/>
      <property name="hibernate.connection.driver_class" value="org.hsqldb.jdbcDriver"/>
      <property name="hibernate.connection.username" value="sa"/>
      <property name="hibernate.connection.password" value=""/>
      <property name="hibernate.connection.url" value="jdbc:hsqldb:data/tutorial"/>
    </properties>
-->
  </persistence-unit>
</persistence>
File: ejb-jar.xml
<?xml version="1.0" encoding="UTF-8"?>
<ejb-jar>
   <enterprise-beans>
   </enterprise-beans>
</ejb-jar>
```

EJB-UsingPostPersist.zip( 4,487 k)
1.  Entity bean lifecycle: PreUpdate
2.  Entity bean lifecycle: Post Update
3.  Entity bean lifecycle: PostRemove
4.  Entity bean lifecycle: PreRemove
5.  Entity bean lifecycle: PrePersist
6.  Entity bean lifecycle: PostLoad
