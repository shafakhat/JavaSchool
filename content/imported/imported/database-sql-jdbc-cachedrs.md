---
title: Cached RS
nav: Cached RS
description: String sql = "SELECT SSN, Name, Salary, Hiredate FROM Employees WHERE SSN=?";
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20091128185318/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/CachedRS.htm
---
```java title=Example.java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import javax.sql.rowset.CachedRowSet;
public class CachedRS {
  private final static String CRS_FILE_LOC = "cachedrs.crs";
  public static void main(String[] args) throws Exception {
    FileInputStream fis = new FileInputStream(CRS_FILE_LOC);
    ObjectInputStream in = new ObjectInputStream(fis);
    CachedRowSet crs = (CachedRowSet) in.readObject();
    fis.close();
    in.close();
    Class.forName("oracle.jdbc.driver.OracleDriver");
    crs.setUrl("jdbc:oracle:thin:@localhost:1521:ORCL");
    crs.setUsername("yourName");
    crs.setPassword("mypwd");
    String sql = "SELECT SSN, Name, Salary, Hiredate FROM Employees WHERE SSN=?";
    crs.setCommand(sql);
    crs.setInt(1, 111111111);
    crs.execute();
    FileOutputStream fos = new FileOutputStream(CRS_FILE_LOC);
    ObjectOutputStream out = new ObjectOutputStream(fos);
    out.writeObject(crs);
    out.close();
    crs.close();
    fis = new FileInputStream(CRS_FILE_LOC);
    in = new ObjectInputStream(fis);
    crs = (CachedRowSet) in.readObject();
    fis.close();
    in.close();
    while (crs.next()) {
      System.out.print("SSN: " + crs.getInt("ssn"));
      System.out.print(", Name: " + crs.getString("name"));
      System.out.print(", Salary: $" + crs.getDouble("salary"));
      System.out.print(", HireDate: " + crs.getDate("hiredate"));
    }
    crs.close();
  }
}
```

1.  Save CachedRowSet Back To Database
