---
title: JSTL If No Body
nav: JSTL If No Body
description: Imported from the java2s.com archive: JSTL If No Body
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20060502044642/http://www.java2s.com:80/Code/Java/JSTL/JSTLIfNoBody.htm
---
JSTL If No Body

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>If with NO Body</title>
  </head>
  <body>
    <c:if test="${pageContext.request.method=='POST'}">
    <c:if test="${param.guess=='5'}" var="result" />
    I tested to see if you picked my number, the result was
    <c:out value="${result}" />
    </c:if>
    <form method="post">Guess what number I am thinking of?
    <input type="text" name="guess" />
    <input type="submit" value="Try!" />
    <br />
    </form>
  </body>
</html>
```

Download: JSTL-If-No-Body.zip (851 K)
---
Related examples in the same category
1. JSTL core tag: if
2. JSTL RT If
3. JSTL: If Else
4. If with Body
5. JSTL: if tag
