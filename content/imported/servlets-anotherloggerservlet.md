---
title: Another logger servlet
nav: Another logger servlet
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20061104062930/http://www.java2s.com:80/Code/Java/Servlets/Anotherloggerservlet.htm
---
```java title=Example.java
//Log4j from Apache is required
import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import javax.servlet.*;
import javax.servlet.http.*;
public class LoggerServlet2 extends HttpServlet {
  private Logger log = null;
  public void init() {
    log = Logger.getLogger(LoggerServlet2.class);
  }
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    //display a DEBUG level message
    log.debug("Sending a DEBUG message from logger2");
    //display an INFO level message
    log.info("Sending an INFO message from logger2");
    //better display something
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out.println("<html><head><title>Servlet logging</title></head><body>");
    out.println("<h2>Hello from LoggerServlet</h2>");
    out.println("Your logger name is: " + log.getName() + "<br>");
    out.println("Your logger parent is: " + log.getParent().getName()
        + "<br>");
    out.println("</body></html>");
    out.close();
  } //end doGet
  public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    doGet(request, response);
  }
}
```

Related examples in the same category
---
3. Context log
4. Logger without configure file
5. Logger Servlet
6. Logger new config
7. Servlet: Root logger
8. Session logger
9. LoggerSkel for Servlet
10. Context logger
11. Log Filter
12. Log in ServletContext
