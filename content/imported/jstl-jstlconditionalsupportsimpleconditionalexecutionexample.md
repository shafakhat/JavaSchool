---
title: JSTL
nav: JSTL
description: JSTL: Conditional Support -- Simple Conditional Execution Example : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20060503162223/http://www.java2s.com:80/Code/Java/JSTL/JSTLConditionalSupportSimpleConditionalExecutionExample.htm
---
JSTL: Conditional Support -- Simple Conditional Execution Example : Java examples (example source code) » JSTL » Loop

JSTL: Conditional Support -- Simple Conditional Execution Example

```java title=Example.java
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<html>
<head>
  <title>JSTL: Conditional Support -- Simple Conditional Execution Example</title>
</head>
<body bgcolor="#FFFFFF">
<h3>Loop in JSTL</h3>
    <c:forEach var="i" begin="1" end="10" step="1">
      <c:out value="${i}" />
      <br />
    </c:forEach>
</body>
</html>
```

Download: JSTL-Loop.zip (851 K)
---
Related examples in the same category
1. JSTL Tag collaboration with a fixed loop
2. JSTL: fortokens
3. JSTL: another for each and status
4. JSTL: for each and status
5. JSTL: for each and scoped variable
6. JSTL: for each loop
7. JSTL: for each
8. Count to 10 Example using JSTL
9. JSTL For Each
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
