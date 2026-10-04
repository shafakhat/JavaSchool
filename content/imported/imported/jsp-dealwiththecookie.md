---
title: Deal with the cookie : Java examples (example source code) » JSP » Cookie
nav: Deal with the cookie : Jav...
description: <strong>Cookie name:</strong> <c:out value="${cookieVal.key}" /><br>
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20060513081038/http://www.java2s.com/Code/Java/JSP/Dealwiththecookie.htm
---
Deal with the cookie

```java title=Example.java
// cookieReader.jsp
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
<body>
<c:choose>
  <c:when test="${empty cookie}" >
  <h2>We did not find any cookies in the request</h2>
  </c:when>
  <c:otherwise>
<h2>The name and value of each found cookie</h2>
<c:forEach var="cookieVal" items="${cookie}">
<strong>Cookie name:</strong> <c:out value="${cookieVal.key}" /><br>
<strong>Cookie value:</strong> <c:out value="${cookieVal.value.value}" /><br><br>
</c:forEach>
</c:otherwise>
</c:choose>
</body>
</html>
// cookieSetter.jsp
<jsp:useBean id="cookieBean" class="com.java2s.CookieBean" />
<jsp:setProperty name="cookieBean" property="name"  value="bakedcookie" />
<jsp:setProperty name="cookieBean" property="maxAge"  value="<%=(365*24*60*60) %>" />
<jsp:setProperty name="cookieBean" property="path"  value="<%= request.getContextPath() %>" />
<jsp:setProperty name="cookieBean" property="cookieHeader"  value="<%= response %>" />
<html>
<head><title>Cookie Maker</title></head>
<body>
<h2>Here is information about the new cookie</h2>
Name: <jsp:getProperty name="cookieBean" property="name" /><br>
Value: <jsp:getProperty name="cookieBean" property="value" /><br>
Path: <jsp:getProperty name="cookieBean" property="path" />
</body>
</html>
// put the class file to WEB-INF/classes/com/java2s
//CookieBean.java
package com.java2s;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;
public class CookieBean {
  private Cookie cookie = null;
  public CookieBean() {
  }
  public void setName(String name) {
    if (name == null || (name.equals("")))
      throw new IllegalArgumentException("Invalid cookie name set in: "
          + getClass().getName());
    cookie = new Cookie(name, "" + new java.util.Date().getTime());
  }
  public void setValue(String value) {
    if (value == null || (value.equals("")))
      throw new IllegalArgumentException("Invalid cookie value set in: "
          + getClass().getName());
    if (cookie != null)
      cookie.setValue(value);
  }
  public void setMaxAge(int maxAge) {
    if (cookie != null)
      cookie.setMaxAge(maxAge);
  }
  public void setPath(String path) {
    if (path == null || (path.equals("")))
      throw new IllegalArgumentException("Invalid cookie path set in: "
          + getClass().getName());
    if (cookie != null)
      cookie.setPath(path);
  }
  public void setCookieHeader(HttpServletResponse response) {
    if (response == null)
      throw new IllegalArgumentException(
          "Invalid HttpServletResponse set in: "
              + getClass().getName());
    if (cookie != null)
      response.addCookie(cookie);
  }
  public String getName() {
    if (cookie != null)
      return cookie.getName();
    else
      return "unavailable";
  }
  public String getValue() {
    if (cookie != null)
      return cookie.getValue();
    else
      return "unavailable";
  }
  public String getPath() {
    if (cookie != null)
      return cookie.getPath();
    else
      return "unavailable";
  }
}
```

Related examples in the same category
---
1. JSP Create and List Cookie
2. JSP List All Cookie
3. Setting a Cookie
4. Setting and Reading Cookies
5. Cookie display in a JSP page
6. JSP: deal with cookie
