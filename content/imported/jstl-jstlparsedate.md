---
title: JSTL Parse Date
nav: JSTL Parse Date
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20060717051120/http://www.java2s.com:80/Code/Java/JSTL/JSTLParseDate.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Parse Date</title>
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
                <font color="#FFFFFF" size="4">Date
                Formatting</font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="47%">Enter a date to be parsed:</td>
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
                <c:out value="${param.num}"  escapeXml="false" />
                </font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td width="51%">type="date" dateStyle="short"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseDate var="i" type="date" dateStyle="short"
              value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td width="51%">type="date" dateStyle="medium"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseDate var="i" type="date" dateStyle="medium"
              value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td width="51%">type="date" dateStyle="long"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseDate var="i" type="date" dateStyle="long"
              value="${param.num}" />
              <c:out value="${i}"  escapeXml="false" />
            </c:catch>
            <c:out value="${e}"  escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td width="51%">type="date" dateStyle="full"</td>
          <td width="49%">
            <c:catch var="e">
              <fmt:parseDate var="i" type="date" dateStyle="full"
              value="${param.num}" />
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

Download: JSTL-Parse-Date.zip ( 852 K )
---
Related examples in the same category
1. JSTL Time Zone
2. JSTL Format: Date
3. Date Formating in JSTL
4. Format Locale date in JSP
