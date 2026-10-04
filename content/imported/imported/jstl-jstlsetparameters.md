---
title: JSTL Set Parameters
nav: JSTL Set Parameters
description: Imported from the java2s.com archive: JSTL Set Parameters
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20061018125357/http://www.java2s.com/Code/Java/JSTL/JSTLSetParameters.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Set Examples</title>
  </head>
  <body>
  <h3>Set With No Body</h3>
  <c:set var="str" value="Hello World" />
  str =
  <c:out value="${str}" />
  <br />
  <h3>Set With Body</h3>
  <c:set var="str">Hello, Again World</c:set>
  str =
  <c:out value="${str}" />
  <br />
  </body>
</html>
```

Download: JSTL-Set-Parameters.zip ( 851 K )
---
Related examples in the same category
3. JSTL: Set page parameters
