---
title: Expression Language Examples : Java examples (example source code) » JSP » Basics
nav: Expression Language Exampl...
description: Expression Language Examples : Java examples (example source code) » JSP » Basics
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20060504224048/http://www.java2s.com:80/Code/Java/JSP/ExpressionLanguageExamples.htm
---
Expression Language Examples : Java examples (example source code) » JSP » Basics

Expression Language Examples

```java title=Example.java
<html>
<head>
<title><!-- be aware that this listing will not work
in Tomcat 4.1, or any other container that does
not support the use of the expression language outside
of tags -->
<html>
<head>
<title>Expression Language Examples</title>
<%
  // set up a page context parameter for use later in the page
  // normally this would have been set within the context of
  // an application
  pageContext.setAttribute("pageColor", "blue");
%>
</head>
<body bgcolor="${pageScope.pageColor}">
<h1>Welcome to the ${param.department} Department</h1>
Here are some basic comparisons:
<p>
Is 1 less than 2? ${1<2} <br>
Does 5 equal 5? ${5==5} <br>
Is 6 greater than 7? ${6 gt 7}<br>
<p>Now for some math:<br>
6 + 7 = ${6+7}<br>
8 x 9 = ${8*9}<br>
<hr>You appear to be using the following browser:
${header["user-agent"]}
</body>
</html></title>
```

Related examples in the same category
---
1. JSP Passing Parameters
2. Simplest Jsp page: A Web Page
3. Output: Creating a Greeting
4. Simple JSP output
5. Simple JSP page to display the random number
6. Comments in JSP page
7. Declaration Tag Example
8. Declaration Tag - Methods
9. Passing parameters
10. JSP Initialization
11. Welcome page and top level URL
12. JSP Expression Language
13. JSP without beans
14. Request header display in a JSP
15. Multiple Declaration
16. Embedding Code
17. pwd -- print working directory
18. JSP post
19. JSP Post Data Viewer
20. JSP in J2EE
21. JSP Performance
22. JSP Best Practices and Tools
23. JSP Model 2
24. JSP: expression language 2
25. JSP Basics: Dynamic Page Creation for Data Presentation 2
26. JSP Directives: your page
27. JSP Directives
28. JSP Basics ch02
29. JSP Basics: Generalized Templating and Server Scripting 1
30. JSP Basics: Generalized Templating and Server Scripting 2
31. JSP Basics: Generalized Templating and Server Scripting 3
32. CSS, JavaScript, VBScript, and JSP 1
33. CSS, JavaScript, VBScript, and JSP 2
34. Advanced Dynamic Web Content Generation. 1
