---
title: A First JSP Database : Java examples (example source code) » JSP » Database
nav: A First JSP Database : Jav...
description: <%@ taglib prefix="c" uri="http://java.sun.com/jstl/core_rt" %>
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20060513085452/http://www.java2s.com/Code/Java/JSP/AFirstJSPDatabase.htm
---
A First JSP Database

```java title=Example.java
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core_rt" %>
<%@ taglib prefix="sql" uri="http://java.sun.com/jstl/sql_rt" %>
<sql:setDataSource var="datasource"
                driver="com.mysql.jdbc.Driver"
                   url="jdbc:mysql://localhost/publish" />
<sql:query var="books" dataSource="${datasource}">
  SELECT id, title, price FROM book
</sql:query>
<html>
  <head>
    <title>A First JSP Database</title>
  </head>
  <body>
    <table border="1">
      <tr>
        <td>id</td><td>title</td><td>price</td>
      </tr>
      <c:forEach items="${books.rows}" var="row">
      <tr>
        <td><c:out value="${row.id}" /></td>
        <td><c:out value="${row.title}" /></td>
        <td><c:out value="${row.price}" /></td>
      </tr>
      </c:forEach>
    </table>
  </body>
</html>
```

Download: ExecuteQueryAndOutputJsp.zip (87 K)
---
Related examples in the same category
1. JSP Database Demo
2. JSP Database Query
3. Navigating in a Database Table
4. Joining Tables
5. Filling a Table
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
