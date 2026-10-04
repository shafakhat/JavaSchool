---
title: JSTL
nav: JSTL
description: This page allows you to enter information that is sent as request
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20061018125339/http://www.java2s.com/Code/Java/JSTL/JSTLSetpageparameters.htm
---
JSTL: Set page parameters

```java title=Example.java
<html>
  <head>
    <title>Set page parameters (2)</title>
  </head>
  <body>
    This page allows you to enter information that is sent as request
    parameters to another page.<br />
    There are two parameters, each with two values. <br />
    The next page list the different parameters with their values. <P />
    <form action="listPageParameters.jsp" method="get">
      <table>
        <tr><td>Enter an adjective:</td>
            <td><input type="text" name="adjective" /></td>
        </tr>
        <tr><td>Enter an adjective:</td>
            <td><input type="text" name="adjective" /></td>
        </tr>
        <tr><td>Enter a noun:</td>
            <td><input type="text" name="noun" /></td>
        </tr>
        <tr><td>Enter a noun:</td>
            <td><input type="text" name="noun" /></td>
        </tr>
      </table>
      <input type="submit" value="Send parameters" />
    </form>
  </body>
</html>
//listPageParameters.jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<html>
  <head>
    <title>List page parameters</title>
  </head>
  <body>
    You entered the following parameters:<br />
    <ul>
      <c:forEach var="pageParameter" items="${param}">
        <li> <c:out value="pageParameter" /> has the values
        <c:forEach var="currentValue" items="${pageParameter.value}">
          <c:out value="${currentValue}" />
        </c:forEach>
      </c:forEach>
    </ul>
  </body>
</html>
```

Related examples in the same category
