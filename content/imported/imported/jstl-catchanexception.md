---
title: Catch an Exception?
nav: Catch an Exception?
description: Imported from the java2s.com archive: Catch an Exception?
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20061026215134/http://www.java2s.com/Code/Java/JSTL/CatchanException.htm
---
Catch an Exception?

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Catch an Exception?</title>
  </head>
  <body>
    <c:catch var="e">
    <c:set var="x" value="10" scope="page" />
    <c:set var="y" value="five" scope="page" />
    10 divided by 0 is
    <c:out value="${10/0}" />
    <br />
    </c:catch>
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

Download: JSTL-Exception-Catch.zip ( 851 K )
---
Related examples in the same category
4. JSTL: Catch with if
5. JSTL: catch Exception
