---
title: A custom tag that has neither attributes nor body content.
nav: A custom tag that has neit...
description: PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20061026203506/http://www.java2s.com/Code/Java/JSP/Acustomtagthathasneitherattributesnorbodycontent.htm
---
```java title=Example.java
/// Empty Tag
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
  <!-- this tag just outputs some text -->
  <tag>
    <name>emptyTag</name>
    <tag-class>com.java2s.EmptyTag</tag-class>
    <body-content>empty</body-content>
  </tag>
</taglib>
//compile the following code into WEB-INF\classes\com\java2s
package com.java2s;
import java.io.IOException;
import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.TagSupport;
public class EmptyTag extends TagSupport
{
  public int doStartTag() throws JspException
  {
    try
    {
      pageContext.getOut().print("in EmptyTag.doStartTag()");
    }
    catch (IOException e)
    {
      System.out.println("Error in EmptyTag.doStartTag()");
      e.printStackTrace();
      throw new JspException(e); // throw the error to the error page (if set)
    } // end of try-catch
    return SKIP_BODY;
  }
}
// start comcat and load the following jsp page in browser
<%@ taglib uri="/java2s" prefix="java2s" %>
<html>
  <head>
    <title>A custom tag: empty</title>
  </head>
  <body>
    This page uses a custom tag that has neither attributes nor body content.
    Here is its output:
    <h1><java2s:emptyTag /></h1>
  </body>
</html>
```

Related examples in the same category
---
1. Your own simple JSP tag
2. Create your own tag: a custom tag body
3. A custom tag: empty with attributes
4. A custom tag: scripting variable
5. Write your own tag
6. Logo Tag
7. A custom tag: empty
8. Tag lifecycle with Attribute
9. A custom tag: iteration
10. JSP Simple Tags
