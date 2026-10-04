---
title: Get parent logger
nav: Get parent logger
description: Driver driver = DriverManager.getDriver("jdbc:derby://localhost:1527");
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/20130721105551/http://www.java2s.com:80/Code/Java/JDK-7/Getparentlogger.htm
---
```java title=Example.java
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
public class Test {
  public static void main(String[] args) throws Exception {
    Connection conn = DriverManager
        .getConnection("...", "username", "password");
    Driver driver = DriverManager.getDriver("jdbc:derby://localhost:1527");
    System.out.println("Parent Logger" + driver.getParentLogger());
  }
}
```

1.  Using the RowSetFactory class
---  ---
2.  Java 7 database enhancements:Get auto generated key
3.  Retrieving pseudo-columns
4.  Controlling the type value of the OUT parameter
