---
title: JSTL
nav: JSTL
description: <%-- 'param' is an implicit object. It is a Map that maps a 'key'
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20061018194026/http://www.java2s.com/Code/Java/JSTL/JSTLHTTPheader.htm
---
JSTL: HTTP header

```java title=Example.java
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<html>
  <head>
    <title>List HTTP headers</title>
  </head>
  <body>
    This page has the following HTTP headers:<br />
    <ol>
      <%-- 'param' is an implicit object. It is a Map that maps a 'key'
           (the parameter name) to a 'value' --%>
      <c:forEach var="nextHeader" items="${header}">
        <li> <c:out value="${nextHeader.key}" /> = <c:out value="${nextHeader.value}" />
      </c:forEach>
    </ol>
  </body>
</html>
```

Related examples in the same category
