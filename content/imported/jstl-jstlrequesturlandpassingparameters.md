---
title: JSTL Request URL And Passing Parameters
nav: JSTL Request URL And Passi...
description: href="<c:out value="${pageContext.request.requestURI}"/>?color=red">
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20061018125403/http://www.java2s.com/Code/Java/JSTL/JSTLRequestURLAndPassingParameters.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Query String Example</title>
  </head>
  <body>Your favorite color is:
  <b>
    <c:out value="${param.color}" />
  </b>
  <br />
  <br />
  Choose your favorite color:
  <br />
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=red">
  red</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=blue">
  blue</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=green">
  green</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=yellow">
  yellow</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=other">
  other</a>
  <br />
  </body>
</html>
```

Download: JSTL-RequestURLAndPassingParameters.zip ( 853 K )
---
Related examples in the same category
3. JSTL: Set page parameters
