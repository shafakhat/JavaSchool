---
title: JSTL
nav: JSTL
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20060503161958/http://www.java2s.com:80/Code/Java/JSTL/JSTLforeachloop.htm
---
JSTL: for each loop

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core"    prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/core_rt" prefix="c-rt" %>
<%!
  String[] names = { "Joe", "Rosy", "Sissi", "Sun" };
  int[]    ages  = {29, 8, 6, 5};
%>
<HTML>
  <HEAD><TITLE>JSTL 'forEach' tag</TITLE></HEAD>
  <BODY>
    <H1>List of people</H1>
    <TABLE BORDER="1">
      <TH>Name</TH>
      <c-rt:forEach var="person" items="<%= names %>">
        <TR>
          <TD><c:out value="${person}"  /></TD>
          <TD><c:out value="${ages[i]}" /></TD>
        </TR>
      </c-rt:forEach>
    </TABLE>
  </BODY>
</HTML>
```

Related examples in the same category
---
1. JSTL: Conditional Support -- Simple Conditional Execution Example
2. JSTL Tag collaboration with a fixed loop
3. JSTL: fortokens
4. JSTL: another for each and status
5. JSTL: for each and status
6. JSTL: for each and scoped variable
7. JSTL: for each
8. Count to 10 Example using JSTL
9. JSTL For Each
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
