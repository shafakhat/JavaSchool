---
title: JSTL RT If
nav: JSTL RT If
description: <%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20060423084306/http://www.java2s.com:80/Code/Java/JSTL/JSTLRTIf.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
<html>
  <head>
    <title>If Caseless</title>
  </head>
  <body>
    <c:set var="str" value="jStL" />
    <jsp:useBean id="str" type="java.lang.String" />
    <c-rt:if test='<%=str.equalsIgnoreCase("JSTL")%>'> They are
    equal</c-rt:if>
  </body>
</html>
```

Download: JSTL-RT-If.zip (851 K)
---
Related examples in the same category
1. JSTL core tag: if
2. JSTL: If Else
3. JSTL If No Body
4. If with Body
5. JSTL: if tag
