---
title: Database connection pool demo
nav: Database connection pool d...
description: DriverManagerConnectionFactory cf = new DriverManagerConnectionFactory(
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20061026235124/http://www.java2s.com/Code/Java/Apache-Common/Databaseconnectionpooldemo.htm
---
Database connection pool demo

```java title=Example.java
import org.apache.commons.pool.impl.GenericObjectPool;
import org.apache.commons.dbcp.*;
import java.sql.*;
public class DBCPDemo{
  public static void main(String args[]) throws Exception{
    // create a generic pool
    GenericObjectPool pool = new GenericObjectPool(null);
    // use the connection factory which will wraped by
    // the PoolableConnectionFactory
    DriverManagerConnectionFactory cf =  new DriverManagerConnectionFactory(
                                            "jdbc:jtds:sqlserver://myserver:1433/tandem",
                                            "user",
                                            "pass");
    PoolableConnectionFactory pcf =  new PoolableConnectionFactory(cf, pool, null, "SELECT * FROM mysql.db", false, true);
    // register our pool and give it a name
    new PoolingDriver().registerPool("myPool", pool);
    // get a connection and test it
        Connection conn = DriverManager.getConnection("jdbc:apache:commons:dbcp:myPool");
        // now we can use this pool the way we want.
        System.err.println("Are we connected? " + !conn.isClosed());
        System.err.println("Idle Connections: " + pool.getNumIdle() + ", out of " + pool.getNumActive());
  }
}
```

Download: DBCPDemo.zip ( 1,214 K )
Related examples in the same category
