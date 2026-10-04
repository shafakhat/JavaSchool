---
title: Another Method To Check Table Existance
nav: Another Method To Check Ta...
description: st.executeUpdate("create table survey (id int,name varchar(30));");
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20061018125141/http://www.java2s.com/Code/Java/Database-SQL-JDBC/AnotherMethodToCheckTableExistance.htm
---
```java title=Example.java
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class Main {
  public static void main(String[] args) throws Exception {
    Connection conn = getMySqlConnection();
    System.out.println("Got Connection.");
    Statement st = conn.createStatement();
    st.executeUpdate("drop table survey;");
    st.executeUpdate("create table survey (id int,name varchar(30));");
    st.executeUpdate("insert into survey (id,name ) values (1,'nameValue')");
    String tableName = "survey";
    String query = "select count(*) from  " + tableName;
    Statement stmt = null;
    ResultSet rs = null;
    try {
      stmt = conn.createStatement();
      rs = stmt.executeQuery(query);
      System.out.println("Exist");;
    }
    catch (Exception e ) {
      // table does not exist or some other problem
      //e.printStackTrace();
      System.out.println("Not Exist");
    }
    st.close();
    conn.close();
  }
  private static Connection getHSQLConnection() throws Exception {
    Class.forName("org.hsqldb.jdbcDriver");
    System.out.println("Driver Loaded.");
    String url = "jdbc:hsqldb:data/tutorial";
    return DriverManager.getConnection(url, "sa", "");
  }
  public static Connection getMySqlConnection() throws Exception {
    String driver = "org.gjt.mm.mysql.Driver";
    String url = "jdbc:mysql://localhost/demo2s";
    String username = "oost";
    String password = "oost";
    Class.forName(driver);
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
  public static Connection getOracleConnection() throws Exception {
    String driver = "oracle.jdbc.driver.OracleDriver";
    String url = "jdbc:oracle:thin:@localhost:1521:caspian";
    String username = "mp";
    String password = "mp2";
    Class.forName(driver); // load Oracle driver
    Connection conn = DriverManager.getConnection(url, username, password);
    return conn;
  }
}
```

Download: AnotherMethodToCheckTableExistance.zip ( 2,516 K )
---
Related examples in the same category
5. Database metadata: data type
6. List the Tables in an SQL database
7. Create table with primary key
8. Create table with foreign key
9. Create data table 3
10. Create supplier table
11. Create data table: reference
12. Create data table 2
13. Create data type and data table
