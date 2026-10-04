---
title: Filling a Table : Java examples (example source code) » JSP » Database
nav: Filling a Table : Java exa...
description: connection = DriverManager.getConnection("jdbc:odbc:data", "userName", "password");
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20060513085322/http://www.java2s.com/Code/Java/JSP/FillingaTable.htm
---
Filling a Table

```java title=Example.java
<%@ page import="java.sql.*" %>
<HTML>
    <HEAD>
        <TITLE>Filling a Table</TITLE>
    </HEAD>
    <BODY>
        <H1>Filling a Table</H1>
        <%
            Connection connection = null;
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
            connection = DriverManager.getConnection("jdbc:odbc:data", "userName", "password");
            Statement statement = connection.createStatement();
            String command = "INSERT INTO Employees (ID, Name) VALUES (1, 'Joe')";
            statement.executeUpdate(command);
            command = "INSERT INTO Employees (ID, Name) VALUES (2, 'Yin')";
            statement.executeUpdate(command);
            ResultSet resultset =
                statement.executeQuery("select * from Employees");
            while(resultset.next()){
        %>
            <TABLE BORDER="1">
                <TR>
                    <TH>ID</TH>
                    <TH>Name</TH>
                </TR>
                <TR>
                    <TD> <%= resultset.getString(1) %> </TD>
                    <TD> <%= resultset.getString(2) %> </TD>
                </TR>
            </TABLE>
        <%
            }
        %>
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
6. Display table in Database
7. Selecting records with condition From a Database
8. Navigating in a Database Table 2
9. Using Table Metadata
10. Creating a Table
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
