---
title: Form TextField Demo
nav: Form TextField Demo
description: Imported from the java2s.com archive: Form TextField Demo
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20061018174654/http://www.java2s.com/Code/Java/JSP/FormTextFieldDemo.htm
---
Form TextField Demo

```java title=Example.java
//File: index.html
<html>
  <body>
    <h1>Hello Web Application</h1>
    <form action="hello.jsp" method="POST" >
      <table width="75%">
        <tr>
          <td width="48%">What is your name?</td>
          <td width="52%">
            <input type="text" name="name" />
          </td>
        </tr>
      </table>
      <p>
        <input type="submit" name="Submit" value="Submit name" />
        <input type="reset" name="Reset" value="Reset form" />
      </p>
    </form>
  </body>
</html>
//File: hello.jsp
<html>
  <head>
    <title>Hello Web Application</title>
  </head>
  <body>
    <h1>Hello Web Application</h1>
    <br/><br/>
    <%
    String name   = request.getParameter("name");
    if (name.trim().length() == 0) {
    %>
      You did not tell me your name!<br><br><br>
    <%
    } else {
    %>
      Hello <%=name%><br><br><br>
    <%
    }
    %>
    <a href="index.html">Try again?</a>
  </body>
</html>
```

Download: SimpleFormInJsp.zip ( 88 K )
Related examples in the same category
