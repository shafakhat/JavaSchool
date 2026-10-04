---
title: Controlling the type value of the OUT parameter
nav: Controlling the type value...
description: CallableStatement callableStatement = (CallableStatement) conn
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20130720010037/http://www.java2s.com:80/Code/Java/JDK-7/ControllingthetypevalueoftheOUTparameter.htm
---
Controlling the type value of the OUT parameter

```java title=Example.java
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.Types;
public class Test {
  public static void main(String[] args) throws Exception {
    Connection conn = DriverManager
        .getConnection("...", "username", "password");
    String query = "{CALL GETDATE(?,?)}";
    CallableStatement callableStatement = (CallableStatement) conn
        .prepareCall(query);
    callableStatement.setInt(1, 123);
    callableStatement.registerOutParameter(1, Types.DATE);
    callableStatement.executeQuery();
    Date date = callableStatement.getObject(2, Date.class);
  }
}
```

1.  Using the RowSetFactory class
---  ---
2.  Java 7 database enhancements:Get auto generated key
3.  Retrieving pseudo-columns
4.  Get parent logger
