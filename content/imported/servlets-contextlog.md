---
title: Context log
nav: Context log
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20061123214040/http://www.java2s.com:80/Code/Java/Servlets/Contextlog.htm
---
Context log

```java title=Example.java
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class ContextLog extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    String yourMessage = request.getParameter("mine");
    //Call the two ServletContext.log methods
    //the javax.servlet.GenericServlet.getServletContext method
    ServletContext context = getServletContext();
    if (yourMessage == null || yourMessage.equals(""))
      //log version with Throwable parameter
      context.log("No message received:", new IllegalStateException(
          "Missing parameter"));
    else
      context.log("Here is the visitor's message: " + yourMessage);
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    //logging servlets probably want to display more HTML; this is 'lazy
    // HTML'
    out.println("<html><head><title>ServletContext logging</title></head><body>");
    out.println("<h2>Messages sent</h2>");
    out.println("</body></html>");
  } //end doGet
}
```

Related examples in the same category
---
3. Logger without configure file
4. Logger Servlet
5. Another logger servlet
6. Logger new config
7. Servlet: Root logger
8. Session logger
9. LoggerSkel for Servlet
10. Context logger
11. Log Filter
12. Log in ServletContext
