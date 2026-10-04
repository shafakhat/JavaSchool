---
title: JSTL format
nav: JSTL format
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20060411085442/http://www.java2s.com:80/Code/Java/JSTL/JSTLformatnumber.htm
---
JSTL format: number

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Format Number</title>
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
                <font color="#FFFFFF" size="4">Number
                Formatting</font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="47%">Enter a number to be formatted:</td>
          <td width="53%">
            <input type="text" name="num" size="20" />
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
      <table border="1" cellpadding="0" cellspacing="0"
      style="border-collapse: collapse" bordercolor="#111111"
      width="63%" id="AutoNumber2">
        <tr>
          <td width="100%" colspan="2" bgcolor="#0000FF">
            <p align="center">
              <b>
                <font color="#FFFFFF" size="4">Formatting:
                <c:out value="${param.num}" />
                </font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="51%">type="number"</td>
          <td width="49%">
            <fmt:formatNumber type="number" value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="number" maxIntegerDigits="3"</td>
          <td>
            <fmt:formatNumber type="number" maxIntegerDigits="3"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="number" minIntegerDigits="10"</td>
          <td>
            <fmt:formatNumber type="number" minIntegerDigits="10"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="number" maxFractionDigits="3"</td>
          <td>
            <fmt:formatNumber type="number" maxFractionDigits="3"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="number" minFractionDigits="10"</td>
          <td>
            <fmt:formatNumber type="number" minFractionDigits="10"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="number" maxFractionDigits="3"
          groupingUsed="false"</td>
          <td>
            <fmt:formatNumber type="number" maxFractionDigits="3"
            groupingUsed="false" value="${param.num}" />
          </td>
        </tr>
      </table>
    </c:if>
  </body>
</html>
```

Download: JSTL-Format-Number.zip (852 K)
---
Related examples in the same category
1. JSTL Parse Number
2. JSTL: Format Percent
