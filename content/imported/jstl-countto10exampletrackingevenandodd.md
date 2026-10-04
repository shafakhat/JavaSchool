---
title: Count to 10 Example
nav: Count to 10 Example
description: Count to 10 Example: tracking even and odd : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20060503161835/http://www.java2s.com:80/Code/Java/JSTL/Countto10Exampletrackingevenandodd.htm
---
Count to 10 Example: tracking even and odd : Java examples (example source code) » JSTL » Loop

Count to 10 Example: tracking even and odd

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

Download: JSTL-HTML-Table.zip (851 K)
---
Related examples in the same category
1. JSTL: Conditional Support -- Simple Conditional Execution Example
2. JSTL Tag collaboration with a fixed loop
3. JSTL: fortokens
4. JSTL: another for each and status
5. JSTL: for each and status
6. JSTL: for each and scoped variable
7. JSTL: for each loop
8. JSTL: for each
9. Count to 10 Example using JSTL
10. JSTL For Each
11. JSTL Form Value and ForEach Loop
