---
title: A custom tag
nav: A custom tag
description: PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN"
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20061026204011/http://www.java2s.com/Code/Java/JSP/Acustomtagscriptingvariable.htm
---
A custom tag: scripting variable

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
  <!-- this tag lists random numbers; the HTML is hard-coded within
       the tag handler
    -->
  <!-- this tag exports random numbers in a named array -->
  <tag>
    <name>defineObjects</name>
    <tag-class>com.conygre.jspdevhandbook.chapter9.EmptyTagWithAttrsExport</tag-class>
    <tei-class>com.conygre.jspdevhandbook.chapter9.EmptyTagExtraInfo</tei-class>
    <body-content>empty</body-content>
    <!--
         Use this block instead of a TEI class
    <variable>
      <name-from-attribute>name</name-from-attribute>
      <variable-class>int []</variable-class>
      <declare>TRUE</declare>
      <scope>AT_END</scope>
    </variable>
    -->
    <attribute>
      <name>howMany</name>
    </attribute>
    <attribute>
      <name>name</name>
    </attribute>
  </tag>
</taglib>
//compile the following code into WEB-INF\classes\com\java2s
package com.java2s;
import javax.servlet.jsp.tagext.TagData;
import javax.servlet.jsp.tagext.TagExtraInfo;
import javax.servlet.jsp.tagext.VariableInfo;
public class EmptyTagExtraInfo extends TagExtraInfo
{
  public VariableInfo[] getVariableInfo(TagData tagData)
  {
    String exportedArrayName = (String) tagData.getAttribute("name");
    VariableInfo exportedArrayInfo = new VariableInfo(exportedArrayName,
                                                      "int []",
                                                      true,
                                                      VariableInfo.AT_END);
    return new VariableInfo[] {exportedArrayInfo};
  }
}
package com.java2s;
import javax.servlet.jsp.*;
import javax.servlet.jsp.tagext.*;
/* This tag handler generates the random numbers. The "howMany" attribute
   specifies how many number to generate and display. The generated array
   of integers is exported with nested visibility, through an array named
   byte the "name" attribute.
 */
public class EmptyTagWithAttrsExport extends BodyTagSupport
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
  // Code to implement the "name" attribute
  private String exportedArrayName;
  public String getName()
  {
    return exportedArrayName;
  }
  public void setName(String s)
  {
    exportedArrayName = s;
  }
  public int doStartTag() throws JspException
  {
    int[] outputArray = new int[howMany];
    System.out.println("Generating " + howMany + " numbers");
    for ( int i=0; i<howMany; i++ )
    {
      outputArray[i] = (int) (Math.random() * 10);
    } // end of for ()
    pageContext.setAttribute(exportedArrayName, outputArray);
    return SKIP_BODY;
  }
  /*  public int doEndTag() throws JspException
  {
    return super.doEndTag();
  }*/
}
// start comcat and load the following jsp page in browser
<%@ taglib uri="/java2s" prefix="java2s" %>
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>A custom tag: scripting variable</title>
  </head>
  <body>
    output:
    <java2s:defineObjects howMany="5" name="numbers" />
    <ul>
      <c:forEach items="${numbers}" var="currentNumber">
        <li>
          <c:out value="${currentNumber}" />
        </li>
      </c:forEach>
    </ul>
  </body>
</html>
```

Related examples in the same category
---
1. Your own simple JSP tag
2. Create your own tag: a custom tag body
3. A custom tag that has neither attributes nor body content.
4. A custom tag: empty with attributes
5. Write your own tag
6. Logo Tag
7. A custom tag: empty
8. Tag lifecycle with Attribute
9. A custom tag: iteration
10. JSP Simple Tags
