---
title: Inheritance Result Mapping
nav: Inheritance Result Mapping
description: return "ContractProfessor id: " + getId() + " name: " + getName();
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20090422105832/http://www.java2s.com:80/Code/Java/JPA/InheritanceResultMapping.htm
---
```java title=Example.java
File: ContractProfessor.java
import javax.persistence.Column;
import javax.persistence.Entity;
@Entity
public class ContractProfessor extends Professor {
  @Column(name = "DAILY_RATE")
  private int dailyRate;
  private int term;
  public int getDailyRate() {
    return dailyRate;
  }
  public void setDailyRate(int dailyRate) {
    this.dailyRate = dailyRate;
  }
  public int getTerm() {
    return term;
  }
  public void setTerm(int term) {
    this.term = term;
  }
  public String toString() {
    return "ContractProfessor id: " + getId() + " name: " + getName();
  }
}
File: Professor.java
import java.util.Date;
import javax.persistence.Column;
import javax.persistence.DiscriminatorColumn;
import javax.persistence.Entity;
import javax.persistence.EntityResult;
import javax.persistence.FieldResult;
import javax.persistence.Id;
import javax.persistence.Inheritance;
import javax.persistence.SqlResultSetMapping;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
@Entity
@Table(name="EMPLOYEE")
@Inheritance
@DiscriminatorColumn(name="EMP_TYPE")
@SqlResultSetMapping(
    name="ProfessorStageMapping",
    entities=
        @EntityResult(
            entityClass=Professor.class,
            discriminatorColumn="TYPE",
            fields={
                @FieldResult(name="startDate", column="START_DATE"),
                @FieldResult(name="dailyRate", column="DAILY_RATE"),
                @FieldResult(name="hourlyRate", column="HOURLY_RATE")
            }
        )
)
public abstract class Professor {
    @Id private int id;
    private String name;
    @Temporal(TemporalType.DATE)
    @Column(name="START_DATE")
    private Date startDate;
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
    public Date getStartDate() {
        return startDate;
    }
    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }
    public String toString() {
        return "Professor id: " + getId() + " name: " + getName();
    }
}
File: ProfessorService.java
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.Query;
public class ProfessorService {
  protected EntityManager em;
  public ProfessorService(EntityManager em) {
    this.em = em;
  }
  public List findAllProfessors() {
    Query query = em.createNativeQuery("SELECT id, name, start_date, daily_rate, term "
        + " FROM employee", "ProfessorStageMapping");
    return query.getResultList();
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

JPA-InheritanceResultMapping.zip( 5,334 k)
1.  Using Entity Result
2.  Sql Resultset Mapping With Alias
3.  SQL Resultset Mapping: Two Entities
4.  SQL Resultset Mapping: One Entity
5.  Sql Resultset Mapping: Column Result
6.  Inheritance Result Mapping Two Subclasses
7.  Cast Result List To Generic Collection
