---
title: Deal with the errors
nav: Deal with the errors
description: <%-- After clicking the button, it will call itself again the generate error --%>
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20060713173642/http://www.java2s.com:80/Code/Java/JSP/Dealwiththeerrors.htm
---
```java title=Example.java
// generateError.jsp
<%@ page errorPage="processError.jsp" %>
<%-- Declare the page to send errors to --%>
<%-- After clicking the button, it will call itself again the generate error --%>
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
    <FORM METHOD="POST" ACTION="generateError.jsp">
      <INPUT TYPE="HIDDEN" NAME="hiddenValue" VALUE="error">
      <INPUT TYPE="SUBMIT" VALUE="Generate exception!">
    </FORM>
  </BODY>
</HTML>
//Another JSP file: processError.jsp
<%@ page isErrorPage="true" %>
<HTML>
  <HEAD><TITLE> Process Error</TITLE></HEAD>
  <BODY>
    <% if ( exception != null ) {
         out.write("\nAn error occurred. This page is to tell you what you did wrong.\n");
       }
       else {
         out.write("\nYou have reached this page, but no error information is available.\n");
       }
    %>
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
6. Error without handler
7. JSP Error handler
8. Error Handling: compile error in JSP page
9. JSP error: no such page
10. Page with error in JSP directive and actions
11. JSP error detected
12. Advanced Dynamic Web Content Generation: form error check
