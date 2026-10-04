---
title: Hard Code Constant In SQL
nav: Hard Code Constant In SQL
description: <!-- Configure a built-in transaction manager. If you're using an
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20100212030048/http://java2s.com/Code/Java/J2EE/HardCodeConstantInSQL.htm
---
Hard Code Constant In SQL

```java title=Example.java
File: Account.java
public class Account {
  private int id;
  private String firstName;
  private String lastName;
  private String emailAddress;
  public int getId() {
    return id;
  }
  public void setId(int id) {
    this.id = id;
  }
  public String getFirstName() {
    return firstName;
  }
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }
  public String getLastName() {
    return lastName;
  }
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }
  public String getEmailAddress() {
    return emailAddress;
  }
  public void setEmailAddress(String emailAddress) {
    this.emailAddress = emailAddress;
  }
}
File: Account.xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE sqlMap
    PUBLIC "-//ibatis.apache.org//DTD SQL Map 2.0//EN"
    "http://ibatis.apache.org/dtd/sql-map-2.dtd">
<sqlMap namespace="Account">
  <typeAlias alias="Account" type="Account"/>
  <resultMap id="AccountResult" class="Account">
    <result property="id" column="ACC_ID"/>
    <result property="firstName" column="ACC_FIRST_NAME"/>
    <result property="lastName" column="ACC_LAST_NAME"/>
    <result property="emailAddress" column="ACC_EMAIL"/>
  </resultMap>
  <select id="getByLike" resultClass="Account">
      select ACC_ID as id,
      ACC_FIRST_NAME as firstName,
      'ACC_LAST_NAME' as lastName,
      ACC_EMAIL as emailAddress
      from ACCOUNT
  where ACC_EMAIL like '%$value$%'
  </select>
  <!-- Insert example, using the Account parameter class -->
  <insert id="insertAccount" parameterClass="Account">
    insert into ACCOUNT (
      ACC_ID,
      ACC_FIRST_NAME,
      ACC_LAST_NAME,
      ACC_EMAIL
    )values (
      #id#, #firstName#, #lastName#, #emailAddress#
    )
  </insert>
</sqlMap>
File: SqlMapConfig.xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE sqlMapConfig
    PUBLIC "-//ibatis.apache.org//DTD SQL Map Config 2.0//EN"
    "http://ibatis.apache.org/dtd/sql-map-config-2.dtd">
<sqlMapConfig>
  <!-- Configure a built-in transaction manager.  If you're using an
       app server, you probably want to use its transaction manager
       and a managed datasource -->
  <transactionManager type="JDBC" commitRequired="false">
    <dataSource type="SIMPLE">
      <property name="JDBC.Driver" value="org.hsqldb.jdbcDriver"/>
      <property name="JDBC.ConnectionURL" value="jdbc:hsqldb:data/tutorial"/>
      <property name="JDBC.Username" value="sa"/>
      <property name="JDBC.Password" value=""/>
    </dataSource>
  </transactionManager>
  <!-- List the SQL Map XML files. They can be loaded from the
       classpath, as they are here (com.domain.data...) -->
  <sqlMap resource="Account.xml"/>
  <!-- List more here...
  <sqlMap resource="com/mydomain/data/Order.xml"/>
  <sqlMap resource="com/mydomain/data/Documents.xml"/>
  -->
</sqlMapConfig>
File: Main.java
import java.util.List;
import com.ibatis.sqlmap.client.SqlMapClient;
public class Main {
  public static void main(String[] a) throws Exception {
    Util util = new Util();
    util
        .executeSQLCommand("create table ACCOUNT(ACC_ID int, ACC_FIRST_NAME varchar,ACC_LAST_NAME varchar,ACC_EMAIL varchar);");
    util.executeSQLCommand("create table Message(Message_ID int, content varchar);");
    SqlMapClient sqlMapper = util.getSqlMapClient();
    Account account = new Account();
    account.setId(1);
    account.setEmailAddress("e");
    account.setFirstName("first");
    account.setLastName("last");
    sqlMapper.insert("insertAccount", account);
    util.checkData("select * from account");
    List list = sqlMapper.queryForList("getByLike", "e");
    System.out.println(((Account)list.get(0)).getLastName());
  }
}
File: Util.java
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import com.ibatis.common.resources.Resources;
import com.ibatis.sqlmap.client.SqlMapClient;
import com.ibatis.sqlmap.client.SqlMapClientBuilder;
public class Util {
  Statement st;
  public Util() throws Exception{
    // Load the JDBC driver.
    Class.forName("org.hsqldb.jdbcDriver");
    System.out.println("Driver Loaded.");
    // Establish the connection to the database.
    String url = "jdbc:hsqldb:data/tutorial";
    Connection conn = DriverManager.getConnection(url, "sa", "");
    System.out.println("Got Connection.");
    st = conn.createStatement();
  }
  public SqlMapClient getSqlMapClient() throws Exception{
    Reader reader = Resources.getResourceAsReader("SqlMapConfig.xml");
    SqlMapClient sqlMapper = SqlMapClientBuilder.buildSqlMapClient(reader);
    reader.close();
    return sqlMapper;
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
```

iBatis-HardCodeConstantInSQL.zip( 941 k)
1.  iBatis Development Environment Setup
2.  Define Result Class
3.  Delete By ID
4.  Get List Of Objects
5.  Get Object From iBatis
6.  Insert Into Database
7.  iBatis JPetStore 5.0
8.  Set Cache Mode
9.  String Parameter
10.  Update Object
11.  Use Map To Pass In Two String Parameter
12.  Use Order By clause
13.  User Object As Parameter
14.  Use Like in where clause
