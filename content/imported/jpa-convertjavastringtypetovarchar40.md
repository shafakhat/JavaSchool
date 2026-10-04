---
title: Convert Java String Type To Varchar 40
nav: Convert Java String Type T...
description: Connection conn = DriverManager.getConnection(url, "sa", "");
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20090515021134/http://www.java2s.com:80/Code/Java/JPA/ConvertJavaStringTypeToVarchar40.htm
---
Convert Java String Type To Varchar 40

```java title=Example.java
File: Professor.java
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
@Entity
public class Professor {
    @Id
    @Column(columnDefinition="VARCHAR(40)")
    private String name;
    @Column(precision=8, scale=2)
    private float hourlyRate;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public float getHourlyRate() {
      return hourlyRate;
    }
    public void setHourlyRate(float hourlyRate) {
      this.hourlyRate = hourlyRate;
    }
}
File: ProfessorService.java
import java.util.Collection;
import javax.persistence.EntityManager;
import javax.persistence.Query;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public Collection<Professor> findAllProfessors() {
    Query query = em.createQuery("SELECT e FROM Professor e");
    return (Collection<Professor>) query.getResultList();
  }
}
File: JPAUtil.java
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
public class JPAUtil {
  Statement st;
  public JPAUtil() throws Exception{
    Class.forName("org.hsqldb.jdbcDriver");
    System.out.println("Driver Loaded.");
    String url = "jdbc:hsqldb:data/tutorial";
    Connection conn = DriverManager.getConnection(url, "sa", "");
    System.out.println("Got Connection.");
    st = conn.createStatement();
  }
  public void executeSQLCommand(String sql) throws Exception {
    st.executeUpdate(sql);
  }
  public void checkData(String sql) throws Exception {
    ResultSet rs = st.executeQuery(sql);
    ResultSetMetaData metadata = rs.getMetaData();
    for (int i = 0; i < metadata.getColumnCount(); i++) {
      System.out.print("\t"+ metadata.getColumnLabel(i + 1));
    }
    System.out.println("\n----------------------------------");
    while (rs.next()) {
      for (int i = 0; i < metadata.getColumnCount(); i++) {
        Object value = rs.getObject(i + 1);
        if (value == null) {
          System.out.print("\t       ");
        } else {
          System.out.print("\t"+value.toString().trim());
        }
      }
      System.out.println("");
    }
  }
}
File: Main.java
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
public class Main {
  public static void main(String[] a) throws Exception {
    JPAUtil util = new JPAUtil();
    EntityManagerFactory emf = Persistence.createEntityManagerFactory("ProfessorService");
    EntityManager em = emf.createEntityManager();
    ProfessorService service = new ProfessorService(em);
    em.getTransaction().begin();
    service.findAllProfessors();
    util.checkData("select * from Professor");
    em.getTransaction().commit();
    em.close();
    emf.close();
  }
}
File: persistence.xml
<persistence xmlns="http://java.sun.com/xml/ns/persistence"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://java.sun.com/xml/ns/persistence http://java.sun.com/xml/ns/persistence/persistence" version="1.0">
  <persistence-unit name="JPAService" transaction-type="RESOURCE_LOCAL">
    <properties>
      <property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
      <property name="hibernate.hbm2ddl.auto" value="update"/>
      <property name="hibernate.connection.driver_class" value="org.hsqldb.jdbcDriver"/>
      <property name="hibernate.connection.username" value="sa"/>
      <property name="hibernate.connection.password" value=""/>
      <property name="hibernate.connection.url" value="jdbc:hsqldb:data/tutorial"/>
    </properties>
  </persistence-unit>
</persistence>
```

JPA-ConvertJavaStringTypeToVarchar40.zip( 5,333 k)
1.  Set Column Definition
2.  Set Column Name
3.  Set Column Length
4.  Set Column Definition For Many To One Mapping
5.  Nullable Column
6.  Not Updatable Column
7.  Mark Column Precision And Scale
