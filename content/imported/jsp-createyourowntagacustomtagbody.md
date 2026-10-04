---
title: Create your own tag
nav: Create your own tag
description: PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20061026203917/http://www.java2s.com/Code/Java/JSP/Createyourowntagacustomtagbody.htm
---
Create your own tag: a custom tag body

```java title=Example.java
///
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
  <!-- this tag manipulates its body content by converting it to upper case
    -->
  <tag>
    <name>bodyContentTag</name>
    <tag-class>com.java2s.BodyContentTag</tag-class>
    <body-content>JSP</body-content>
    <attribute>
      <name>howMany</name>
    </attribute>
  </tag>
</taglib>
//compile the following code into WEB-INF\classes\com\java2s
package com.java2s;
import java.io.IOException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.BodyContent;
import javax.servlet.jsp.tagext.BodyTagSupport;
public class BodyContentTag extends BodyTagSupport
{
  private int iterations, howMany;
  public void setHowMany(int i)
  {
    this.howMany = i;
  }
  public void setBodyContent(BodyContent bc)
  {
    super.setBodyContent(bc);
    System.out.println("BodyContent = '" + bc.getString() + "'");
  }
  public int doAfterBody()
  {
    try
    {
      BodyContent bodyContent = super.getBodyContent();
      String      bodyString  = bodyContent.getString();
      JspWriter   out         = bodyContent.getEnclosingWriter();
      if ( iterations % 2 == 0 )
        out.print(bodyString.toLowerCase());
      else
        out.print(bodyString.toUpperCase());
      iterations++;
      bodyContent.clear(); // empty buffer for next evaluation
    }
    catch (IOException e)
    {
      System.out.println("Error in BodyContentTag.doAfterBody()" + e.getMessage());
      e.printStackTrace();
    } // end of catch
    int retValue = SKIP_BODY;
    if ( iterations < howMany )
      retValue = EVAL_BODY_AGAIN;
    return retValue;
  }
}
// start comcat and load the bodyContent.jsp in browser
<%@ taglib uri="/java2s" prefix="java2s" %>
<html>
  <head>
    <title>A custom tag: body content</title>
  </head>
  <body>
    This page uses a custom tag manipulates its body content.
    Here is its output:
    <ol>
      <java2s:bodyContentTag howMany="3">
        <li>java2s.com</li>
      </java2s:bodyContentTag>
    </ol>
  </body>
</html>
```

Related examples in the same category
---
1. Your own simple JSP tag
2. A custom tag that has neither attributes nor body content.
3. A custom tag: empty with attributes
4. A custom tag: scripting variable
5. Write your own tag
6. Logo Tag
7. A custom tag: empty
8. Tag lifecycle with Attribute
9. A custom tag: iteration
10. JSP Simple Tags
