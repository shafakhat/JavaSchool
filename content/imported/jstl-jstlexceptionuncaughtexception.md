---
title: JSTL Exception
nav: JSTL Exception
description: Imported from the java2s.com archive: JSTL Exception
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20061026215152/http://www.java2s.com/Code/Java/JSTL/JSTLExceptionUnCaughtException.htm
---
JSTL Exception: UnCaught Exception

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Throw an Exception</title>
  </head>
  <body>
  <c:set var="x" value="10" scope="page" />
  <c:set var="y" value="five" scope="page" />
  x divided by y is
  <c:out value="${x/y}" />
  <br />
  </body>
</html>
```

Download: JSTL-Exception-UnCaughtException.zip ( 852 K )
---
Related examples in the same category
4. JSTL: Catch with if
5. JSTL: catch Exception
