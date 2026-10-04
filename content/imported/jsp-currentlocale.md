---
title: Current Locale
nav: Current Locale
description: <%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20070503153327/http://www.java2s.com:80/Code/Java/JSP/CurrentLocale.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
<head><title><fmt:message key="Welcome" /></title></head>
<body>
<h2><fmt:message key="Hello" /> <fmt:message key="and" /> <fmt:message key="Welcome" /></h2>
Locale: <c:out value="${pageContext.request.locale.language}" />_<c:out value="${pageContext.request.locale.country}" />
<br /><br />
<fmt:formatNumber value="1000000" type="currency" />
</body>
</html>
```

Related examples in the same category
---
1. Locale info
2. Locale Display in a JSP
8. Internationalized Web Applications: JavaServer Pages
