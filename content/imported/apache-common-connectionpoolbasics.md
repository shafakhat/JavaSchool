---
title: Connection Pool Basics
nav: Connection Pool Basics
description: import org.apache.commons.dbcp.DriverManagerConnectionFactory;
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20061026235132/http://www.java2s.com/Code/Java/Apache-Common/ConnectionPoolBasics.htm
---
Connection Pool Basics

```java title=Example.java
import java.sql.Connection;
import java.util.Properties;
import java.sql.PreparedStatement;
import org.apache.commons.dbcp.ConnectionFactory;
import org.apache.commons.dbcp.PoolingDriver;
import org.apache.commons.dbcp.PoolingDataSource;
import org.apache.commons.dbcp.DriverConnectionFactory;
import org.apache.commons.dbcp.PoolableConnectionFactory;
import org.apache.commons.dbcp.DriverManagerConnectionFactory;
import org.apache.commons.pool.impl.GenericObjectPool;
import org.apache.commons.pool.KeyedObjectPoolFactory;
import org.apache.commons.pool.impl.GenericKeyedObjectPoolFactory;
public class ConnectionPoolBasics {
  public static void main(String args[]) throws Exception {
    GenericObjectPool gPool = new GenericObjectPool();
    /*Class.forName("com.mysql.jdbc.Driver");
    DriverManagerConnectionFactory cf =
      new DriverManagerConnectionFactory(
        "jdbc:mysql://localhost/commons", "root", "");*/
    Properties props = new Properties();
    props.setProperty("Username", "root");
    props.setProperty("Password", "");
    ConnectionFactory cf =
      new DriverConnectionFactory(new com.mysql.jdbc.Driver(),
                                  "jdbc:mysql://localhost/commons",
                    props);
    KeyedObjectPoolFactory kopf =new GenericKeyedObjectPoolFactory(null, 8);
    PoolableConnectionFactory pcf =  new PoolableConnectionFactory(cf,
                                    gPool,
                                    kopf,
                                    null,
                                    false,
                                    true);
    for(int i = 0; i < 5; i++) {
      gPool.addObject();
    }
    // PoolingDataSource pds = new PoolingDataSource(gPool);
    PoolingDriver pd = new PoolingDriver();
    pd.registerPool("example", gPool);
    for(int i = 0; i < 5; i++) {
      gPool.addObject();
    }
    Connection conn = java.sql.DriverManager.getConnection("jdbc:apache:commons:dbcp:example");
    System.err.println("Connection: " + conn ); //": Delegate: " + ((org.apache.commons.dbcp.PoolingConnection)conn).getDelegate());
    // do some work with the connection
    PreparedStatement ps = conn.prepareStatement("Select * from customer where id = ?");
    System.err.println("Active: " + gPool.getNumActive() + ", Idle: " + gPool.getNumIdle());
    conn.close();
    System.err.println("Active: " + gPool.getNumActive() + ", Idle: " + gPool.getNumIdle());
  }
}
```

Download: ConnectionPoolBasics.zip ( 1,214 K )
Related examples in the same category
