---
title: Causing a Runtime Error
nav: Causing a Runtime Error
description: Imported from the java2s.com archive: Causing a Runtime Error
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20061027021039/http://www.java2s.com/Code/Java/JSP/CausingaRuntimeError.htm
---
```java title=Example.java
<HTML>
    <HEAD>
        <TITLE>Causing a Runtime Error</TITLE>
    </HEAD>
    <BODY>
        <H1>Causing a Runtime Error</H1>
        <%
            int i = 1;
            i = i / 0;
            out.println("The answer is " + i);
        %>
    </BODY>
</HTML>
```

Related examples in the same category
---
1. Catching an ArrayIndexOutOfBoundsException Exception
2. Creating a Custom Exception Object
3. Calling Superclass Constructors
4. Runtime Polymorphism
