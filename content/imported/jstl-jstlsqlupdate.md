---
title: JSTL SQL Update
nav: JSTL SQL Update
description: <%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20060513084526/http://www.java2s.com/Code/Java/JSTL/JSTLSQLUpdate.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
<%@ taglib uri="http://java.sun.com/jstl/sql" prefix="sql" %>
<sql:setDataSource var="dataSource" driver="org.gjt.mm.mysql.Driver"
url="jdbc:mysql://localhost/forum?user=forumuser"
scope="session" />
<html>
  <head>
    <title>General Query</title>
  </head>
  <body>
  <c:choose>
    <c:when test="${param.cmd!=null}">
      <c:set var="str" value="${param.cmd}" />
    </c:when>
    <c:otherwise>
      <c:set var="str"
      value="select * from tableName" />
    </c:otherwise>
  </c:choose>
  Please enter a query:
  <br />
  <form method="post">
    <textarea name="cmd" cols="40" rows="5">
<c:out value="${str}" />
    </textarea>
    <br />
    <input type="submit" />
  </form>
  <c:if test="${pageContext.request.method=='POST'}">
    <c:catch var="e">
      <sql:query var="users" dataSource="${dataSource}"
      sql="${param.cmd}" />
      <table border="1">
        <c:forEach var="row" items="${users.rows}"
        varStatus="status">
          <jsp:useBean id="status"
          type="javax.servlet.jsp.jstl.core.LoopTagStatus" />
          <c-rt:if test="<%=status.getCount()==1%>">
            <tr>
              <c:forEach var="col" items="${row}">
                <th>
                  <c:out value="${col.key}" />
                </th>
              </c:forEach>
            </tr>
          </c-rt:if>
          <tr>
            <c:forEach var="col" items="${row}">
              <td>
                <c:out value="${col.value}" />
              </td>
            </c:forEach>
          </tr>
        </c:forEach>
      </table>
    </c:catch>
    <c:if test="${e!=null}">
      <h3>Error</h3>
      <c:out value="${e}" />
    </c:if>
  </c:if>
  </body>
</html>
```

Download: JSTL-SQL-Update.zip (6553 K)
---
Related examples in the same category
1. JSTL SQL Query
2. Updating a database using the sql:update tag
3. Presenting database content using tags
4. JSTL: Transaction with a JSP
5. SQL Tag Out Examples
