---
title: JSTL core tag
nav: JSTL core tag
description: <c:out value="Phew, time has not stopped yet...<br /><br />" escapeXml="false" />
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20060423084206/http://www.java2s.com:80/Code/Java/JSTL/JSTLcoretagif.htm
---
JSTL core tag: if

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
<head><title>Using the Core JSTL tags</title></head>
<body>
<h2>Here are the available Time Zone IDs on your system</h2>
<jsp:useBean id="zone" class="com.java2s.ZoneWrapper" />
<jsp:useBean id="date" class="java.util.Date" />
<c:if test="${date.time != 0}" >
    <c:out value="Phew, time has not stopped yet...<br /><br />" escapeXml="false" />
</c:if>
<c:set var="zones" value="${zone.availableIDs}" scope="session" />
    <c:forEach var="id" items="${zones}">
        <c:out value="${id}<br />" escapeXml="false" />
    </c:forEach>
</body>
</html>
// Save the ZoneWrapper.class into WEB-INF/classes/com/java2s
//ZoneWrapper.java
package com.java2s;
import java.util.TimeZone;
public class ZoneWrapper {
  public ZoneWrapper() {
  }
  public String[] getAvailableIDs() {
    return TimeZone.getAvailableIDs();
  }
}
```

Related examples in the same category
---
1. JSTL RT If
2. JSTL: If Else
3. JSTL If No Body
4. If with Body
5. JSTL: if tag
