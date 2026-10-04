---
title: JSTL Simple Calculation
nav: JSTL Simple Calculation
description: Imported from the java2s.com archive: JSTL Simple Calculation
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20061018192723/http://www.java2s.com/Code/Java/JSTL/JSTLSimpleCalculation.htm
---
```java title=Example.java
<%@ page contentType="text/html" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<html>
  <head>
    <title>JSP is Easy</title>
  </head>
  <body bgcolor="white">
    <h1>JSP is as easy as ...</h1>
    <%-- Calculate the sum of 1 + 2 + 3 dynamically --%>
    1 + 2 + 3 = <c:out value="${1 + 2 + 3}" />
  </body>
</html>
```

Download: JSTL-Simple-Calculation.zip ( 852 K )
Related examples in the same category
