---
title: Accessing the table field in Database : Java examples (example source code) » JSP » Database
nav: Accessing the table field ...
description: Accessing the table field in Database : Java examples (example source code) » JSP » Database
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20060513085335/http://www.java2s.com/Code/Java/JSP/AccessingthetablefieldinDatabase.htm
---
Accessing the table field in Database : Java examples (example source code) » JSP » Database

Accessing the table field in Database

```java title=Example.java
<%@ page import="java.sql.*" %>
<% Class.forName("sun.jdbc.odbc.JdbcOdbcDriver") ; %>
<HTML>
    <HEAD>
        <TITLE>Accessing the tableName Database Table</TITLE>
    </HEAD>
    <BODY>
        <H1>Accessing the tableName Database Table</H1>
        <%
            Connection connection = DriverManager.getConnection(
                "jdbc:odbc:data", "userName", "password");
                Statement statement = connection.createStatement() ;
                ResultSet resultset =
                    statement.executeQuery("select name from tableName") ;
        %>
        <TABLE BORDER="1">
            <TR>
                <TH>Name</TH>
            </TR>
            <% while(resultset.next()){ %>
                <TR>
                    <TD>
                        <%= resultset.getString(1)%>
                    </TD>
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
7. Display table in Database
8. Selecting records with condition From a Database
9. Navigating in a Database Table 2
10. Using Table Metadata
11. Creating a Table
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
