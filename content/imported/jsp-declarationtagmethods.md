---
title: Declaration Tag - Methods : Java examples (example source code) » JSP » Basics
nav: Declaration Tag - Methods ...
description: 25. JSP Basics: Dynamic Page Creation for Data Presentation 2
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20060504223838/http://www.java2s.com:80/Code/Java/JSP/DeclarationTagMethods.htm
---
Declaration Tag - Methods

```java title=Example.java
<%!
  private String getName()
  {
    return "Rosy";
  }
  private int getAge()
  {
    return 6;
  }
%>
<HTML>
  <HEAD><TITLE>Declaration Tag - Methods</TITLE></HEAD>
  <%= getName() %>, age <%= getAge() %>, is one funny kid!
</HTML>
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
8. Expression Language Examples
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
