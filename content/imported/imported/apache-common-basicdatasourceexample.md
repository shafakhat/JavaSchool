---
title: Basic DataSource Example
nav: Basic DataSource Example
description: Imported from the java2s.com archive: Basic DataSource Example
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20061026235120/http://www.java2s.com/Code/Java/Apache-Common/BasicDataSourceExample.htm
---
Basic DataSource Example

```java title=Example.java
import java.sql.Connection;
import org.apache.commons.dbcp.BasicDataSource;
public class BasicDataSourceExample {
  public static void main(String args[]) throws Exception {
    BasicDataSource bds = new BasicDataSource();
    bds.setDriverClassName("com.mysql.jdbc.Driver");
    bds.setUrl("jdbc:mysql://localhost/commons");
    bds.setUsername("root");
    bds.setPassword("");
//    bds.setInitialSize(5);
    Connection connection = bds.getConnection();
    System.err.println(connection);
    connection.close();
  }
}
```

Download: BasicDataSourceExample.zip ( 1,004 K )
Related examples in the same category
