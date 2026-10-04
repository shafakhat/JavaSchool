---
title: Context Attributes Servlet
nav: Context Attributes Servlet
description: public void doGet(HttpServletRequest req, HttpServletResponse res)throws ServletException, IOException
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20070501200957/http://www.java2s.com:80/Code/Java/Servlets/ContextAttributesServlet.htm
---
```java title=Example.java
import java.io.PrintWriter;
import java.io.IOException;
import java.util.Date;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
public class SessionTracker2 extends HttpServlet
{
  public void doGet(HttpServletRequest req, HttpServletResponse res)throws ServletException, IOException
  {
    res.setContentType("text/html");
    PrintWriter out = res.getWriter();
    HttpSession session = req.getSession(true);
    Integer totalCount = (Integer) getServletContext().getAttribute("total");
    if (totalCount == null)
    {
      totalCount = new Integer(1);
    }
    else
    {
      totalCount = new Integer(totalCount.intValue() + 1);
    }
    Integer count = (Integer) session.getAttribute("count");
    if (count == null) {
      count = new Integer(1);
    } else {
      count = new Integer(count.intValue() + 1);
    }
    session.setAttribute("count", count);
    getServletContext().setAttribute("total", totalCount);
    out.println("<html><head><title>SessionSnoop</title></head>");
    out.println("<body><h1>Session Details</h1>");
    out.println("You've visited this page " + count + ((count.intValue() == 1) ? " time." : " times.") + "<br/>");
    out.println("Total number of visits: " + totalCount + "<br/>");
    out.println("<h3>Details of this session:</h3>");
    out.println("Session id: " + session.getId() + "<br/>");
    out.println("New session: " + session.isNew() + "<br/>");
    out.println("Timeout: " + session.getMaxInactiveInterval() + "<br/>");
    out.println("Creation time: " + new Date(session.getCreationTime()) + "<br/>");
    out.println("Last access time: " + new Date(session.getLastAccessedTime()) + "<br/>");
    out.println("</body></html>");
  }
}
```

Download: ContextAttributesServlet.zip ( 90 K )
---
Related examples in the same category
3. Context log
4. Context logger
5. Context binder
6. Context accessor
7. Set the context parameters in web.xml
8. Log in ServletContext
