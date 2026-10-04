---
title: Display table in Database : Java examples (example source code) » JSP » Database
nav: Display table in Database ...
description: Display table in Database : Java examples (example source code) » JSP » Database
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20060513085327/http://www.java2s.com/Code/Java/JSP/DisplaytableinDatabase.htm
---
Display table in Database : Java examples (example source code) » JSP » Database

Display table in Database

```java title=Example.java
<%@ page import="java.sql.*" %>
<% Class.forName("sun.jdbc.odbc.JdbcOdbcDriver"); %>
<HTML>
    <HEAD>
        <TITLE>The tableName Database Table </TITLE>
    </HEAD>
    <BODY>
        <H1>The tableName Database Table </H1>
        <%
            Connection connection = DriverManager.getConnection(
                "jdbc:odbc:data", "Steve", "password");
            Statement statement = connection.createStatement() ;
            ResultSet resultset =
                statement.executeQuery("select * from tableName") ;
        %>
        <TABLE BORDER="1">
            <TR>
                <TH>ID</TH>
                <TH>Name</TH>
                <TH>City</TH>
                <TH>State</TH>
                <TH>Country</TH>
            </TR>
            <% while(resultset.next()){ %>
            <TR>
                <TD> <%= resultset.getString(1) %></td>
                <TD> <%= resultset.getString(2) %></TD>
                <TD> <%= resultset.getString(3) %></TD>
                <TD> <%= resultset.getString(4) %></TD>
                <TD> <%= resultset.getString(5) %></TD>
            </TR>
            <% } %>
        </TABLE>
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
