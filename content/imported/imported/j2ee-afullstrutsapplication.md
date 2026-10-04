---
title: A Full Struts Application
nav: A Full Struts Application
description: <logic:notPresent name="org.apache.struts.action.MESSAGE" scope="application">
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20060411090202/http://www.java2s.com:80/Code/Java/J2EE/AFullStrutsApplication.htm
---
A Full Struts Application

```java title=Example.java
/*
Title:       Struts : Essential Skills (Essential Skills)
Authors:     Steven Holzner
Publisher:   McGraw-Hill Osborne Media
ISBN:       0072256591
*/
//index.jsp
<%@ taglib uri="/tags/struts-html" prefix="html" %>
<%@ taglib uri="/tags/struts-logic" prefix="logic" %>
<html:html locale="true">
<head>
<title>A Welcome Page</title>
<html:base/>
</head>
<body bgcolor="white">
<logic:notPresent name="org.apache.struts.action.MESSAGE" scope="application">
  <font color="red">
    ERROR:  Application resources not loaded -- check servlet container
    logs for error messages.
  </font>
</logic:notPresent>
    <h1>Reading User Input</h1>
    <html:form action="Data">
          Please type your name: <html:text property="text" />
          <html:submit />
    </html:form>
</body>
</html:html>
//ch03_01.jsp
<%@ taglib uri="/tags/struts-bean" prefix="bean" %>
<%@ taglib uri="/tags/struts-html" prefix="html" %>
<%@ taglib uri="/tags/struts-logic" prefix="logic" %>
<%@ taglib uri="/ch03" prefix="ch03" %>
<HTML>
    <HEAD>
        <TITLE>The Struts Cafe</TITLE>
    </HEAD>
    <BODY>
        <H1>The Struts Cafe</H1>
        <html:errors/>
        <ch03:items/>
        <ch03:toppings/>
        <html:form action="ch03_04.do">
            <TABLE>
                <TR>
                    <TD ALIGN="LEFT" VALIGN="TOP">
                        <bean:message key="toppings"/>
                        <BR>
                        <logic:iterate id="toppings1" name="toppings">
                            <html:multibox property="toppings">
                                <%= toppings1 %>
                            </html:multibox>
                            <%= toppings1 %>
                            <BR>
                        </logic:iterate>
                    </TD>
                    <TD ALIGN="LEFT" VALIGN="TOP">
                        <bean:message key="items"/>
                        <BR>
                        <html:select property="items">
                            <html:options name="items"/>
                        </html:select>
                    </TD>
                </TR>
                <TR>
                    <TD ALIGN="LEFT">
                                    <BR>
                        <bean:message key="email"/>
                        <html:text property="email"/>
                    </TD>
                <TR>
            </TABLE>
                  <BR>
            <html:submit value="Place Your Order!"/>
        </html:form>
    </BODY>
</html>
package ch03;
import ch03.DataForm;
import java.io.IOException;
import javax.servlet.*;
import javax.servlet.http.*;
import org.apache.struts.action.*;
public class DataAction extends Action {
  public ActionForward execute(ActionMapping mapping,
    ActionForm form,
    HttpServletRequest request,
    HttpServletResponse response)
    throws IOException, ServletException {
    String text = null;
    String target = new String("success");
    if ( form != null ) {
      DataForm dataForm = (DataForm)form;
      text = dataForm.getText();
    }
    return (mapping.findForward(target));
  }
}
package ch03;
import javax.servlet.http.HttpServletRequest;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionError;
import org.apache.struts.action.ActionErrors;
public class DataForm extends ActionForm {
  private String text = null;
  public String getText() {
    return (text);
  }
  public void setText(String text) {
    this.text = text;
  }
  public void reset(ActionMapping mapping,
    HttpServletRequest request) {
    this.text = null;
  }
//  public ActionErrors validate(ActionMapping mapping,
//    HttpServletRequest request) {
//    ActionErrors errors = new ActionErrors();
//    if ( (symbol == null ) || (symbol.length() == 0) ) {
//      errors.add("symbol",
//        new ActionError("errors.data.symbol.required"));
//    }
//    return errors;
//  }
}
package ch03;
import java.util.*;
import javax.servlet.jsp.tagext.TagSupport;
public class ch03_02 extends TagSupport
{
    public int doStartTag()
      {
        String[] itemsArray = {"", "Pizza", "Calzone", "Sandwich"};
        pageContext.setAttribute("items", itemsArray);
        return SKIP_BODY;
    }
}
package ch03;
import java.util.*;
import javax.servlet.jsp.tagext.TagSupport;
public class ch03_03 extends TagSupport
{
    public int doStartTag()
      {
        String[] toppingsArray = {"Pepperoni", "Hamburger", "Sausage", "Ham", "Cheese"};
        pageContext.setAttribute("toppings", toppingsArray);
        return SKIP_BODY;
    }
}
package ch03;
import java.io.*;
import java.util.*;
import ch03.ch03_06;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
import org.apache.struts.action.*;
public class ch03_04 extends Action
{
  public ActionForward execute(ActionMapping mapping,
    ActionForm form,
    HttpServletRequest request,
    HttpServletResponse response)
    throws IOException, ServletException {      ActionErrors actionerrors = new ActionErrors();
        ch03_06 orderForm = (ch03_06)form;
        String email = orderForm.getEmail();
        if(email.trim().equals("")) {
            actionerrors.add(ActionErrors.GLOBAL_ERROR, new ActionError("error.noemail"));
        }
        String items = orderForm.getItems();
        if(items.trim().equals("")) {
            actionerrors.add("ActionErrors.GLOBAL_ERROR", new ActionError("error.noitems"));
        }
        String[] toppings = orderForm.getToppings();
        if(toppings == null) {
            actionerrors.add("ActionErrors.GLOBAL_ERROR", new ActionError("error.notoppings"));
        }
        if(actionerrors.size() != 0) {
            saveErrors(request, actionerrors);
            return new ActionForward(mapping.getInput());
        }
        return mapping.findForward("OK");
    }
}
```

Download: Struts-Essential-Skills-ch03.zip (1446 K)
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
18. Struts Creating the View
19. Struts: Creating the Model
20. Struts: Creating the Controller
21. Creating Custom Tags
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
