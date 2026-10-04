---
title: Block Filter
nav: Block Filter
description: public void init(FilterConfig filterConfig) throws ServletException {
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20061128202409/http://www.java2s.com:80/Code/Java/Servlets/BlockFilter.htm
---
Block Filter

```java title=Example.java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
public class BlockFilter implements Filter {
  private FilterConfig config;
  /** Creates new BlockFilter */
  public BlockFilter() {
  }
  public void init(FilterConfig filterConfig) throws ServletException {
    this.config = filterConfig;
  }
  public void doFilter(ServletRequest request, ServletResponse response,
      FilterChain chain) throws IOException, ServletException {
    HttpServletRequest req = null;
    boolean authenticated = false;
    PrintWriter out = null;
    if (request instanceof HttpServletRequest) {
      req = (HttpServletRequest) request;
      String user = req.getParameter("user");
      authenticated = authenticateUser(user);
    }
    if (authenticated) {
      chain.doFilter(request, response);
    } else {
      response.setContentType("text/html");
      out = response.getWriter();
      out
          .println("<html><head><title>Authentication Response</title></head><body>");
      out.println("<h2>Sorry your authentication attempt failed</h2>");
      out.println("</body></html>");
      out.close();
    }
  }// doFilter
  public void destroy() {
    /*
     * called before the Filter instance is removed from service by the web
     * container
     */
  }
  private boolean authenticateUser(String userName) {
    //authenticate the user using JNDI and a database, for instance
    return false;
  }
}
```

Related examples in the same category
---
1. Filtering page to UTF-8
12. Filter that performs filtering based on comparing the appropriate request
13. JNDI Filter
14. Email JNDI Filter
15. Send filter
16. Log Filter
17. IP Filter
18. Checker Filter
19. Servlet : session filter
20. Parameter Filter
21. HTML filter utility
22. Compression Filter
23. Request Filter
