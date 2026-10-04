---
title: JSTL
nav: JSTL
description: <%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20060423084559/http://www.java2s.com:80/Code/Java/JSTL/JSTLfortokens.htm
---
JSTL: fortokens

```java title=Example.java
<%@ taglib prefix="c"    uri="http://java.sun.com/jstl/core" %>
<c:set var="names" value="Joe:Petter;Ryan|John" scope="page" />
<html>
  <head>
    <title>forTokens action</title>
  </head>
  <body>
    <c:forTokens items="${pageScope.names}"
                 delims=":;|"
                 var="currentName"
                 varStatus="status"
      >
      Family member #<c:out value="${status.count}" /> is
        <c:out value="${currentName}" /> <br />
    </c:forTokens>
  </body>
</html>
```

Related examples in the same category
---
1. JSTL: Conditional Support -- Simple Conditional Execution Example
2. JSTL Tag collaboration with a fixed loop
3. JSTL: another for each and status
4. JSTL: for each and status
5. JSTL: for each and scoped variable
6. JSTL: for each loop
7. JSTL: for each
8. Count to 10 Example using JSTL
9. JSTL For Each
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
