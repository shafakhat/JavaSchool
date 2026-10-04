---
title: JSTL RT Get Browser Info
nav: JSTL RT Get Browser Info
description: <%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20060307045659/http://www.java2s.com:80/Code/Java/JSTL/JSTLRTGetBrowserInfo.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
<html>
  <head>
    <title>Check Browser</title>
  </head>
  <body>
    <c-rt:choose>
      <c-rt:when test="<%=request.getHeader(\"User-Agent\").indexOf(\"MSIE\")!=-1%>">
      You are using Internet Explorer
      </c-rt:when>
      <c-rt:otherwise>
      You are using Netscape, or some other browser....
      </c-rt:otherwise>
    </c-rt:choose>
  </body>
</html>
```

Download: JSTL-RT-GetBrowser-Info.zip (852 K)
Related examples in the same category
