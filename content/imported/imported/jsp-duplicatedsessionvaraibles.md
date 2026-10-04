---
title: Duplicated session varaibles : Java examples (example source code) » JSP » Session
nav: Duplicated session varaibl...
description: Duplicated session varaibles : Java examples (example source code) » JSP » Session
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20060428120329/http://www.java2s.com:80/Code/Java/JSP/Duplicatedsessionvaraibles.htm
---
Duplicated session varaibles

```java title=Example.java
<jsp:useBean id="myBookBean"   class="com.java2s.Book"
             scope="session">
  <%-- The setProperty tag is only executed when a JavaBean is created --%>
  <jsp:setProperty name="myBookBean" property="author" value="Joe" />
</jsp:useBean>
<html>
  <head>
    <title>When a JavaBean already exists...</title>
  </head>
  <body>
    The author of your book is <jsp:getProperty name="myBookBean"
                                                property="author" /><P>
    Click <a href="beanAlreadyExists2.jsp">here</a> to see another page that
    declares a JavaBean that uses the same name and scope.
  </body>
</html>
//beanAlreadyExists2.jsp
<jsp:useBean id="myBookBean"   class="com.java2s.Book"
             scope="session" />
<html>
  <head>
    <title>When a JavaBean already exists...</title>
  </head>
  <body>
    This page redeclares the JavaBean, but does not set any of its properties.
    The same name and scope were used for the JavaBean, so the original bean
    is used.
    <P>
    The author of your book is <jsp:getProperty name="myBookBean"
                                                property="author" /><P>
  </body>
</html>
```

Related examples in the same category
---
1. JSP: display a session info
2. JSP Session Parameter Rewrite
3. JSP New Session Parameter
4. Jsp Session Cart
5. Use Session Jsp
6. Jsp Using Bean Scope Session
7. Print the request headers and the session attributes
8. Using Sessions to Track Users
9. Sessions disabled
10. JSP: display a session info
11. JSP: view session
12. JSP and session
13. JSP and session 2
14. JSP session counter
