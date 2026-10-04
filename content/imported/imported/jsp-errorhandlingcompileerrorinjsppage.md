---
title: Error Handling
nav: Error Handling
description: public class Java2sTempClassNameBeginningJavaServerPages-ch10-1 {
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20060713174550/http://www.java2s.com:80/Code/Java/JSP/ErrorHandlingcompileerrorinJSPpage.htm
---
Error Handling: compile error in JSP page

```java title=Example.java
/*
Beginning JavaServer Pages
Vivek Chopra, Jon Eaves, Rupert Jones, Sing Li, John T. Bell
ISBN: 0-7645-7485-X
*/
public class Java2sTempClassNameBeginningJavaServerPages-ch10-1 {
<html>
<head>
<title>Error in Scripting Element</title>
</head>
<body>
       <h1>Page with error in scripting element</h1>
<%
int sum= 0;
for { int i=0; i<50; i++ }
  sum = sum + i;
%>
</body>
</html>
```

Download: BeginningJavaServerPages-ch10-1.zip ( 288 K )
---
Related examples in the same category
1. Simple error testing
2. Jsp Error Bean
3. Using an Error Page Jsp
4. Using the Exception Object in Jsp
5. Building a simple error handling page
6. Deal with the errors
7. Error without handler
8. JSP Error handler
9. JSP error: no such page
10. Page with error in JSP directive and actions
11. JSP error detected
12. Advanced Dynamic Web Content Generation: form error check
