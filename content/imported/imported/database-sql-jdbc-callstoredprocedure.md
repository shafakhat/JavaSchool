---
title: Call stored procedure
nav: Call stored procedure
description: 1. Call Stored Procedure In Oracle And Pass In Out Parameters
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20090502104857/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/Callstoredprocedure.htm
---
```java title=Example.java
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.Types;
public class Main {
  public static void main(String[] argv) throws Exception {
    Connection conn = null;
    String query = "begin proc(?,?,?); end;";
    CallableStatement cs = conn.prepareCall(query);
    cs.setString(1, "string parameter");
    cs.setInt(2, 1);
    cs.registerOutParameter(2, Types.INTEGER);
    cs.registerOutParameter(3, Types.INTEGER);
    cs.execute();
    int parm2 = cs.getInt(2); // get the result from OUTPUT #2
    int parm3 = cs.getInt(3); // get the result from OUTPUT #3
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
9.  Call a procedure with one OUT parameter
10.  Call a procedure with one IN/OUT parameter
11.  Calling a Function in a Database: call functions with IN, OUT, and IN/OUT parameters.
12.  Call a function with one IN parameter; the function returns a VARCHAR
13.  Call a function with one OUT parameter; the function returns a VARCHAR
14.  Creating a Stored Procedure or Function in an Oracle Database
15.  Call a function with one IN/OUT parameter; the function returns a VARCHAR
16.  Create procedure myprocin with an IN parameter named x.
17.  Create procedure myprocout with an OUT parameter named x
18.  Create procedure myprocinout with an IN/OUT parameter named x; x is an IN parameter and an OUT parameter
19.  Create a function named myfunc which returns a VARCHAR value; the function has no parameter
20.  Create a function named myfuncin which returns a VARCHAR value; the function has an IN parameter named x
21.  Create a function named myfuncout which returns a VARCHAR value;
22.  Create a function named myfuncinout that returns a VARCHAR value
23.  Calling a Stored Procedure in a Database with no parameters
24.  Getting the Stored Procedure Names in a Database: retrieves the names of all stored procedures in a database.
25.  Stored procedure with Input/Output parms and a ResultSet
