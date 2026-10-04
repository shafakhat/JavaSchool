---
title: All data types for Oracle
nav: All data types for Oracle
description: String url = "jdbc:oracle:thin:@localhost:1521:databaseName";
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20061018171455/http://www.java2s.com/Code/Java/Database-SQL-JDBC/AlldatatypesforOracle.htm
---
All data types for Oracle

```java title=Example.java
/**
Code revised from
Database Metadata with JDBC
A sample from
JDBC Metadata, MySQL, and Oracle Recipes
by Mahmoud Parsian
*/
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
 public class CreateTableAllTypesInOracle {
    public static Connection getConnection() throws Exception {
        String driver = "oracle.jdbc.driver.OracleDriver";
        String url = "jdbc:oracle:thin:@localhost:1521:databaseName";
        String username = "scott";
        String password = "tiger";
        Class.forName(driver);  // load Oracle driver
        Connection conn = DriverManager.getConnection(url, username, password);
        return conn;
    }
    public static void main(String[] args) {
        PreparedStatement pstmt = null;
        Connection conn = null;
        try {
            conn = getConnection();
            pstmt = conn.prepareStatement("CREATE TYPE varray_type is VARRAY(5) OF VARCHAR(10)");
            pstmt.executeUpdate();
            // Create an OBJECT type
            pstmt = conn.prepareStatement("CREATE TYPE oracle_object is OBJECT(column_string VARCHAR(128), column_integer INTEGER)");
            pstmt.executeUpdate();
            StringBuffer allTypesTable = new StringBuffer("CREATE TABLE oracle_all_types(");
            //                    Column Name          Oracle Type              Java Type
            allTypesTable.append("column_short           SMALLINT, ");          // short
            allTypesTable.append("column_int             INTEGER, ");           // int
            allTypesTable.append("column_float           REAL, ");              // float; can also be NUMBER
            allTypesTable.append("column_double          DOUBLE PRECISION, ");  // double; can also be FLOAT or NUMBER
            allTypesTable.append("column_bigdecimal      DECIMAL(13,0), ");     // BigDecimal
            allTypesTable.append("column_string          VARCHAR2(254), ");     // String; can also be CHAR(n)
            allTypesTable.append("column_characterstream LONG, ");              // CharacterStream or AsciiStream
            allTypesTable.append("column_bytes           RAW(2000), ");         // byte[]; can also be LONG RAW(n)
            allTypesTable.append("column_binarystream    RAW(2000), ");         // BinaryStream; can also be LONG RAW(n)
            allTypesTable.append("column_timestamp       DATE, ");              // Timestamp
            allTypesTable.append("column_clob            CLOB, ");              // Clob
            allTypesTable.append("column_blob            BLOB, ");              // Blob; can also be BFILE
            allTypesTable.append("column_bfile           BFILE, ");             // oracle.sql.BFILE
            allTypesTable.append("column_array           varray_type, ");       // oracle.sql.ARRAY
            allTypesTable.append("column_object          oracle_object)");      // oracle.sql.OBJECT
            pstmt.executeUpdate(allTypesTable.toString());
        } catch (Exception e) {
            // creation of table failed.
            // handle the exception
            e.printStackTrace();
        }
    }
}
```

Related examples in the same category
---
6. Test Oracle JDBC Driver Installation
7. Create Employee Table Oracle
8. Count row in Oracle
9. Get Column Names From ResultSet for Oracle
10. Demo ResultSet Oracle
11. Get Column Privileges Oracle
12. Test OCINet 8 App
13. Test SSL
14. Test Data Encryption Integrity
15. Test DataSource LookUp
16. OracleDataSource Demo
17. Register custome type to Oracle
18. Insert custom type to Oracle
19. Check JDBC Installation for Oracle
