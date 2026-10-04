---
title: File
nav: File
description: Imported from the java2s.com archive: File
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20070111182850/http://www.java2s.com:80/Code/Java/JSP/FileTheGuestBook.htm
---
File: The Guest Book

```java title=Example.java
<%@ page import="java.io.*" %>
<HTML>
    <HEAD>
        <TITLE>The Guest Book</TITLE>
    </HEAD>
    <BODY>
        <H1>The Guest Book</H1>
        Here are the current entries in the guest book:
        <BR>
        <BR>
        <%
            String file = application.getRealPath("/") + "test.txt";
            File fileObject = new File(file);
            char data[] = new char[(int) fileObject.length()];
            FileReader filereader = new FileReader(file);
            int charsread = filereader.read(data);
            out.println(new String(data, 0 , charsread));
            filereader.close();
        %>
    </BODY>
</HTML>
```

Related examples in the same category
