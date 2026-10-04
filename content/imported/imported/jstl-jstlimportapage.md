---
title: JSTL
nav: JSTL
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20060513085155/http://www.java2s.com/Code/Java/JSTL/JSTLImportaPage.htm
---
JSTL: Import a Page

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Import a Page</title>
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
                <font color="#FFFFFF" size="4">Import
                </font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="47%">Enter a site to import:</td>
          <td width="53%">
            <input type="text" name="url" size="20"
              value="http://www.java2s.com"/>
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
      <c:import url="${param.url}"/>
    </c:if>
  </body>
</html>
```

Download: JSTL-Importing-Data.zip (852 K)
Related examples in the same category
