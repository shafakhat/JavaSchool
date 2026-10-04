---
title: Calling Superclass Constructors
nav: Calling Superclass Constru...
description: Imported from the java2s.com archive: Calling Superclass Constructors
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20061027021051/http://www.java2s.com/Code/Java/JSP/CallingSuperclassConstructors.htm
---
```java title=Example.java
<HTML>
    <HEAD>
        <TITLE>Calling Superclass Constructors</TITLE>
    </HEAD>
    <BODY>
        <H1>Calling Superclass Constructors</H1>
        <%!
            javax.servlet.jsp.JspWriter localOut;
            class a
            {
                a() throws java.io.IOException
                {
                    localOut.println("In a\'s constructor...<BR>");
                }
            }
            class b extends a
            {
                b() throws java.io.IOException
                {
                    localOut.println("In b\'s constructor...<BR>");
                }
            }
        %>
        <%
        localOut = out;
        b obj = new b();
        %>
    </BODY>
</HTML>
```

Related examples in the same category
---
1. Catching an ArrayIndexOutOfBoundsException Exception
2. Causing a Runtime Error
3. Creating a Custom Exception Object
4. Runtime Polymorphism
