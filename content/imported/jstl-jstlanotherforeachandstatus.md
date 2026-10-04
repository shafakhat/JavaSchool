---
title: JSTL
nav: JSTL
description: JSTL: another for each and status : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20060503162037/http://www.java2s.com:80/Code/Java/JSTL/JSTLanotherforeachandstatus.htm
---
JSTL: another for each and status : Java examples (example source code) » JSTL » Loop

JSTL: another for each and status

```java title=Example.java
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<%
  synchronized (pageContext) {
    String[] names = {"Joe", "Rosy", "Petter", "Rob"};
    pageContext.setAttribute("names", names, PageContext.PAGE_SCOPE);
  }
%>
<html>
  <head>
    <title>forEach and status</title>
  </head>
  <body>
    The forEach tag exposes a scoped variable called 'count', which
    is the position of the current element within the collection. <br />
    <c:forEach var="currentName" items="${pageScope.names}" varStatus="status">
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
4. JSTL: for each and status
5. JSTL: for each and scoped variable
6. JSTL: for each loop
7. JSTL: for each
8. Count to 10 Example using JSTL
9. JSTL For Each
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
