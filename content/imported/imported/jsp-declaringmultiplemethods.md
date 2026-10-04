---
title: Declaring Multiple Methods
nav: Declaring Multiple Methods
description: Imported from the java2s.com archive: Declaring Multiple Methods
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20070128200516/http://www.java2s.com:80/Code/Java/JSP/DeclaringMultipleMethods.htm
---
```java title=Example.java
<HTML>
  <HEAD>
    <TITLE>Declaring Multiple Methods</TITLE>
  </HEAD>
  <BODY>
    <H1>Declaring Multiple Methods</H1>
    <%!
    int addem(int op1, int op2)
    {
      return op1 + op2;
    }
    int subtractem(int op1, int op2)
    {
      return op1 - op2;
    }
    %>
    <%
    out.println("2 + 2 = " + addem(2, 2) + "<BR>");
    out.println("8 - 2 = " + subtractem(8, 2) + "<BR>");
    %>
  </BODY>
</HTML>
```

Related examples in the same category
---
1. Define function
2. Passing the out Object to a Method
3. Using Recursion
4. Creating a Method
5. Passing Arrays to Methods
