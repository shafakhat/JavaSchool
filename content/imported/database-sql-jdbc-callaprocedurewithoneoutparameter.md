---
title: Call a procedure with one OUT parameter
nav: Call a procedure with one ...
description: Connection connection = DriverManager.getConnection(url, username, password);
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20090502013620/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/CallaprocedurewithoneOUTparameter.htm
---
```java title=Example.java
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Types;
public class Main {
  public static void main(String[] argv) throws Exception {
    String driverName = "com.jnetdirect.jsql.JSQLDriver";
    Class.forName(driverName);
    String serverName = "127.0.0.1";
    String portNumber = "1433";
    String mydatabase = serverName + ":" + portNumber;
    String url = "jdbc:JSQLConnect://" + mydatabase;
    String username = "username";
    String password = "password";
    Connection connection = DriverManager.getConnection(url, username, password);
    CallableStatement cs = connection.prepareCall("{call myprocout(?)}");
    // Register the type of the OUT parameter
    cs.registerOutParameter(1, Types.VARCHAR);
    cs.execute();
    String outParam = cs.getString(1);     // OUT parameter
    System.out.println(outParam);
  }
}
```

1.  Call Stored Procedure In Oracle And Pass In Out Parameters
---  ---
2.  Get Stored Procedure Name And Type
3.  Stored procedure utilities
4.  Get Stored Procedure Signature
5.  Connect to database and call stored procedure
6.  Call a stored procedure with no parameters and return value.
7.  Call Stored Procedure In MySql
8.  Call a procedure with one IN parameter
9.  Call a procedure with one IN/OUT parameter
10.  Calling a Function in a Database: call functions with IN, OUT, and IN/OUT parameters.
11.  Call a function with one IN parameter; the function returns a VARCHAR
12.  Call a function with one OUT parameter; the function returns a VARCHAR
13.  Creating a Stored Procedure or Function in an Oracle Database
14.  Call a function with one IN/OUT parameter; the function returns a VARCHAR
15.  Create procedure myprocin with an IN parameter named x.
16.  Create procedure myprocout with an OUT parameter named x
17.  Create procedure myprocinout with an IN/OUT parameter named x; x is an IN parameter and an OUT parameter
18.  Create a function named myfunc which returns a VARCHAR value; the function has no parameter
19.  Create a function named myfuncin which returns a VARCHAR value; the function has an IN parameter named x
20.  Create a function named myfuncout which returns a VARCHAR value;
21.  Create a function named myfuncinout that returns a VARCHAR value
22.  Calling a Stored Procedure in a Database with no parameters
23.  Getting the Stored Procedure Names in a Database: retrieves the names of all stored procedures in a database.
24.  Call stored procedure
25.  Stored procedure with Input/Output parms and a ResultSet
