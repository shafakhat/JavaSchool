---
title: Checker Filter
nav: Checker Filter
description: public void init(FilterConfig filterConfig) throws ServletException {
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20061025044342/http://www.java2s.com:80/Code/Java/Servlets/CheckerFilter.htm
---
```java title=Example.java
import java.io.IOException;
import java.util.Enumeration;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
public class CheckFilter implements Filter {
  private FilterConfig config;
  public CheckFilter() {
  }
  public void init(FilterConfig filterConfig) throws ServletException {
    this.config = filterConfig;
  }
  public void doFilter(ServletRequest request, ServletResponse response,
      FilterChain chain) throws IOException, ServletException {
    Enumeration params = request.getParameterNames();
    boolean rejected = false;
    while (params.hasMoreElements()) {
      if (isEmpty(request.getParameter((String) params.nextElement()))) {
        reject(request, response);
        rejected = true;
      }
    }
    if (!rejected)
      chain.doFilter(request, response);
  }// doFilter
  private boolean isEmpty(String param) {
    if (param == null || param.length() < 1) {
      return true;
    }
    return false;
  }
  private void reject(ServletRequest request, ServletResponse response)
      throws IOException, ServletException {
    request.setAttribute("errorMsg",
            "Please make sure to provide a valid value for all of the text fields.");
    Enumeration params = request.getParameterNames();
    String paramN = null;
    while (params.hasMoreElements()) {
      paramN = (String) params.nextElement();
      request.setAttribute(paramN, request.getParameter(paramN));
    }
    RequestDispatcher dispatcher = request
        .getRequestDispatcher("/form.jsp");
    dispatcher.forward(request, response);
  }
  public void destroy() {
    /*
     * called before the Filter instance is removed from service by the web
     * container
     */
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
18. Block Filter
19. Servlet : session filter
20. Parameter Filter
21. HTML filter utility
22. Compression Filter
23. Request Filter
