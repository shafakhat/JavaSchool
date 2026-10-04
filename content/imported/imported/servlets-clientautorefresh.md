---
title: Client auto refresh : Java examples (example source code) » Servlets » Redirect
nav: Client auto refresh : Java...
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20060513083511/http://www.java2s.com/Code/Java/Servlets/Clientautorefresh.htm
---
Client auto refresh

```java title=Example.java
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
public class AutoServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    //client browser will request the page every 60 seconds
    HttpSession session = request.getSession();
    Long times = (Long) session.getAttribute("times");
    if (times == null)
      session.setAttribute("times", new Long(0));
    long temp = 1;
    if (times != null)
      temp = (times.longValue()) + 1;
    if (temp < 5)
      response.addHeader("Refresh", "15");
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out.println("<html><head><title>Client Refresh</title></head><body>");
    //More HTML or dynamic content
    out.println("You've viewed this page " + temp + " times.");
    session.setAttribute("times", new Long(temp));
    out.println("</body></html>");
  } //end doGet
}
```

Related examples in the same category
---
1. Redirect to New Location
2. Servlet redirect
3. Servlet: URL redirect
4. Servlet: URL rewrite
