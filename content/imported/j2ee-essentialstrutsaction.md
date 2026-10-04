---
title: Essential Struts Action
nav: Essential Struts Action
description: <logic:notPresent name="org.apache.struts.action.MESSAGE" scope="application">
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20060506000038/http://www.java2s.com:80/Code/Java/J2EE/EssentialStrutsAction.htm
---
Essential Struts Action

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
<h1>A Sample Welcome Page</h1>
<logic:notPresent name="org.apache.struts.action.MESSAGE" scope="application">
  <font color="red">
    ERROR:  Application resources not loaded -- check servlet container
    logs for error messages.
  </font>
</logic:notPresent>
    <html:form action="Data">
          Please click the button:
          <html:submit />
    </html:form>
</body>
</html:html>
//result.jsp
<html>
  <head>
    <title>A Results page</title>
  </head>
  <body>
  <h1>A Sample Results Page</h1>
    <%= request.getAttribute("DATA") %>
  </body>
</html>
package ch02;
import javax.servlet.http.HttpServletRequest;
import org.apache.struts.action.*;
public class DataForm extends ActionForm {
  public ActionErrors validate(ActionMapping mapping,
    HttpServletRequest request) {
    return new ActionErrors();
  }
}
package ch02;
//import ch02.DataForm;
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
    String text = "No worries.";
    String target = new String("success");
    request.setAttribute("DATA", text);
    return (mapping.findForward(target));
  }
}
```

Download: Struts-Essential-Skills-ch02.zip (1437 K)
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
17. A Full Struts Application
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
