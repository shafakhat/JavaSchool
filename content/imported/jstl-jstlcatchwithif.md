---
title: JSTL
nav: JSTL
description: pageContext.setAttribute("signalStrength", new Integer(i), PageContext.PAGE_SCOPE);
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20061026215140/http://www.java2s.com/Code/Java/JSTL/JSTLCatchwithif.htm
---
JSTL: Catch with if

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%
  int i= (int) (Math.random() * 10);
  pageContext.setAttribute("signalStrength", new Integer(i), PageContext.PAGE_SCOPE);
%>
<html>
  <head>
    <title>The c:catch action</title>
  </head>
  <body>
    <c:if test="${pageScope.signalStrength < 5}">
      <c:set var="signalFailure" value="true" scope="page" />
    </c:if>
    <c:choose>
      <c:when test="${pageScope.signalFailure == true}">
        Exception occurs.
      </c:when>
      <c:otherwise>
        No Exception.
      </c:otherwise>
    </c:choose>
  </body>
</html>
```

Related examples in the same category
5. JSTL: catch Exception
