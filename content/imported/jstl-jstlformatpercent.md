---
title: JSTL
nav: JSTL
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20060505114346/http://www.java2s.com:80/Code/Java/JSTL/JSTLFormatPercent.htm
---
JSTL: Format Percent

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Format Percent</title>
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
          <td width="47%">Enter a percent to be formatted:</td>
          <td width="53%">
            <input type="text" name="num" size="20" />
          </td></tr>
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
          <td width="51%">type="percent"</td>
          <td width="49%">
            <fmt:formatNumber type="percent"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="percent" maxIntegerDigits="3"</td>
          <td>
            <fmt:formatNumber type="percent" maxIntegerDigits="3"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="percent" minIntegerDigits="10"</td>
          <td>
            <fmt:formatNumber type="percent" minIntegerDigits="10"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="percent" maxFractionDigits="3"</td>
          <td>
            <fmt:formatNumber type="percent" maxFractionDigits="3"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="percent" minFractionDigits="10"</td>
          <td>
            <fmt:formatNumber type="percent" minFractionDigits="10"
            value="${param.num}" />
          </td>
        </tr>
        <tr>
          <td>type="percent" maxFractionDigits="3"
          groupingUsed="false"</td>
          <td>
            <fmt:formatNumber type="percent" maxFractionDigits="3"
            groupingUsed="false" value="${param.num}" />
          </td>
        </tr>
      </table>
    </c:if>
  </body>
</html>
```

Download: JSTL-Format-Percent.zip (852 K)
---
Related examples in the same category
1. JSTL Parse Number
2. JSTL format: number
