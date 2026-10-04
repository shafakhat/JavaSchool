---
title: Call Stored Procedure In Oracle And Pass In Out Parameters
nav: Call Stored Procedure In O...
description: CallableStatement cs = conn.prepareCall(proc3StoredProcedure);
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20070113165141/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/CallStoredProcedureInOracleAndPassInOutParameters.htm
---
Call Stored Procedure In Oracle And Pass In Out Parameters

```java title=Example.java
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
public class Main {
  public static void main(String[] args) throws Exception {
    Connection conn = getOracleConnection();
    // Step-2: identify the stored procedure
    String proc3StoredProcedure = "{ call proc3(?, ?, ?) }";
    // Step-3: prepare the callable statement
    CallableStatement cs = conn.prepareCall(proc3StoredProcedure);
    // Step-4: set input parameters ...
    // first input argument
    cs.setString(1, "abcd");
    // third input argument
    cs.setInt(3, 10);
    // Step-5: register output parameters ...
    cs.registerOutParameter(2, java.sql.Types.VARCHAR);
    cs.registerOutParameter(3, java.sql.Types.INTEGER);
    // Step-6: execute the stored procedures: proc3
    cs.execute();
    // Step-7: extract the output parameters
    // get parameter 2 as output
    String param2 = cs.getString(2);
    // get parameter 3 as output
    int param3 = cs.getInt(3);
    System.out.println("param2=" + param2);
    System.out.println("param3=" + param3);
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

Download: CallStoresProcedureInOracleAndPassInOutParameters.zip ( 3,849 K )
---
Related examples in the same category
2. Stored procedure utilities
