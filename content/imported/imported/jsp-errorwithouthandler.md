---
title: Error without handler
nav: Error without handler
description: <%-- This scriptlet checks a hidden field to see whether or not to throw an exception --%>
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20060713173618/http://www.java2s.com:80/Code/Java/JSP/Errorwithouthandler.htm
---
```java title=Example.java
//File Name: generateErrorNoHandler.jsp
<%-- This scriptlet checks a hidden field to see whether or not to throw an exception --%>
<%
  String hiddenField = request.getParameter("hiddenValue");
  if ( hiddenField.equals("error"))
    throw new java.lang.NullPointerException();
%>
<HTML>
  <HEAD><TITLE>Generate Error</TITLE></HEAD>
  <BODY>
    This page generates an error when you click the button.<P>
    <FORM METHOD="POST" ACTION="generateErrorNoHandler.jsp">
      <INPUT TYPE="HIDDEN" NAME="hiddenValue" VALUE="error">
      <INPUT TYPE="SUBMIT" VALUE="Generate exception!">
    </FORM>
  </BODY>
</HTML>
```

Related examples in the same category
---
1. Simple error testing
2. Jsp Error Bean
3. Using an Error Page Jsp
4. Using the Exception Object in Jsp
5. Building a simple error handling page
6. Deal with the errors
7. JSP Error handler
8. Error Handling: compile error in JSP page
9. JSP error: no such page
10. Page with error in JSP directive and actions
11. JSP error detected
12. Advanced Dynamic Web Content Generation: form error check
