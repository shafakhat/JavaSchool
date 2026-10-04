---
title: boolean java.sql.DriverPropertyInfo.required (Is property value required?)
nav: boolean java.sql.DriverPro...
description: boolean java.sql.DriverPropertyInfo.required (Is property value required?)
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20100213225613/http://java2s.com/Code/Java/Database-SQL-JDBC/booleanjavasqlDriverPropertyInforequiredIspropertyvaluerequired.htm
---
boolean java.sql.DriverPropertyInfo.required (Is property value required?)

```java title=Example.java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.DriverPropertyInfo;
public class Main {
  public static void main(String[] argv) throws Exception {
    String driverName = "org.gjt.mm.mysql.Driver";
    Class.forName(driverName);
    String url = "jdbc:mysql://a/b";
    Driver driver = DriverManager.getDriver(url);
    DriverPropertyInfo[] info = driver.getPropertyInfo(url, null);
    for (int i = 0; i < info.length; i++) {
      String name = info[i].name;
      boolean isRequired = info[i].required;
      String value = info[i].value;
      String desc = info[i].description;
      String[] choices = info[i].choices;
    }
  }
}
```

1.  Connect to more than one database
---  ---
2.  Verify database setup
3.  Debug Database connection
4.  Create Connection With Properties
5.  Set save point
6.  JDBC Simple Connection
7.  Load some drivers
8.  Encapsulate the Connection-related operations that every JDBC program seems to use
9.  Test of loading a driver and connecting to a database
10.  Load MySQL JDBC Driver
11.  Oracle JDBC Driver load
12.  Oracle JDBC Driver load test: NewInstance
13.  Test Register Oracle JDBC Driver
14.  Install Oracle Driver and Execute Resultset
15.  Test Thin Net8 App
16.  Specify a CharSet when connecting to a DBMS
17.  Listing All Available Parameters for Creating a JDBC Connection
18.  String java.sql.DriverPropertyInfo.name (Get name of property)
19.  String java.sql.DriverPropertyInfo.value (Get current value)
20.  String java.sql.DriverPropertyInfo.description (Get description of property)
21.  String[] java.sql.DriverPropertyInfo.choices (Get possible choices for property; if null, value can be any string)
22.  Determining If a Database Supports Transactions
23.  Committing and Rolling Back Updates to a Database
24.  Disable auto commit mode in JDBC
25.  Print warnings on a Connection to STDERR.
26.  Print warnings on a Connection to a specified PrintWriter.
