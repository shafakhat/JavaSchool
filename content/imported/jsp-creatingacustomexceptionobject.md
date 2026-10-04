---
title: Creating a Custom Exception Object
nav: Creating a Custom Exceptio...
description: Imported from the java2s.com archive: Creating a Custom Exception Object
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20061026100723/http://www.java2s.com:80/Code/Java/JSP/CreatingaCustomExceptionObject.htm
---
```java title=Example.java
<HTML>
    <HEAD>
        <TITLE>Creating a Custom Exception Object</TITLE>
    </HEAD>
    <BODY>
        <H1>Creating a Custom Exception Object</H1>
        <%!
            class NewException extends Exception
            {
                int value;
                public String toString()
                {
                    return "NewException " + value;
                }
                NewException(int v)
                {
                    value = v;
                }
            }
            void doWork(int value) throws NewException
            {
                if(value == 0){
                    throw new NewException(value);
            }
        }
    %>
    <%
        try {
            doWork(3);
            doWork(0);
        } catch (NewException e) {
            out.println("Exception: " + e);
        }
    %>
    </BODY>
</HTML>
```

Related examples in the same category
---
1. Catching an ArrayIndexOutOfBoundsException Exception
2. Causing a Runtime Error
3. Calling Superclass Constructors
4. Runtime Polymorphism
