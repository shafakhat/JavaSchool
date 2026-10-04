---
title: Building a simple error handling page
nav: Building a simple error ha...
description: 12. Advanced Dynamic Web Content Generation: form error check
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20060713173425/http://www.java2s.com:80/Code/Java/JSP/Buildingasimpleerrorhandlingpage.htm
---
```java title=Example.java
<HTML>
    <HEAD>
        <TITLE>Building a simple error handling page.</TITLE>
    </HEAD>
    <BODY>
        <%
            try{
                int value = 1;
                value = value / 0;
            }
            catch (Exception e){
                System.out.println(e.getMessage());
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
5. Deal with the errors
6. Error without handler
7. JSP Error handler
8. Error Handling: compile error in JSP page
9. JSP error: no such page
10. Page with error in JSP directive and actions
11. JSP error detected
12. Advanced Dynamic Web Content Generation: form error check
