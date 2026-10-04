---
title: Creating a Table : Java examples (example source code) » JSP » Database
nav: Creating a Table : Java ex...
description: connection = DriverManager.getConnection("jdbc:odbc:data", "userName", "password");
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20060513085344/http://www.java2s.com/Code/Java/JSP/CreatingaTable.htm
---
Creating a Table

```java title=Example.java
<%@ page import="java.sql.*" %>
<HTML>
    <HEAD>
        <TITLE>Creating a Table</TITLE>
    </HEAD>
    <BODY>
        <H1>Creating a Table</H1>
        <%
            Connection connection = null;
            try {
                Class.forName("sun.jdbc.odbc.JdbcOdbcDriver").newInstance();
                connection = DriverManager.getConnection("jdbc:odbc:data", "userName", "password");
                Statement statement = connection.createStatement();
                String command = "CREATE TABLE Employees (ID INTEGER, Name CHAR(50));";
                statement.executeUpdate(command);
            } catch (Exception e) {
                out.println("An error occurred.");
            }
        %>
        The Employees table was created.
    </BODY>
</HTML>
```

Related examples in the same category
---
1. JSP Database Demo
2. JSP Database Query
3. A First JSP Database
4. Navigating in a Database Table
5. Joining Tables
6. Filling a Table
7. Display table in Database
8. Selecting records with condition From a Database
9. Navigating in a Database Table 2
10. Using Table Metadata
11. Accessing the table field in Database
12. Fetching Data From a Database
13. JSTL: Transaction with a JSP
14. Using a Result object
15. Calling a Stored procedure within a JSP
16. Presenting database content using tags
17. Obtaining a Connection in JSP
18. Presenting database content
19. Using a DataSource
20. Using Transactions
21. Updating a database using the sql:update tag
22. Using a Preconfigured DataSource
23. Using the SortedMap
24. New Address Creation using executeUpdate
25. Obtaining a database Connection
26. JSP Access to Databases
