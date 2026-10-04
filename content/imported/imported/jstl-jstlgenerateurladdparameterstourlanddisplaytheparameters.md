---
title: JSTL
nav: JSTL
description: JSTL: generate URL, add parameters to url and display the parameters
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20070706234123/http://www.java2s.com:80/Code/Java/JSTL/JSTLgenerateURLaddparameterstourlanddisplaytheparameters.htm
---
JSTL: generate URL, add parameters to url and display the parameters

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>the c:url action (1)</title>
  </head>
  <body>
    This page takes 3 values that you specify, and forwards them to another JSP.
    That JSP will create a URL to another page, that then extracts the
    parameters and displays them.
    <p />
      <form action="createURL.jsp" method="post">
        <table>
          <tr><td>Enter name:</td>
              <td><input type="text" name="name"   /></td></tr>
          <tr><td>Enter age:</td>
              <td><input type="text" name="age"    /></td></tr>
          <tr><td>Enter gender:</td >
              <td><input type="text" name="gender" /></td></tr>
        </table>
        <input type="submit" value="Submit details" />
      </form>
  </body>
</html>
//createURL.jsp
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<c:url value="displayValues.jsp" var="displayURL">
  <c:param name="nameParam"   value="${param.name}" />
  <c:param name="ageParam"    value="${param.age}" />
  <c:param name="genderParam" value="${param.gender}" />
</c:url>
<html>
  <head>
    <title>the c:url action (2)</title>
  </head>
  <body>
    This page receives the values you specified, and creates a URL that contains
    them.
    <p />
    The generated URL is <c:out value="${displayURL}" />. <p/>
    Click <a href='<c:out value="${displayURL}" />'>here</a> to view the it.
  </body>
</html>
//displayValues.jsp
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>the c:url action (3)</title>
  </head>
  <body>
    <h3>List of query string parameters:</h3>
    <ul>
      <c:forEach items="${param}" var="currentParam">
        <li><c:out value="${currentParam.key}" />
            = <c:out value="${currentParam.value}" /></li>
      </c:forEach>
    </ul>
 </body>
</html>
```

Related examples in the same category
