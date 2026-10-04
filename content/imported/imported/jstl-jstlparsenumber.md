---
title: JSTL Parse Number
nav: JSTL Parse Number
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20060411085111/http://www.java2s.com:80/Code/Java/JSTL/JSTLParseNumber.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Parse Number</title>
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
          <td width="47%">Enter a number to be parsed:</td>
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
                <c:out value="${param.num}" escapeXml="false" />
                </font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="51%">type="number"</td>
          <td width="49%">     <c:catch var="e">
              <fmt:parseNumber var="i" type="number"
              value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td width="51%">type="currency"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseNumber var="i" type="currency"
              value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td width="51%">type="percent"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseNumber var="i" type="percent"
              value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td width="51%">type="number" integerOnly="true"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseNumber var="i" integerOnly="true"
              type="number" value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
      </table>
    </c:if>
  </body>
</html>
```

Download: JSTL-Parse-Number.zip (852 K)
---
Related examples in the same category
1. JSTL format: number
2. JSTL: Format Percent
