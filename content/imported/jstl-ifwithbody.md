---
title: If with Body
nav: If with Body
description: <c:if test="${param.guess!='5'}">You did not guess my number!
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20060423084332/http://www.java2s.com:80/Code/Java/JSTL/IfwithBody.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>If with Body</title>
  </head>
  <body>
    <c:if test="${pageContext.request.method=='POST'}">
      <c:if test="${param.guess=='5'}">You guessed my number!
      <br />
      <br />
      <br />
      </c:if>
      <c:if test="${param.guess!='5'}">You did not guess my number!
      <br />
      <br />
      <br />
      </c:if>
    </c:if>
    <form method="post">Guess what number I am thinking of?
    <input type="text" name="guess" />
    <input type="submit" value="Try!" />
    <br />
    </form>
  </body>
</html>
```

Download: JSTL-IfWithBody.zip (851 K)
---
Related examples in the same category
1. JSTL core tag: if
2. JSTL RT If
3. JSTL: If Else
4. JSTL If No Body
5. JSTL: if tag
