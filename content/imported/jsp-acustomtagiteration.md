---
title: A custom tag
nav: A custom tag
description: PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20061026203547/http://www.java2s.com/Code/Java/JSP/Acustomtagiteration.htm
---
A custom tag: iteration

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
  <!-- this tag iterates over its body a number of times -->
  <tag>
    <name>iterationTag</name>
    <tag-class>com.java2s.IterationTag</tag-class>
    <body-content>JSP</body-content>
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
/* This tag iterates a number of times, as specified by
   its "howMany" attribute.
 */
public class IterationTag extends TagSupport
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
    return EVAL_BODY_INCLUDE;
  }
  private int countIterations = 0;
  public int doAfterBody() throws JspException
  {
    int retValue = (countIterations >= (howMany - 1)) ? SKIP_BODY
                                                      : EVAL_BODY_AGAIN;
    try
    {
      JspWriter out = pageContext.getOut();
      if ( countIterations < howMany)
      {
        int nextNumber = (int) (Math.random() * 10);
        out.println(nextNumber + "<br />");
      }
    }
    catch (IOException e)
    {
      System.out.println("Error in IterateTag.doAfterBody()");
      e.printStackTrace();
      throw new JspException(e); // throw the error to the error page (if set)
    } // end of try-catch
    countIterations++;
    return retValue;
  } // end of doAfterBody()
} // end of class IterationTag
// start comcat and load the following jsp page in browser
<%@ taglib uri="/java2s" prefix="java2" %>
<html>
  <head>
    <title>A custom tag: iteration</title>
  </head>
  <body>
    output: <p />
    <java2s:iterationTag howMany="5">
      Here is a random number:
    </java2s:iterationTag>
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
8. A custom tag: empty
9. Tag lifecycle with Attribute
10. JSP Simple Tags
