---
title: Creating Custom Tags
nav: Creating Custom Tags
description: <h2>Using &lt;logic:empty name="ch07_03" property="empty"&gt;</h2>
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20060506000105/http://www.java2s.com:80/Code/Java/J2EE/CreatingCustomTags.htm
---
Creating Custom Tags

```java title=Example.java
/*
Title:       Struts : Essential Skills (Essential Skills)
Authors:     Steven Holzner
Publisher:   McGraw-Hill Osborne Media
ISBN:       0072256591
*/
//ch07_01.jsp
<%@ taglib uri="/tags/struts-html" prefix="html" %>
<%@ taglib uri="/tags/struts-logic" prefix="logic" %>
<html:html>
    <head>
        <title>Using &lt;logic&gt; Tags</title>
    </head>
    <body>
        <h1>Using &lt;logic&gt; Tags</h1>
        <html:form action="ch07_02.do">
            <h2>Enter your data:</h2>
            <html:text property="text"/>
            <br>
            <br>
            <html:submit value="Submit"/>
            <html:cancel/>
        </html:form>
    </body>
</html:html>
//ch07_04.jsp
<%@ taglib uri="/tags/struts-bean" prefix="bean" %>
<%@ taglib uri="/tags/struts-logic" prefix="logic" %>
<HTML>
    <HEAD>
        <TITLE>Here's Your Data...</TITLE>
    </HEAD>
    <BODY>
        <H1>Here's Your Data...</H1>
        <h2>The text field text:</h2>
        <bean:write name="ch07_03" property="text"/>
        <BR>
        <h2>Using &lt;logic:empty name="ch07_03" property="empty"&gt;</h2>
        <logic:empty name="ch07_03" property="empty">
        Results: Empty
        </logic:empty>
        <BR>
        <h2>Using &lt;logic:notEmpty name="ch07_03" property="text"&gt;</h2>
        <logic:notEmpty name="ch07_03" property="text">
        Results: Not empty
        </logic:notEmpty>
        <BR>
        <h2>Using &lt;logic:equal name="ch07_03" property="number" value="6"&gt;</h2>
        <logic:equal name="ch07_03" property="number" value="6">
        Results: Equal
        </logic:equal>
        <BR>
        <h2>Using &lt;logic:notEqual&gt; name="ch07_03" property="number" value="7"</h2>
        <logic:notEqual name="ch07_03" property="number" value="7">
        Results: Not equal
        </logic:notEqual>
        <BR>
        <h2>Using &lt;logic:greaterEqual name="ch07_03" property="number" value="3"&gt;</h2>
        <logic:greaterEqual name="ch07_03" property="number" value="3">
        Results: Greater than or equal
        </logic:greaterEqual>
        <BR>
        <h2>Using &lt;logic:greaterThan name="ch07_03" property="number" value="4"&gt;</h2>
        <logic:greaterThan name="ch07_03" property="number" value="4">
        Results: Greater than
        </logic:greaterThan>
        <BR>
        <h2>Using &lt;logic:lessEqual name="ch07_03" property="number" value="8"&gt;</h2>
        <logic:lessEqual name="ch07_03" property="number" value="8">
        Results: Less than or equal
        </logic:lessEqual>
        <BR>
        <h2>Using &lt;logic:lessThan name="ch07_03" property="number" value="8"&gt;</h2>
        <logic:lessThan name="ch07_03" property="number" value="8">
        Results: Less than
        </logic:lessThan>
        <BR>
        <h2>Using &lt;logic:match name="ch07_03" property="text" value="6"&gt;</h2>
        <logic:match name="ch07_03" property="text" value="6">
        Results: Matched
        </logic:match>
        <BR>
        <h2>Using &lt;logic:notMatch name="ch07_03" property="number" value="9"&gt;</h2>
        <logic:notMatch name="ch07_03" property="number" value="9">
        Results: No match
        </logic:notMatch>
        <BR>
        <h2>Using &lt;logic:present name="ch07_03" property="number"&gt;</h2>
        <logic:present name="ch07_03" property="number">
        Results: Present
        </logic:present>
        <BR>
        <h2>Using &lt;logic:notPresent name="ch07_03" property="fish"&gt;</h2>
        <logic:notPresent name="ch07_03" property="fish">
        Results: Not present
        </logic:notPresent>
        <BR>
    </BODY>
</HTML>
//ch07_05.jsp
<%@ taglib uri="/tags/struts-html" prefix="html" %>
<html:html>
    <head>
        <title>Using &lt;bean&gt; Tags</title>
    </head>
    <body>
        <h1>Using &lt;bean&gt; Tags</h1>
        <%
        Cookie cookie1 = new Cookie("message", "Hello!");
        cookie1.setMaxAge(24 * 60 * 60);
        response.addCookie(cookie1);
        %>
        <html:form action="ch07_06.do">
            <h2>Enter your data:</h2>
            <html:text property="text"/>
            <br>
            <br>
            <html:submit value="Submit"/>
            <html:cancel/>
        </html:form>
    </body>
</html:html>
//ch07_08.jsp
<%@ page import="ch07.ch07_07" %>
<%@ taglib uri="/tags/struts-bean" prefix="bean" %>
<%@ taglib uri="/tags/struts-logic" prefix="logic" %>
<HTML>
    <HEAD>
        <TITLE>Here's Your Data...</TITLE>
    </HEAD>
    <BODY>
        <H1>Here's Your Data...</H1>
        <h2>The text field text:</h2>
        <bean:write name="ch07_07" property="text"/>
        <BR>
        <h2>The cookie data:</h2>
        <bean:cookie id="messageCookie" name="message"/>
        <%= messageCookie.getValue() %>
        <BR>
        <h2>The new variable:</h2>
        <bean:define id="variable" name="ch07_07" property="text"/>
        <%= variable %>
        <BR>
        <h2>The user-agent header data:</h2>
        <bean:header id="headerObject" name="user-agent"/>
        <%= headerObject %>
        <BR>
        <h2>The parameter data:</h2>
        <bean:parameter id="text" name="text"/>
        <%= text %>
        <BR>
        <h2>The mapping data:</h2>
        <bean:struts id="mapping" mapping="/ch07_06"/>
        <% String[] a = mapping.findForwards();
        out.println(a[0]); %>
        <BR>
    </BODY>
</html>
package ch07;
import org.apache.struts.action.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class ch07_03 extends ActionForm
{
    private String empty = "";
    private String text = "";
    private int number;
    public String getEmpty()
    {
        return empty;
    }
    public void setEmpty(String text)
    {
    }
    public String getText()
    {
        return text;
    }
    public void setText(String text)
    {
        this.text = text;
        this.number = Integer.parseInt(text);
    }
    public int getNumber()
    {
        return number;
    }
    public void setNumber(int number)
    {
        this.number = number;
    }
}
package ch07;
import java.io.*;
import java.util.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
import org.apache.struts.action.*;
public class ch07_06 extends Action
{
  public ActionForward execute(ActionMapping mapping,
    ActionForm form,
    HttpServletRequest request,
    HttpServletResponse response)
    throws IOException, ServletException {
        return mapping.findForward("success");
    }
}
package ch07;
import org.apache.struts.action.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class ch07_07 extends ActionForm
{
    private String text = "";
    public String getText()
    {
        return text;
    }
    public void setText(String text)
    {
        this.text = text;
    }
}
package ch07;
import java.io.*;
import java.util.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
import org.apache.struts.action.*;
public class ch07_02 extends Action
{
  public ActionForward execute(ActionMapping mapping,
    ActionForm form,
    HttpServletRequest request,
    HttpServletResponse response)
    throws IOException, ServletException {
        return mapping.findForward("success");
    }
}
```

