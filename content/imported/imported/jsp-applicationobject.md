---
title: Application Object
nav: Application Object
description: This page sets data that can be retrieved by other pages in the application.<P>
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20061018171538/http://www.java2s.com/Code/Java/JSP/ApplicationObject.htm
---
Application Object

```java title=Example.java
//File Name: application_page1.jsp
<%
  String theSharedObject = "JSP is cool";
  application.setAttribute("message", theSharedObject);
%>
<HTML>
  <HEAD>
    <TITLE>Application Object - Page 1</TITLE>
  </HEAD>
  <BODY>
    This page sets data that can be retrieved by other pages in the application.<P>
    Click <a href="application_page2.jsp">here</a> to see this in action.
  </BODY>
</HTML>
//File Name:application_page2.jsp
<%
  // getAttribute() returns a java.lang.Object, so need to cast
  String theSharedObject = (String) application.getAttribute("message");
%>
<HTML>
  <HEAD>
    <TITLE>Application Object - Page 2</TITLE>
  </HEAD>
  <BODY>
    This page retrieves the message that was stored in the <i>application</i> object  by another page.
  <P>
    The message is <b><%= theSharedObject %></b>
  </BODY>
</HTML>
```

Related examples in the same category
---
1. Page directive attributes
2. Set page parameters
3. Set JSP PageContext attributes
4. JSP page scope
