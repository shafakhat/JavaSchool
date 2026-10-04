---
title: boolean java.sql.Driver.jdbcCompliant()
nav: boolean java.sql.Driver.jd...
description: 8. Loading a JDBC Driver: call Class.forName() within the code
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20090813161524/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/booleanjavasqlDriverjdbcCompliant.htm
---
boolean java.sql.Driver.jdbcCompliant()

```java title=Example.java
import java.sql.Driver;
import java.sql.DriverManager;
import java.util.Collections;
import java.util.List;
public class Main {
  public static void main(String[] argv) throws Exception {
    List drivers = Collections.list(DriverManager.getDrivers());
    for (int i = 0; i < drivers.size(); i++) {
      Driver driver = (Driver) drivers.get(i);
      String name = driver.getClass().getName();
      System.out.println(name);
      int majorVersion = driver.getMajorVersion();
      System.out.println(majorVersion);
      int minorVersion = driver.getMinorVersion();
      System.out.println(minorVersion);
      boolean isJdbcCompliant = driver.jdbcCompliant();
      System.out.println(isJdbcCompliant);
    }
  }
}
```

1.  Get Driver Property Info
---  ---
2.  Get Driver Name
3.  int java.sql.Driver.getMajorVersion()
4.  int java.sql.Driver.getMinorVersion()
5.  Enumeration java.sql.DriverManager.getDrivers()
6.  Get Driver Version
7.  JDBC Driver Information
8.  Loading a JDBC Driver: call Class.forName() within the code
9.  Listing All Loaded JDBC Drivers and gets information about each one.
10.  DriverPropertyInfo[] java.sql.Driver.getPropertyInfo(String url, Properties info)
11.  Enable JDBC logging
