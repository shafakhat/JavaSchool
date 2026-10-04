---
title: Context logger
nav: Context logger
description: public class ContextLogger implements ServletContextListener {
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20061123214654/http://www.java2s.com:80/Code/Java/Servlets/Contextlogger.htm
---
Context logger

```java title=Example.java
//Log4j from Apache is required
import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import javax.servlet.*;
import javax.servlet.http.*;
public class ContextLogger implements ServletContextListener {
  private Logger log;
  public ContextLogger() {
  }
  public void contextDestroyed(ServletContextEvent sce) {
    String name = sce.getServletContext().getServletContextName();
    //log request of the INFO level
    log.info("ServletContext shut down: " + (name == null ? "" : name));
  }
  public void contextInitialized(ServletContextEvent sce) {
    ServletContext context = sce.getServletContext();
    String realPath = context.getRealPath("/");
    String fileSep = System.getProperty("file.separator");
    if (realPath != null && (!realPath.endsWith(fileSep)))
      realPath = realPath + fileSep;
    //Initialize logger here:
    PropertyConfigurator.configure(realPath + "WEB-INF/classes/"
        + context.getInitParameter("logger-config"));
    log = Logger.getLogger(ContextLogger.class);
    String name = context.getServletContextName();
    //log request about servlet context being initialized
    log.info("ServletContext ready: " + (name == null ? "" : name));
  }
}
```

Related examples in the same category
---
3. Context log
4. Logger without configure file
5. Logger Servlet
6. Another logger servlet
7. Logger new config
8. Servlet: Root logger
9. Session logger
10. LoggerSkel for Servlet
11. Log Filter
12. Log in ServletContext
