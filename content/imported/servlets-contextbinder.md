---
title: Context binder
nav: Context binder
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20070111183334/http://www.java2s.com:80/Code/Java/Servlets/Contextbinder.htm
---
Context binder

```java title=Example.java
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class ContextBinder extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    //bind an object to the servlet context
    getServletContext().setAttribute("com.java2s.ContextObject",
        new ContextObject());
    //better display something
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out
        .println("<html><head><title>Servlet Context Attribute</title></head><body>");
    out.println("<h2>Servlet Context Attribute Bound</h2>");
    out.println("Object: "
        + getServletContext().getAttribute("com.java2s.ContextObject"));
    out.println("</body></html>");
  } //end doGet
}
//ContextObject.java
class ContextObject {
  private Map map;
  public ContextObject() {
    map = Collections.synchronizedMap(new HashMap());
  }
  public void put(Object key, Object value) {
    if (key == null || value == null)
      throw new IllegalArgumentException(
          "Invalid parameters passed to ContextObject.put");
    map.put(key, value);
  }
  public Map getMap() {
    return map;
  }
  public String getValues() {
    StringBuffer buf = new StringBuffer("");
    Set set = map.keySet();
    synchronized (map) {
      Iterator i = set.iterator();
      while (i.hasNext())
        buf.append((String) i.next() + "<br>");
    }
    return buf.toString();
  }
  public String toString() {
    return getClass().getName() + "[ " + map + " ]";
  }
}
```

Related examples in the same category
---
3. Context log
4. Context logger
5. Context accessor
6. Set the context parameters in web.xml
7. Log in ServletContext
