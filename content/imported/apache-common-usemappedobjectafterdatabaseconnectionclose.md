---
title: Use Mapped Object after database Connection close
nav: Use Mapped Object after da...
description: Imported from the java2s.com archive: Use Mapped Object after database Connection close
section: Imported - java2s Archive
order: 1073
source: https://web.archive.org/web/20070129024640/http://www.java2s.com:80/Code/Java/Apache-Common/UseMappedObjectafterdatabaseConnectionclose.htm
---
Use Mapped Object after database Connection close

```java title=Example.java
import org.apache.commons.dbcp.BasicDataSource;
import org.apache.commons.beanutils.DynaBean;
import org.apache.commons.beanutils.RowSetDynaClass;
import java.util.Iterator;
import java.sql.ResultSet;
import java.sql.Connection;
import java.sql.PreparedStatement;
public class DynaBeansExampleV3 {
  public static void main(String args[]) throws Exception {
    Connection conn = getConnection();
    PreparedStatement ps =
      conn.prepareStatement(
        "SELECT * from movie, person " +
        "WHERE movie.director = person.Id");
    ResultSet rs = ps.executeQuery();
    RowSetDynaClass rsdc = new RowSetDynaClass(rs);
    conn.close();
    Iterator itr = rsdc.getRows().iterator();
    while(itr.hasNext()) {
      DynaBean bean = (DynaBean)itr.next();
      System.err.println(bean.get("title"));
    }
  }
  private static Connection getConnection() throws Exception {
    BasicDataSource bds = new BasicDataSource();
    bds.setDriverClassName("com.mysql.jdbc.Driver");
    bds.setUrl("jdbc:mysql://localhost/commons");
    bds.setUsername("root");
    bds.setPassword("");
//    bds.setInitialSize(5);
    return bds.getConnection();
  }
}
```

Download: BeanUtilsDynaBeansExampleV3.zip ( 1,005 K )
---
Related examples in the same category
1. Map ResultSet to Object
