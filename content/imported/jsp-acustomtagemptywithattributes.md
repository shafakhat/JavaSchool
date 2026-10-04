---
title: A custom tag
nav: A custom tag
description: PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20061026204005/http://www.java2s.com/Code/Java/JSP/Acustomtagemptywithattributes.htm
---
A custom tag: empty with attributes

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
  <!-- this tag lists random numbers; the HTML is hard-coded within
       the tag handler
    -->
  <tag>
    <name>emptyTagWithAttrs</name>
    <tag-class>com.java2s.EmptyTagWithAttrs</tag-class>
    <body-content>empty</body-content>
    <attribute>
      <name>howMany</name>
    </attribute>
  </tag>
</taglib>
//compile the following code into WEB-INF\classes\com\java2s
package com.java2s;
import java.io.IOException;
import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.TagSupport;
/* This tag handler generates the random numbers. The "howMany" attribute
   specifies how many numbers to generate and display.
 */
public class EmptyTagWithAttrs extends TagSupport
{
  // Code to implement the "howMany" attribute
  private int howMany;
  public int getHowMany()
  {
    return howMany;
  }
  public void setHowMany(int i)
  {
    howMany = i;
  }
  public int doStartTag() throws JspException
  {
    try
    {
      JspWriter out = pageContext.getOut();
      for ( int i=0; i<this.howMany; i++ )
      {
        int nextNumber = (int) (Math.random() * 10);
        out.println("<li>" + nextNumber + "</li>");
      } // end of for ()
    }
    catch (IOException e)
    {
      System.out.println("Error in EmptyTagWithAttrs.doStartTag()");
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
    <title>A custom tag: empty with attributes</title>
  </head>
  <body>
    This page uses a custom tag that has no body content, but takes
    an attribute called "howMany" that specifies how many random
    numbers to generate. Here is its output:
    <ul>
      <java2:emptyTagWithAttrs howMany="5" />
    </ul>
  </body>
</html>
```

Related examples in the same category
---
1. Your own simple JSP tag
2. Create your own tag: a custom tag body
3. A custom tag that has neither attributes nor body content.
4. A custom tag: scripting variable
5. Write your own tag
6. Logo Tag
7. A custom tag: empty
8. Tag lifecycle with Attribute
9. A custom tag: iteration
10. JSP Simple Tags
