---
title: Cookie : Java examples (example source code) » Servlets » Cookie
nav: Cookie : Java examples (ex...
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20060208022547/http://www.java2s.com:80/Code/Java/Servlets/Cookie.htm
---
Cookie

```java title=Example.java
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class CookieServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    Cookie cookie = null;
    Cookie[] cookies = request.getCookies();
    boolean newCookie = false;
    if (cookies != null) {
      for (int i = 0; i < cookies.length; i++) {
        if (cookies[i].getName().equals("mycookie")) {
          cookie = cookies[i];
        }
      }
    }
    if (cookie == null) {
      newCookie = true;
      int maxAge;
      try {
        maxAge = new Integer(getServletContext().getInitParameter(
            "cookie-age")).intValue();
      } catch (Exception e) {
        maxAge = -1;
      }
      cookie = new Cookie("mycookie", "" + getNextCookieValue());
      cookie.setPath(request.getContextPath());
      cookie.setMaxAge(maxAge);
      response.addCookie(cookie);
    }
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Cookie info</title>");
    out.println("</head>");
    out.println("<body>");
    out
        .println("<h2> Information about the cookie named \"mycookie\"</h2>");
    out.println("Cookie value: " + cookie.getValue() + "<br>");
    if (newCookie) {
      out.println("Cookie Max-Age: " + cookie.getMaxAge() + "<br>");
      out.println("Cookie Path: " + cookie.getPath() + "<br>");
    }
    out.println("</body>");
    out.println("</html>");
    out.close();
  }
  private long getNextCookieValue() {
    return new java.util.Date().getTime();
  }
  public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    doGet(request, response);
  }
}
```

Related examples in the same category
---
1. Setting and Reading Cookies
2. Cookie reader
3. Example servlet showing request headers
