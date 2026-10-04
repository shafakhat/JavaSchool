---
title: JSTL
nav: JSTL
description: Imported from the java2s.com archive: JSTL
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20060423084528/http://www.java2s.com:80/Code/Java/JSTL/JSTLIfElse.htm
---
JSTL: If Else

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Using Choose,Otherwise and When</title>
  </head>
  <body>
    <c:if test="${pageContext.request.method=='POST'}">Ok, we'll
    send
    <c:out value="${param.enter}" />
    <c:choose>
      <c:when test="${param.enter=='1'}">pizza.
      <br />
      </c:when>
      <c:otherwise>pizzas.
      <br />
      </c:otherwise>
    </c:choose>
    </c:if>
    <form method="post">Enter a number between 1 and 5:
    <input type="text" name="enter" />
    <input type="submit" value="Accept" />
    <br />
    </form>
  </body>
</html>
```

Download: JSTL-If-Else.zip (851 K)
---
Related examples in the same category
1. JSTL core tag: if
2. JSTL RT If
3. JSTL If No Body
4. If with Body
5. JSTL: if tag
