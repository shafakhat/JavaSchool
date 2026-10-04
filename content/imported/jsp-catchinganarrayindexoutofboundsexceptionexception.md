---
title: Catching an ArrayIndexOutOfBoundsException Exception
nav: Catching an ArrayIndexOutO...
description: <TITLE>Catching an ArrayIndexOutOfBoundsException Exception</TITLE>
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20061026101927/http://www.java2s.com:80/Code/Java/JSP/CatchinganArrayIndexOutOfBoundsExceptionException.htm
---
```java title=Example.java
<HTML>
    <HEAD>
        <TITLE>Catching an ArrayIndexOutOfBoundsException Exception</TITLE>
    </HEAD>
    <BODY>
        <H1>Catching an ArrayIndexOutOfBoundsException Exception</H1>
    <%
    try {
        int array[] = new int[10];
        array[100] = 100;
    } catch (ArrayIndexOutOfBoundsException e) {
        out.println("Array index out of bounds.");
    }
    %>
    </BODY>
</HTML>
```

Related examples in the same category
---
1. Causing a Runtime Error
2. Creating a Custom Exception Object
3. Calling Superclass Constructors
4. Runtime Polymorphism
