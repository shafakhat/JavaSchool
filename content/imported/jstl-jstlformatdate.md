---
title: JSTL Format
nav: JSTL Format
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %><%@ taglib uri="http://java.sun.com/jstl/fmt
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20060702055654/http://www.java2s.com:80/Code/Java/JSTL/JSTLFormatDate.htm
---
JSTL Format: Date

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Format Date</title>
  </head>
  <body>
    <c-rt:set var="now" value="<%=new java.util.Date()%>" />
    <table border="1" cellpadding="0" cellspacing="0"
    style="border-collapse: collapse" bordercolor="#111111"
    width="63%" id="AutoNumber2">
      <tr>
        <td width="100%" colspan="2" bgcolor="#0000FF">
          <p align="center"> <b>
              <font color="#FFFFFF" size="4">Formatting:
              <fmt:formatDate value="${now}" type="both"
              timeStyle="long" dateStyle="long" />
              </font>
            </b>
          </p>
        </td>
      </tr>
      <tr>
        <td width="51%">formatDate type="time"</td>
        <td width="49%">
          <fmt:formatDate type="time" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="date"</td>
        <td width="49%">
          <fmt:formatDate type="date" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="both"</td>
        <td width="49%">
          <fmt:formatDate type="both" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="both" dateStyle="default"
        timeStyle="default"</td>
        <td width="49%">
          <fmt:formatDate type="both" dateStyle="default"
          timeStyle="default" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="both" dateStyle="short"
        timeStyle="short"</td>
        <td width="49%">
          <fmt:formatDate type="both" dateStyle="short"
          timeStyle="short" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="both" dateStyle="medium"
        timeStyle="medium"</td>
        <td width="49%">
          <fmt:formatDate type="both" dateStyle="medium"
          timeStyle="medium" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="both" dateStyle="long"
        timeStyle="long"</td>
        <td width="49%">
          <fmt:formatDate type="both" dateStyle="long"
          timeStyle="long" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">type="both" dateStyle="full"
        timeStyle="full"</td>
        <td width="49%">
          <fmt:formatDate type="both" dateStyle="full"
          timeStyle="full" value="${now}" />
        </td>
      </tr>
      <tr>
        <td width="51%">pattern="yyyy-MM-dd"</td>
        <td width="49%">
          <fmt:formatDate pattern="yyyy-MM-dd" value="${now}" />
        </td>
      </tr>
    </table>
  </body>
</html>
```

Download: JSTL-Format-Date.zip (852 K)
---
Related examples in the same category
1. JSTL Time Zone
2. JSTL Parse Date
3. Date Formating in JSTL
4. Format Locale date in JSP
