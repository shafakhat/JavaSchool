---
title: JSTL
nav: JSTL
description: This JSP stores the 'para' in a session-scoped variable where
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20061027000045/http://www.java2s.com/Code/Java/JSTL/JSTLsetattributes.htm
---
JSTL: set attributes

```java title=Example.java
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<html>
  <body>
    This JSP stores the 'para' in a session-scoped variable where
    the other JSPs in the web application can access it.
    <p />
    <c:set var="para" value="${41+1}" scope="session"  />
     Click <a href="displayAttributes.jsp">here</a> to view it.
  </body>
</html>
//displayAttributes.jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<html>
  <head>
    <title>Retrieval of attributes</title>
  </head>
  <body>
    The para is <c:out value="${sessionScope.para}" /> <br/>
  </body>
</html>
```

Related examples in the same category
1. JSTL: Remove the attributes
