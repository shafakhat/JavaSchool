---
title: Client Pull
nav: Client Pull
description: public void doGet(HttpServletRequest req, HttpServletResponse res)
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20071017021355/http://www.java2s.com:80/Code/Java/Servlets/ClientPull.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class ClientPull extends HttpServlet {
  public void doGet(HttpServletRequest req, HttpServletResponse res)
                               throws ServletException, IOException {
    res.setContentType("text/plain");
    PrintWriter out = res.getWriter();
    res.setHeader("Refresh", "10");
    out.println(new Date().toString());
  }
}
```

1.  Client Post
2.  Client Pull and Move
