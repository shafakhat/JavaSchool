---
title: Creating a Method
nav: Creating a Method
description: Imported from the java2s.com archive: Creating a Method
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20070128195744/http://www.java2s.com:80/Code/Java/JSP/CreatingaMethod.htm
---
Creating a Method

```java title=Example.java
<HTML>
  <HEAD>
    <TITLE>Creating a Method</TITLE>
  </HEAD>
  <BODY>
    <H1>Creating a Method</H1>
    <%!
    int addem(int op1, int op2)
    {
      return op1 + op2;
    }
    %>
    <%
    out.println("2 + 2 = " + addem(2, 2));
    %>
  </BODY>
</HTML>
```

Related examples in the same category
---
1. Define function
2. Passing the out Object to a Method
3. Using Recursion
4. Declaring Multiple Methods
5. Passing Arrays to Methods
