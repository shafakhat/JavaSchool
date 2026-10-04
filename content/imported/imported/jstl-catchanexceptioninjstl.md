---
title: Catch an Exception in JSTL
nav: Catch an Exception in JSTL
description: Imported from the java2s.com archive: Catch an Exception in JSTL
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20061026215124/http://www.java2s.com/Code/Java/JSTL/CatchanExceptioninJSTL.htm
---
Catch an Exception in JSTL

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Catch an Exception</title>
  </head>
  <body>
    <c:catch var="e">
    <c:set var="x" value="10" scope="page" />
    <c:set var="y" value="five" scope="page" />
    x divided by y is
    <c:out value="${x/y}" />
    <br />
    </c:catch>
    <br />
    <c:if test="${e!=null}">The caught exception is:
    <c:out value="${e}" />
    <br />
    </c:if>
    <c:if test="${e==null}">No exception was thrown
    <br />
    </c:if>
  </body>
</html>
```

Download: JSTL-Exception-Display-Exceptions.zip ( 853 K )
---
Related examples in the same category
4. JSTL: Catch with if
5. JSTL: catch Exception
