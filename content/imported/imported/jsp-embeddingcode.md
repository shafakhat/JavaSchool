---
title: Embedding Code
nav: Embedding Code
description: Imported from the java2s.com archive: Embedding Code
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20070119000732/http://www.java2s.com:80/Code/Java/JSP/EmbeddingCode.htm
---
```java title=Example.java
<%!
  String[] names = {"Green", "White", "Black", "Red"};
%>
<HTML>
  <HEAD><TITLE>Embedding Code</TITLE></HEAD>
  <BODY>
    <H1>List of people</H1>
    <TABLE BORDER="1">
      <TH>Name</TH>
      <% for (int i=0; i<names.length; i++) { %>
        <TR><TD><%= names[i]%></TD></TR>
      <% } %>
    </TABLE>
  </BODY>
</HTML>
```

Related examples in the same category
---
2. Simplest Jsp page: A Web Page
3. Output: Creating a Greeting
5. Simple JSP page to display the random number
6. Comments in JSP page
7. Declaration Tag Example
8. Declaration Tag - Methods
9. Expression Language Examples
10. Passing parameters
11. JSP Initialization
12. Welcome page and top level URL
13. JSP Expression Language
14. JSP without beans
15. Request header display in a JSP
16. Multiple Declaration
17. pwd -- print working directory
18. JSP post
19. JSP Post Data Viewer
