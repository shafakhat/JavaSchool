---
title: JSTL Remove Parameters
nav: JSTL Remove Parameters
description: Imported from the java2s.com archive: JSTL Remove Parameters
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20061018125325/http://www.java2s.com/Code/Java/JSTL/JSTLRemoveParameters.htm
---
JSTL Remove Parameters

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Set Examples</title>
  </head>
  <body>
  <h3>Remove Example</h3>
  <c:set var="test" value="Hello World" scope="page" />
  The value in the variable test before remove is
  <c:out value="${test}" />
  <br />
  <c:remove var="test" scope="page" />
  The value in the variable test after remove is
  <c:out value="${test}" />
  <br />
  </body>
</html>
```

Download: JSTL-Remove-Parameters.zip ( 852 K )
---
Related examples in the same category
3. JSTL: Set page parameters
