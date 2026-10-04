---
title: Adding a New Column Name in Database Table
nav: Adding a New Column Name i...
description: Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbctutorial",
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20090502034936/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/AddingaNewColumnNameinDatabaseTable.htm
---
Adding a New Column Name in Database Table

```java title=Example.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
public class Main {
  public static void main(String[] argv) throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbctutorial",
        "root", "root");
    Statement st = con.createStatement();
    int n = st.executeUpdate("ALTER TABLE mytable ADD col int");
    System.out.println("Query OK, " + n + " rows affected");
  }
}
```

1.  Get Column Corresponding Class Name
---  ---
2.  Get Column Detail Information
3.  Get Column Display Size.zip
4.  Get Column Label
5.  Get Column Name
6.  Use DatabaseMetaData to get table column names
7.  Get Column Name And Type For A Table
8.  Get Column Name From ResultSet Metadata
9.  Get Column Number Of Digits To Right Of The Decimal Point
10.  Get Column Number Of Presions Number Of Decimal Digits
11.  Get Column ORDINAL POSITION
12.  Get Column Privilieges
13.  Get Column Size
14.  Get Column Sql Data Type
15.  Get Column SQL Type Name
16.  Get Column Type
17.  Get Table Optimal Set Of Columns
18.  Is Column A Cash Value
19.  Is Column Auto Increase
20.  Is Column Case Sensitive
21.  Is Column Definitely Writable
22.  Is Column Nullable
23.  Is Column Nullable From ResultSet Metadata
24.  Is Column Readonly
25.  Is Column Searchable
26.  Is Column Signed Number
27.  Is Column Writable
28.  Make Unique Column in Database Table
29.  Remove Unique Column in Database Table
30.  Arrange a Column of Database Table
31.  Change Column Name of a Table
32.  Sum of Column in a Database Table
33.  Delete a Column from a Database Table
34.  Designated column's table name
35.  If a table column can have a null value or not?
36.  If a table column value is auto-increment?
37.  Get Column Names From ResultSet for MySQL
