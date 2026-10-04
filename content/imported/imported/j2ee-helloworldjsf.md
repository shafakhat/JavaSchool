---
title: Hello World JSF
nav: Hello World JSF
description: //This example is from Jakub Czeczotka <jakub.czeczotka at gmail.com>
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20071018112447/http://java2s.com:80/Code/Java/J2EE/HelloWorldJSF.htm
---
```java title=Example.java
//This example is from Jakub Czeczotka <jakub.czeczotka at gmail.com>
//web.xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app id="WebApp_ID" version="2.4" xmlns="http://java.sun.com/xml/ns/j2ee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
    <display-name>
    </display-name>
    <description>
  Hello in the JavaServer Faces World!
    </description>
    <listener>
        <listener-class>
      org.apache.myfaces.webapp.StartupServletContextListener
  </listener-class>
    </listener>
    <servlet>
  <servlet-name>Faces Servlet</servlet-name>
  <servlet-class>javax.faces.webapp.FacesServlet</servlet-class>
  <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
  <servlet-name>Faces Servlet</servlet-name>
  <url-pattern>*.jsf</url-pattern>
    </servlet-mapping>
    <welcome-file-list>
  <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>
</web-app>
//faces-config.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE faces-config PUBLIC "-//Sun Microsystems, Inc.//DTD JavaServer Faces Config 1.1//EN"
                              "http://java.sun.com/dtd/web-facesconfig_1_1.dtd">
<faces-config>
    <managed-bean>
  <managed-bean-name>helloWorldBean</managed-bean-name>
  <managed-bean-class>eu.czeczotka.HelloWorldBean</managed-bean-class>
  <managed-bean-scope>session</managed-bean-scope>
    </managed-bean>
</faces-config>
//HelloWorldBean.java
package eu.czeczotka;
/**
 * Sample bean for the HelloWorldJSF project
 *
 * @author Jakub Czeczotka
 */
public class HelloWorldBean {
    private String hello = "Hello in the JavaServer Faces World!";
    public String getHello () {
  return this.hello;
    }
}
//helloworld.jsp
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f" %>
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h" %>
<%-- HelloWorldJSF - author Jakub Czeczotka --%>
<html>
<head>
    <title>HelloWorldJSF</title>
</head>
<body>
    <f:view>
  <h:form>
      <h3>
    <h:outputText value="#{helloWorldBean.hello}" />
      </h3>
  </h:form>
    </f:view>
</body>
</html>
//index.jsp
<% response.sendRedirect("helloworld.jsf"); %>
```

HelloWorldJSF.zip( 2,263 k)
1.  Change Bean Property
2.  JavaServer Faces

w__w___w.j_a___v_a_2s___.___c__o__m
