---
title: Change Bean Property
nav: Change Bean Property
description: //This example is from Jakub Czeczotka <jakub.czeczotka at gmail.com>
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20071018111850/http://java2s.com:80/Code/Java/J2EE/ChangeBeanProperty.htm
---
Change Bean Property

```java title=Example.java
//This example is from Jakub Czeczotka <jakub.czeczotka at gmail.com>
//web.xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app id="WebApp_ID" version="2.4" xmlns="http://java.sun.com/xml/ns/j2ee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
    <display-name>
  ChangeBeanProperty
    </display-name>
    <description>
  Change a property of a simple bean
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
  <managed-bean-name>simpleBean</managed-bean-name>
  <managed-bean-class>eu.czeczotka.SimpleBean</managed-bean-class>
  <managed-bean-scope>session</managed-bean-scope>
    </managed-bean>
</faces-config>
//SimpleBean.java
package eu.czeczotka;
import java.util.logging.Logger;
/**
 * Simple bean for the ChangeBeanProperty project
 *
 * @author Jakub Czeczotka
 */
public class SimpleBean {
    private Logger logger = Logger.getLogger ("eu.czeczotka.SimpleBean");
    private String property = "initial value";
    public String getProperty () {
  return this.property;
    }
    public void setProperty (String property) {
  logger.info ("changing property value from \"" +
    this.property + "\" to \"" + property + "\"");
  this.property = property;
    }
}
//index.jsp
<% response.sendRedirect("changeBeanProperty.jsf"); %>
//changeBeanProperty.jsp
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f" %>
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h" %>
<%-- ChangeBeanProperty - author Jakub Czeczotka --%>
<html>
<head>
    <title>ChangeBeanProperty</title>
</head>
<body>
    <f:view>
  <h:form>
      <h3>Change a property of a simple bean</h3><br />
      <h:inputText value="#{simpleBean.property}" />
      <h:commandButton type="submit" value="change value" action="#" />
  </h:form>
    </f:view>
</body>
</html>
```

ChangeBeanProperty.zip( 2,264 k)
1.  Hello World JSF
2.  JavaServer Faces

www___.j___a__va___2___s.___c_om_