Download: Struts-Essential-Skills-ch07.zip (1456 K)
---
Related examples in the same category
1. Exercise 1: Building your first Struts Application
2. Exercise 2: Improving your first Struts Application
3. Exercise 3: Using JSTL, Struts-EL etc
4. Struts Recipes: Build Struts with Ant
5. Using bean:resource to expose the struts.config.xml to your view
6. Create a pluggable validator for cross-form validation 2
7. Struts: Generate a response with XSL
8. Hibernate and Struts
9. In-container testing with StrutsTestCase and Cactus
10. Exercise 4: Applying Gof and J2EE Patterns:Deploy to WebLogic and Test
11. Exercise 5: Search, List, Action Chaining, Editable List Form
12. Exercise 6: Paging
13. Exercise 7: Better Form and Action Handling
14. Exercise 8: Creating Struts Modules
15. Exercise 9: Using Commons Validator with Struts
16. Exercise 10: Using Struts and Tiles
17. Essential Struts Action
18. A Full Struts Application
19. Struts Creating the View
20. Struts: Creating the Model
21. Struts: Creating the Controller
22. The Struts Tags
23. The Struts and Tags
24. Web Services and the Validator and Tile Packages
25. Struts Framework: A Sample Struts Application
26. Struts Framework Validator
27. Struts Framework: Tiles
28. Struts Framework: Declarative Exception Handling
29. Struts: Internationalizing Struts Applications
30. Securing Struts Applications
31. Testing Struts Applications
32. Struts example
33. Blank Struts template
34. Struts Framework
35. Struts: bank application
36. Struts application
37. Struts application 2
