---
title: Context accessor
nav: Context accessor
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20070111184127/http://www.java2s.com:80/Code/Java/Servlets/Contextaccessor.htm
---
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
public class ContextAccessor extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    //get a servlet context attribute
    ContextObject contextObj = (ContextObject) getServletContext()
        .getAttribute("com.java2s.ContextObject");
    if (contextObj != null)
      contextObj.put(request.getRemoteAddr(), "" + new java.util.Date());
    //display
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out
        .println("<html><head><title>Servlet Context Attribute</title></head><body>");
    if (contextObj != null) {
      out.println("<h2>Servlet Context Attribute Values</h2>");
      out.println(contextObj.getValues());
    } else {
      out.println("<h2>Servlet Context Attribute is Null</h2>");
    }
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
5. Context binder
6. Set the context parameters in web.xml
7. Log in ServletContext
