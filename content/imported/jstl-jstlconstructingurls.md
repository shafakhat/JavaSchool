---
title: JSTL Constructing URLs
nav: JSTL Constructing URLs
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20070706225639/http://www.java2s.com:80/Code/Java/JSTL/JSTLConstructingURLs.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Create a URL</title>
  </head>
  <body>
    <form method="POST">
      <table border="1" cellpadding="0" cellspacing="0"
      style="border-collapse: collapse" bordercolor="#111111"
      width="62%" id="AutoNumber1">
        <tr>
          <td width="100%" colspan="2" bgcolor="#0000FF">
            <p align="center">
              <b>
                <font color="#FFFFFF" size="4">URL
                </font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="47%">Enter a base URL:</td>
          <td width="53%">
            <input type="text" name="url" size="20"
              value="http:"/>
          </td>
        </tr>
        <tr>
          <td width="47%">Eneter a value for parameter "parm1"</td>
          <td width="53%">
            <input type="text" name="parm1" size="20" />
          </td>
        </tr>
        <tr>
          <td width="47%">Eneter a value for parameter "parm2"</td>
          <td width="53%">
            <input type="text" name="parm2" size="20"/>
          </td>
        </tr>
        <tr>
          <td width="47%">Eneter a value for parameter "parm3"</td>
          <td width="53%">
            <input type="text" name="parm3" size="20"/>
          </td>
        </tr>
        <tr>
          <td width="100%" colspan="2">
            <p align="center">
              <input type="submit" value="Submit" name="submit" />
              <input type="reset" value="Reset" name="reset" />
            </p>
          </td>
        </tr>
      </table>
      <p>&#160;</p>
    </form>
    <c:if test="${pageContext.request.method=='POST'}">
      <hr>
      <c:url value="${param.url}" var="url">
        <c:param name="parm1" value="${param.parm1}"/>
        <c:param name="parm2" value="${param.parm2}"/>
        <c:param name="parm3" value="${param.parm3}"/>
      </c:url>
      <br/><b>The resulting URL is:</b>
      <c:out value="${url}"/>
    </c:if>
  </body>
</html>
```

Download: JSTL-Constructing-URLs.zip ( 6,554 K )
---
Related examples in the same category
1. JSTL: generate URL, add parameters to url and display the parameters
