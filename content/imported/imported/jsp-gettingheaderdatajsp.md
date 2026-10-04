---
title: Getting Header Data Jsp
nav: Getting Header Data Jsp
description: /////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20070308130935/http://www.java2s.com:80/Code/Java/JSP/GettingHeaderDataJsp.htm
---
Getting Header Data Jsp

```java title=Example.java
//File: index.html
<HTML>
    <HEAD>
        <TITLE>Getting Header Data</TITLE>
    </HEAD>
    <BODY>
        <H1>Getting Header Data</H1>
        <FORM ACTION="formAction.jsp" METHOD="POST">
            <INPUT TYPE="submit" VALUE="Submit">
        </FORM>
    </BODY>
</HTML>
/////////////////////////////////////////////////////////////
//File: formAction.jsp
<HTML>
    <HEAD>
        <TITLE>Reading Header Information</TITLE>
    </HEAD>
    <BODY>
        <H1>Reading Header Information</H1>
        Here are the request headers and their data:
        <BR>
        <% java.util.Enumeration names = request.getHeaderNames();
        while(names.hasMoreElements()){
            String name = (String) names.nextElement();
            out.println(name + ":<BR>" + request.getHeader(name) + "<BR><BR>");
        }
        %>
    </BODY>
</HTML>
```

Download: GettingHeaderDataJsp.zip ( 89 K )
Related examples in the same category
