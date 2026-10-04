---
title: JSTL
nav: JSTL
description: Imported from the java2s.com archive: JSTL
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20061026215147/http://www.java2s.com/Code/Java/JSTL/JSTLcatchException.htm
---
JSTL: catch Exception

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>The c:catch action</title>
  </head>
  <body>
    <c:catch var="signalException">
      <%
        int i= (int) (Math.random() * 10);
        if (i < 5 )
          throw new NullPointerException(); %>
    </c:catch>
    <c:choose>
      <c:when test="${signalException != null}">
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
5. JSTL: Catch with if
