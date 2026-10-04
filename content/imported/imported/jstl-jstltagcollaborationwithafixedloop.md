---
title: JSTL Tag collaboration with a fixed loop
nav: JSTL Tag collaboration wit...
description: JSTL Tag collaboration with a fixed loop : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20060503161810/http://www.java2s.com:80/Code/Java/JSTL/JSTLTagcollaborationwithafixedloop.htm
---
JSTL Tag collaboration with a fixed loop : Java examples (example source code) » JSTL » Loop

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
<html>
  <head>
    <title>Count to 10 Example(tracking even and odd)</title>
  </head>
  <body>
    <table border="0">
      <c:forEach var="i" begin="1" end="10" varStatus="status">
        <jsp:useBean id="status"
        type="javax.servlet.jsp.jstl.core.LoopTagStatus" />
        <c-rt:choose>
          <c-rt:when test="<%=status.getCount()%2==0%>">
            <c:set var="color" value="#eeeeee" />
          </c-rt:when>
          <c-rt:otherwise>
            <c:set var="color" value="#dddddd" />
          </c-rt:otherwise>
        </c-rt:choose>
        <tr>
          <td width="200" bgcolor="<c:out value="${color}"/>">
          <c:out value="${i}" />
          </td>
        </tr>
      </c:forEach>
    </table>
  </body>
</html>
```

Download: JSTL-Tag-collaboration-with-a-fixed-loop.zip (853 K)
---
Related examples in the same category
1. JSTL: Conditional Support -- Simple Conditional Execution Example
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
