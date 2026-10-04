---
title: JSTL-Form Action And Passing Parameter
nav: JSTL-Form Action And Passi...
description: JSTL-Form Action And Passing Parameter : Java examples (example source code) » JSTL » Form Parameter
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20060513090332/http://www.java2s.com/Code/Java/JSTL/JSTLFormActionAndPassingParameter.htm
---
JSTL-Form Action And Passing Parameter : Java examples (example source code) » JSTL » Form Parameter

JSTL-Form Action And Passing Parameter

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<c:if test="${pageContext.request.method=='POST'}">
  <c:set var="uid" value="${param.uid}" scope="session" />
  <jsp:forward page="session2.jsp" />
</c:if>
<html>
  <head>
  </head>
  <body>
    <form method="POST">
      <table border="1" cellpadding="0" cellspacing="0"
      style="border-collapse: collapse" bordercolor="#111111"
      width="42%" id="AutoNumber1">
        <tr>
          <td width="100%" colspan="2" bgcolor="#0000FF">
            <p align="center">
              <b>
                <font size="4" color="#FFFFFF">Please Login</font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="19%">User Name</td>
          <td width="81%">
            <input type="text" name="uid" size="20" />
          </td>
        </tr>
        <tr>
          <td width="19%">Password</td>
          <td width="81%">
            <input type="password" name="pwd" size="20" />
          </td>
        </tr>
        <tr>
          <td width="100%" colspan="2">
            <p align="center">
              <input type="submit" value="Submit" name="action" />
              <input type="reset" value="Reset" name="B2" />
            </p>
          </td>
        </tr>
      </table>
    </form>
    <p align="left">
      <i>Note: you may use any ID/Password, security is not
      checked.</i>
    </p>
  </body>
</html>
////////////////////////////////////////////////////////////////////////////////////////////
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Session Example</title>
  </head>
  <body>
  <h3>Welcome
  <c:out value="${uid}" />
  </h3>
  Your favorite color is:
  <b>
    <c:out value="${param.color}" />
  </b>
  <br />
  <br />
  Choose your favorite color:
  <br />
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=red">
  red</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=blue">
  blue</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=green">
  green</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=yellow">
  yellow</a>
  <br />
  <a
  href="<c:out value="${pageContext.request.requestURI}"/>?color=other">
  other</a>
  <br />
  </body>
</html>
```

Download: JSTL-FormActionAndPassingParameter.zip (854 K)
---
Related examples in the same category
1. JSTL Form Value and ForEach Loop
2. Property Access
