---
title: Count to 10 Example using JSTL
nav: Count to 10 Example using ...
description: Count to 10 Example using JSTL : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20060423085709/http://www.java2s.com:80/Code/Java/JSTL/Countto10ExampleusingJSTL.htm
---
Count to 10 Example using JSTL : Java examples (example source code) » JSTL » Loop

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Count to 10 Example(using JSTL)</title>
  </head>
  <body>
    <table border="1">
      <tr>
        <td valign="top">
          <h3>From 1 to 10</h3>
          <c:forEach var="i" begin="1" end="10">
            <c:out value="${i}" />
            <br />
          </c:forEach>
        </td>
        <td valign="top">
          <h3>From 10 to 1</h3>
          <c:forEach var="i" begin="1" end="10">
            <c:out value="${11-i}" />
            <br />
          </c:forEach>
        </td>
      </tr>
      <tr>
        <td>
          <h3>By Twos</h3>
          <c:forEach var="i" begin="2" end="10" step="2">
            <c:out value="${i}" />
            <br />
          </c:forEach>
        </td>
        <td valign="top">&nbsp;
        </td>
      </tr>
    </table>
  </body>
</html>
```

Download: JSTL-Fixed-length-loops.zip (852 K)
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
9. JSTL For Each
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
