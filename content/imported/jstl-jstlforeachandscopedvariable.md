---
title: JSTL
nav: JSTL
description: JSTL: for each and scoped variable : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20060503161945/http://www.java2s.com:80/Code/Java/JSTL/JSTLforeachandscopedvariable.htm
---
JSTL: for each and scoped variable : Java examples (example source code) » JSTL » Loop

JSTL: for each and scoped variable

```java title=Example.java
<%@ taglib prefix="c"    uri="http://java.sun.com/jstl/core" %>
<c:set var="names" value="Joe, Zhou" scope="page" />
<html>
  <head>
    <title>forEach and status</title>
  </head>
  <body>
    <h1>The forEach tag exposes a scoped variable called 'count', which
    is the position of the current iteration of the collection.</h1>
    <h2>(Note, it is <i>not</i> the position of the element in the
        underlying collection)</h2>
    <c:forEach items="${pageScope.names}"
               var="currentName"
               varStatus="status"
    >
      Family member #<c:out value="${status.count}" /> is
        <c:out value="${currentName}" /> <br />
    </c:forEach>
  </body>
</html>
```

Related examples in the same category
---
1. JSTL: Conditional Support -- Simple Conditional Execution Example
2. JSTL Tag collaboration with a fixed loop
3. JSTL: fortokens
4. JSTL: another for each and status
5. JSTL: for each and status
6. JSTL: for each loop
7. JSTL: for each
8. Count to 10 Example using JSTL
9. JSTL For Each
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
