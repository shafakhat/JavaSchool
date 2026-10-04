---
title: Define welcome files for web application
nav: Define welcome files for w...
description: xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20090719081119/http://www.java2s.com:80/Code/Java/Servlets/Definewelcomefilesforwebapplication.htm
---
Define welcome files for web application

```java title=Example.java
<?xml version="1.0" encoding="UTF-8"?>
<web-app
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
        version="2.5">
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
        <welcome-file>index.jsp</welcome-file>
        <welcome-file>default.html</welcome-file>
        <welcome-file>default.jsp</welcome-file>
    </welcome-file-list>
</web-app>
```

1.  Using Initialization Parameters Servlet
---  ---
2.  Init Param Servlet
3.  Servlet Mapping In Web XML
4.  A WebAppConfig object is a wrapper around a DOM tree for a web.xml file
5.  Parse a web.xml file using the SAX2 API
