---
title: Format Locale date in JSP
nav: Format Locale date in JSP
description: <%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20060717054052/http://www.java2s.com:80/Code/Java/JSTL/FormatLocaledateinJSP.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<jsp:useBean id="date" class="java.util.Date" />
<html>
<head><title><fmt:message key="Welcome" /></title></head>
<body>
<h2><fmt:message key="Hello" /> <fmt:message key="and" /> <fmt:message key="Welcome" /></h2>
<fmt:formatDate value="${date}" type="both" dateStyle="full" timeStyle="short" /> <br />
Locale: <c:out value="${pageContext.request.locale.language}" />_<c:out value="${pageContext.request.locale.country}" />
</body>
</html>
```

Related examples in the same category
---
1. JSTL Time Zone
2. JSTL Parse Date
3. JSTL Format: Date
4. Date Formating in JSTL
