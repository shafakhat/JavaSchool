---
title: Beans with scriptlet
nav: Beans with scriptlet
description: <head><title>JavaBean usage with scriptlets (1)</title></head>
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20061026215629/http://www.java2s.com/Code/Java/JSP/Beanswithscriptlet.htm
---
Beans with scriptlet

```java title=Example.java
<%@ page import="com.java2s.Book" %>
<%
  Book myBook = (Book) session.getAttribute("myBookBean");
  if ( myBook == null)
  {
    myBook = new Book();
    myBook.setAuthor("Joe");
    session.setAttribute("myBookBean", myBook);
  } // end of if ()
%>
<html>
  <head><title>JavaBean usage with scriptlets (1)</title></head>
  <body>
    This page creates a JavaBean if you don't already have one.<P></P>
    Click <a href="page2_scriptlet.jsp">here</a> to go to a page that retrieves it.
  </body>
</html>
//page2_scriptlet.jsp
<%@ page import="com.java2s.Book" %>
<%
  Book myBook = (Book) session.getAttribute("myBookBean");
%>
<html>
  <head><title>JavaBean usage with scriptlets (2) </title></head>
  <body>
    This page retrieves a JavaBean, and its properties.<P>
    <table border="1">
      <th>JavaBean property</th><th>Value</th>
      <tr><td>id</td>    <td><%= myBookBean.getId()     %></td></tr>
      <tr><td>title</td> <td><%= myBookBean.getTitle()  %></td></tr>
      <tr><td>author</td><td><%= myBookBean.getAuthor() %></td></tr>
      <tr><td>price</td> <td><%= myBookBean.getPrice()  %></td></tr>
    </table>
  </body>
</html>
///JavaBean usage - useBean and setProperty tags
<jsp:useBean id="myBookBean"
             class="com.java2s.Book"
             scope="session">
  <jsp:setProperty name="myBookBean" property="id"     value="42"                      />
  <jsp:setProperty name="myBookBean" property="author" value="Ruth"                    />
  <jsp:setProperty name="myBookBean" property="title"  value="Cookery for accountants" />
  <jsp:setProperty name="myBookBean" property="price"  value="29.99"                   />
</jsp:useBean>
<html>
  <head><title>JavaBean usage - useBean and setProperty tags</title></head>
  <body>
    This page creates a JavaBean if you don't already have one.<P></P>
    Click <a href="useAndSet2.jsp">here</a> to go to a page that retrieves it.
  </body>
</html>
//useAndSet2.jsp
<html>
  <head><title>JavaBean usage - getProperty tag</title></head>
  <body>
    This page retrieves a JavaBean, and its properties.<P>
    <table border="1">
      <th>JavaBean property</th><th>Value</th>
      <tr><td>id</td>    <td><jsp:getProperty name="myBookBean" property="id"     /></td></tr>
      <tr><td>title</td> <td><jsp:getProperty name="myBookBean" property="title"  /></td></tr>
      <tr><td>author</td><td><jsp:getProperty name="myBookBean" property="author" /></td></tr>
      <tr><td>price</td> <td><jsp:getProperty name="myBookBean" property="price"  /></td></tr>
    </table>
  </body>
</html>
```

Related examples in the same category
---
12. Bean property display
13. EL and Complex JavaBeans
14. JSP with Java bean
15. JSP form and Java beans
16. JSP email valid check
17. JSP and Java beans 3
