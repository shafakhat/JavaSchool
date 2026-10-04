---
title: Fetching Data From a Database : Java examples (example source code) » JSP » Database
nav: Fetching Data From a Datab...
description: Fetching Data From a Database : Java examples (example source code) » JSP » Database
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20060513085415/http://www.java2s.com/Code/Java/JSP/FetchingDataFromaDatabase.htm
---
Fetching Data From a Database : Java examples (example source code) » JSP » Database

Fetching Data From a Database

```java title=Example.java
<%@ page import="java.sql.*" %>
<% Class.forName("sun.jdbc.odbc.JdbcOdbcDriver"); %>
<HTML>
    <HEAD>
        <TITLE>Fetching Data From a Database</TITLE>
    </HEAD>
    <BODY>
        <H1>Database Lookup</H1>
        <FORM ACTION="self.jsp" METHOD="POST">
            Please enter the ID of the publisher you want to find:
            <BR>
            <INPUT TYPE="TEXT" NAME="id">
            <BR>
            <INPUT TYPE="SUBMIT" value="Submit">
        </FORM>
        <H1>Fetching Data From a Database</H1>
        <%
            Connection connection = DriverManager.getConnection(
                "jdbc:odbc:data", "userName", "password");
            Statement statement = connection.createStatement();
            String id = request.getParameter("id");
            ResultSet resultset =
                statement.executeQuery("select * from tableName where id = '" + id + "'") ;
            if(!resultset.next()) {
                out.println("Sorry, could not find that publisher. " +
                "Please <A HREF='tryAgain.html'>try again</A>.");
            } else {
        %>
        <TABLE BORDER="1">
            <TR>
               <TH>ID</TH>
               <TH>Name</TH>
               <TH>City</TH>
               <TH>State</TH>
               <TH>Country</TH>
           </TR>
           <TR>
               <TD> <%= resultset.getString(1) %> </TD>
               <TD> <%= resultset.getString(2) %> </TD>
               <TD> <%= resultset.getString(3) %> </TD>
               <TD> <%= resultset.getString(4) %> </TD>
               <TD> <%= resultset.getString(5) %> </TD>
           </TR>
       </TABLE>
       <BR>
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
6. Filling a Table
7. Display table in Database
8. Selecting records with condition From a Database
9. Navigating in a Database Table 2
10. Using Table Metadata
11. Creating a Table
12. Accessing the table field in Database
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
