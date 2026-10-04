---
title: Map ResultSet to Object
nav: Map ResultSet to Object
description: PreparedStatement ps = conn.prepareStatement("SELECT * from movie, person " +
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20070110223035/http://www.java2s.com:80/Code/Java/Apache-Common/MapResultSettoObject.htm
---
Map ResultSet to Object

```java title=Example.java
import org.apache.commons.dbcp.BasicDataSource;
import org.apache.commons.beanutils.DynaBean;
import org.apache.commons.beanutils.ResultSetDynaClass;
import java.util.Iterator;
import java.sql.ResultSet;
import java.sql.Connection;
import java.sql.PreparedStatement;
public class DynaBeansExampleV2 {
  public static void main(String args[]) throws Exception {
    Connection conn = getConnection();
    PreparedStatement ps =  conn.prepareStatement("SELECT * from movie, person " +
                                      "WHERE movie.director = person.Id");
    ResultSet rs = ps.executeQuery();
    ResultSetDynaClass rsdc = new ResultSetDynaClass(rs);
    Iterator itr = rsdc.iterator();
    while(itr.hasNext()) {
      DynaBean bean = (DynaBean)itr.next();
      System.err.println(bean.get("title"));
    }
    conn.close();
  }
  private static Connection getConnection() throws Exception {
    BasicDataSource bds = new BasicDataSource();
    bds.setDriverClassName("com.mysql.jdbc.Driver");
    bds.setUrl("jdbc:mysql://localhost/commons");
    bds.setUsername("root");
    bds.setPassword("");
    //bds.setInitialSize(5);
    return bds.getConnection();
  }
}
```

Related examples in the same category
