---
title: JSTL SQL Query
nav: JSTL SQL Query
description: <%@ taglib uri="http://java.sun.com/jstl/sql" prefix="sql" %>
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20060307044326/http://www.java2s.com:80/Code/Java/JSTL/JSTLSQLQuery.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/sql" prefix="sql" %>
<sql:setDataSource var="dataSource" driver="org.gjt.mm.mysql.Driver"
url="jdbc:mysql://localhost/forum?user=forumuser"
scope="session" />
<html>
  <head>
    <title>Query Example</title>
  </head>
  <body>
<sql:query var = "users" dataSource="${dataSource}">
select column_uid,column_pwd,column_accesses,column_first,column_last,column_bad,column_posted,column_type from t_users
</sql:query>
<table border=1>
<c:forEach var="row" items="${users.rows}">
<tr>
<td><c:out value="${row.column_uid}"/></td>
<td><c:out value="${row.column_pwd}"/></td>
<td><c:out value="${row.column_accesses}"/></td>
<td><c:out value="${row.column_first}"/></td>
<td><c:out value="${row.column_last}"/></td>
<td><c:out value="${row.column_bad}"/></td>
<td><c:out value="${row.column_posted}"/></td>
<td><c:out value="${row.column_type}"/></td>
</tr>
</c:forEach>
</table>
  </body>
</html>
```

Download: JSTL-SQL-Query.zip (6553 K)
---
Related examples in the same category
1. JSTL SQL Update
2. Updating a database using the sql:update tag
3. Presenting database content using tags
4. JSTL: Transaction with a JSP
5. SQL Tag Out Examples
