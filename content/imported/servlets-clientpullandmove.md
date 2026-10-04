---
title: Client Pull and Move
nav: Client Pull and Move
description: public void doGet(HttpServletRequest req, HttpServletResponse res)
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20071017021314/http://www.java2s.com:80/Code/Java/Servlets/ClientPullandMove.htm
---
```java title=Example.java
import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class ClientPullMove extends HttpServlet {
  static final String NEW_HOST = "http:";
  public void doGet(HttpServletRequest req, HttpServletResponse res)
                               throws ServletException, IOException {
    res.setContentType("text/html");
    PrintWriter out = res.getWriter();
    String newLocation = NEW_HOST + req.getRequestURI();
    res.setHeader("Refresh", "10; URL=" + newLocation);
    out.println("The requested URI has been moved to a different host.<BR>");
    out.println("Its new location is " + newLocation + "<BR>");
    out.println("Your browser will take you there in 10 seconds.");
  }
}
```

1.  Client Post
2.  Client Pull
