---
title: Retrieving pseudo-columns
nav: Retrieving pseudo-columns
description: "jdbc:derby://localhost:1527/contact", "userName", "password");
section: Imported - java2s Archive
order: 1123
source: https://web.archive.org/web/20130721105358/http://www.java2s.com:80/Code/Java/JDK-7/Retrievingpseudocolumns.htm
---
```java title=Example.java
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
public class Test {
  public static void main(String[] args) throws Exception {
    Connection con = DriverManager.getConnection(
        "jdbc:derby://localhost:1527/contact", "userName", "password");
    DatabaseMetaData metaData = con.getMetaData();
    ResultSet resultSet = metaData.getPseudoColumns("", "schemaName",
        "tableName", "");
    while (resultSet.next()) {
      System.out.println(resultSet.getString("TABLE_SCHEM ") + " - "
          + resultSet.getString("COLUMN_NAME "));
    }
  }
}
```

1.  Using the RowSetFactory class
---  ---
2.  Java 7 database enhancements:Get auto generated key
3.  Controlling the type value of the OUT parameter
4.  Get parent logger
