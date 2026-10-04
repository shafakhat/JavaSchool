---
title: JSTL Submit Form TextField Action
nav: JSTL Submit Form TextField...
description: ///////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20061027011451/http://www.java2s.com/Code/Java/JSTL/JSTLSubmitFormTextFieldAction.htm
---
```java title=Example.java
<html>
  <head>
    <title>Page Data Example</title>
  </head>
  <body>
    <table border="1">
      <form method="POST" action="params2.jsp">
        <tr>
          <td width="33%">
            <b>First Name</b>
          </td>
          <td width="73%">
            <input type="text" name="first" size="40" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>Last Name</b>
          </td>
          <td width="73%">
            <input type="text" name="last" size="40" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>Address</b>
          </td>
          <td width="73%">
            <input type="text" name="address" size="40" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>City</b>
          </td>
          <td width="73%">
            <input type="text" name="city" size="20" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>State</b>
          </td>
          <td width="73%">
            <input type="text" name="state" size="20" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>ZIP</b>
          </td>
          <td width="73%">
            <input type="text" name="zip" size="20" />
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <input type="submit" value="Submit" name="action" />
            <input type="reset" value="Reset" name="action" />
          </td>
        </tr>
      </form>
    </table>
  </body>
</html>
///////////////////////////////////////////////////////////////////////////
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Page Data Example</title>
  </head>
  <body>
    <table border="1" width="310">
      <tr>
        <td bgcolor="#0000FF" width="98">
          <b>
            <font color="#FFFFFF" size="4">Name</font>
          </b>
        </td>
        <td bgcolor="#0000FF" width="196">
          <b>
            <font color="#FFFFFF" size="4">Value</font>
          </b>
        </td>
      </tr>
      <c:forEach var="aItem" items="${paramValues}">
        <tr>
          <td width="98">
            <b>
              <c:out value="${aItem.key}" />
            </b>
          </td>
          <td width="196">&#160;
          <c:forEach var="aValue" items="${aItem.value}">
            <c:out value="${aValue}" />
          </c:forEach>
          </td>
        </tr>
      </c:forEach>
    </table>
  </body>
</html>
```

Download: JSTL-SubmitFormTextFieldAction.zip ( 853 K )
Related examples in the same category
