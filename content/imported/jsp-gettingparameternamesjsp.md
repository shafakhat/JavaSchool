---
title: Getting Parameter Names Jsp : Java examples (example source code) » JSP » Form Select
nav: Getting Parameter Names Js...
description: Getting Parameter Names Jsp : Java examples (example source code) » JSP » Form Select
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20060505114321/http://www.java2s.com:80/Code/Java/JSP/GettingParameterNamesJsp.htm
---
Getting Parameter Names Jsp

```java title=Example.java
//File: index.html
<HTML>
    <HEAD>
        <TITLE>Getting Parameter Names</TITLE>
    </HEAD>
    <BODY>
        <H1>Getting Parameter Names<H1>
        <FORM ACTION="formAction.jsp" METHOD="POST">
            <INPUT TYPE="TEXT" NAME="text1">
            <BR>
            <SELECT NAME="select1" SIZE="5" MULTIPLE>
                <OPTION>Option 1</OPTION>
                <OPTION selected>Option 2</OPTION>
                <OPTION>Option 3</OPTION>
                <OPTION>Option 4</OPTION>
                <OPTION>Option 5</OPTION>
            </SELECT>
            <BR>
            <INPUT TYPE="SUBMIT" VALUE="Submit">
        </FORM>
    </BODY>
</HTML>
///////////////////////////////////////////////////////////
//File: formAction.jsp
<HTML>
    <HEAD>
        <TITLE>Reading Parameter Names</TITLE>
    </HEAD>
    <BODY>
        <H1>Reading Parameter Names</H1>
        Parameter Names:
        <BR>
        <% java.util.Enumeration names = request.getParameterNames();
        while(names.hasMoreElements()){
            out.println(names.nextElement() + "<BR>");
        }
        %>
    </BODY>
</HTML>
```

Download: GettingParameterNamesJsp.zip (89 K)
---
Related examples in the same category
1. Submitting Multiple Selection Select Controls
2. Submitting Select Controls
