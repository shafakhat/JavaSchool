---
title: Basic Form processor : Java examples (example source code) » Servlets » Form
nav: Basic Form processor : Jav...
description: xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd" version="2.4">
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20051218124707/http://www.java2s.com:80/Code/Java/Servlets/BasicFormprocessor.htm
---
Basic Form processor

```java title=Example.java
/*
<?xml version="1.0" encoding="ISO-8859-1"?>
<web-app xmlns="http://java.sun.com/xml/ns/j2ee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee       http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd" version="2.4">
  <servlet>
    <servlet-name>BasicFormProcessor</servlet-name>
    <servlet-class>BasicFormProcessor</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>BasicFormProcessor</servlet-name>
    <url-pattern>/formProcessor</url-pattern>
  </servlet-mapping>
</web-app>
*/
import java.io.IOException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class BasicFormProcessor extends HttpServlet {
  public void doPost(HttpServletRequest req, HttpServletResponse res)
      throws IOException {
    ServletOutputStream out = res.getOutputStream();
    res.setContentType("text/html");
    out
        .println("<html><head><title>Basic Form Processor Output</title></head>");
    out.println("<body>");
    out.println("<h1>Here is your Form Data</h1>");
    //extract the form data here
    String title = req.getParameter("title");
    String name = req.getParameter("name");
    String city = req.getParameter("city");
    String country = req.getParameter("country");
    String tel = req.getParameter("tel");
    String age = req.getParameter("age");
    // extracting data from the checkbox field
    String[] interests = req.getParameterValues("interests");
    //output the data into a web page
    out.println("Your title is " + title);
    out.println("<br>Your name is " + name);
    out.println("<br>Your city is " + city);
    out.println("<br>Your country is " + country);
    out.println("<br>Your tel is " + tel);
    out.println("<br>Your interests include<ul> ");
    for (int i = 0; i < interests.length; i++) {
      out.println("<li>" + interests[i]);
    }
    out.println("</ul>");
    out.println("<br>Your age is " + age);
    out.println("</body></html>");
  }
}
```

Related examples in the same category
---
1. React to user form input
2. feedback Form
