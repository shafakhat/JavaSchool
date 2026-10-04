---
title: A custom tag
nav: A custom tag
description: PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20061026203950/http://www.java2s.com/Code/Java/JSP/Acustomtagempty.htm
---
A custom tag: empty

```java title=Example.java
  <!-- this must be added to the web application's web.xml -->
<taglib>
  <taglib-uri>/java2s</taglib-uri>
  <taglib-location>/WEB-INF/java2s.tld</taglib-location>
</taglib>
// create File:java2s.tld in the /WEB-INF/
<!DOCTYPE taglib
  PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
   "http://java.sun.com/dtd/web-jsptaglibrary_1_2.dtd">
    <!-- a tab library descriptor -->
<taglib xmlns="http://java.sun.com/JSP/TagLibraryDescriptor">
  <tlib-version>1.0</tlib-version>
  <jsp-version>1.2</jsp-version>
  <short-name>Java2s Simple Tags</short-name>
  <!-- a tag that outputs information when different methods are called -->
  <tag>
    <name>tagLifecycle</name>
    <tag-class>com.java2s.TagLifecycle</tag-class>
    <body-content>empty</body-content>
    <attribute>
      <name>attr1</name>
    </attribute>
    <attribute>
      <name>attr2</name>
    </attribute>
  </tag>
</taglib>
//compile the following code into WEB-INF\classes\com\java2s
package com.java2s;
import java.io.IOException;
import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.PageContext;
import javax.servlet.jsp.tagext.Tag;
import javax.servlet.jsp.tagext.TagSupport;
/* This tag handler outputs information about when different methods
   are called.
 */
public class Lifecycle extends TagSupport
{
  // Constructor
  public Lifecycle()
  {
    System.out.println("constructor called");
  }
  // Methods inherited from TagSupport
  public void setPageContext(PageContext p)
  {
    super.setPageContext(p);
    System.out.println("setPageContext() called");
  }
  public void setParent(Tag t)
  {
    super.setParent(t);
    System.out.println("setParent() called");
  }
  public void release()
  {
    System.out.println("release() called");
  }
  // Code to implement the "attr1" attribute
  private String attr1;
  public String getAttr1()
  {
    return attr1;
  }
  public void setAttr1(String s)
  {
    System.out.println("setAttr1() called with value " + s);
    attr1 = s;
  }
  // Code to implement the "attr2" attribute
  private String attr2;
  public String getAttr2()
  {
    return attr2;
  }
  public void setAttr2(String s)
  {
    System.out.println("setAttr2() called with value " + s);
    attr2 = s;
  }
  public int doStartTag() throws JspException
  {
    System.out.println("doStartTag() called");
    return SKIP_BODY;
  }
  public int doEndTag() throws JspException
  {
    System.out.println("doEndTag() called");
    return super.doEndTag();
  }
}
// start comcat and load the following jsp page in browser
<%@ taglib uri="/java2s" prefix="java2s" %>
<html>
  <head>
    <title>A custom tag: empty</title>
  </head>
  <body>
    <java2s:tagLifecycle attr1="Rob" attr2="G" />
    <java2s:tagLifecycle attr1="Joe" attr2="S" />
    Check your Tomcat console window for the output
  </body>
</html>
```

Related examples in the same category
---
1. Your own simple JSP tag
2. Create your own tag: a custom tag body
3. A custom tag that has neither attributes nor body content.
4. A custom tag: empty with attributes
5. A custom tag: scripting variable
6. Write your own tag
7. Logo Tag
8. Tag lifecycle with Attribute
9. A custom tag: iteration
10. JSP Simple Tags
