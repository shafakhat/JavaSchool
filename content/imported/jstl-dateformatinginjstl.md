---
title: Date Formating in JSTL
nav: Date Formating in JSTL
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20060717053431/http://www.java2s.com:80/Code/Java/JSTL/DateFormatinginJSTL.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/fmt" prefix="fmt" %>
<html>
  <head>
    <title>Calendar</title>
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
          <td width="47%">Enter a month(1-12)</td>
          <td width="53%">
            <input type="text" name="month" size="20" />
          </td>
        </tr>
        <tr>
          <td width="47%">Enter a year(i.e. 2002)</td>
          <td width="53%">
            <input type="text" name="year" size="20" />
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
        <fmt:parseDate var="now"
        value="${param.month}/1/${param.year}" type="date"
        dateStyle="short" />
        <tr>
          <td width="100%" colspan="7" bgcolor="#0000FF">
            <p align="center">
              <b>
                <font color="#FFFFFF" size="4">
                  <fmt:formatDate pattern="MMMMM yyyy"
                  value="${now}" />
                </font>
              </b>
            </p>
          </td>
        </tr>
        <fmt:formatDate var="i" pattern="E" value="${now}" />
        <c:choose>
          <c:when test="${i=='Sun'}">
            <c:set var="i" value="1" />
          </c:when>
          <c:when test="${i=='Mon'}">
            <c:set var="i" value="2" />
          </c:when>
          <c:when test="${i=='Tue'}">
            <c:set var="i" value="3" />
          </c:when>
          <c:when test="${i=='Wed'}">
            <c:set var="i" value="4" />
          </c:when>
          <c:when test="${i=='Thu'}">
            <c:set var="i" value="5" />
          </c:when>
          <c:when test="${i=='Fri'}">
            <c:set var="i" value="6" />
          </c:when>
          <c:when test="${i=='Sat'}">
            <c:set var="i" value="7" />
          </c:when>
          <c:otherwise>
            <c:set var="i" value="?" />
          </c:otherwise>
        </c:choose>
        <c:choose>
          <c:when test="${param.month==2}">
            <c:set var="max" value="28" />
            <c:if
            test="${ ((param.year % 4 == 0 && paran.year % 100 != 0) || param.year % 400 == 0) }">
              <c:set var="max" value="29" />
            </c:if>
          </c:when>
          <c:when test="${param.month==4}">
            <c:set var="max" value="30" />
          </c:when>
          <c:when test="${param.month==6}">
            <c:set var="max" value="30" />
          </c:when>
          <c:when test="${param.month==9}">
            <c:set var="max" value="30" />
          </c:when>
          <c:when test="${param.month==11}">
            <c:set var="max" value="30" />
          </c:when>
          <c:otherwise>
            <c:set var="max" value="31" />
          </c:otherwise>
        </c:choose>
        <tr>
          <td width="70">
            <b>
              <center>Sunday</center>
            </b>
          </td>
          <td width="70">
            <b>
              <center>Monday</center>
            </b>
          </td>
          <td width="70">
            <b>
              <center>Tuesday</center>
            </b>
          </td>
          <td width="70">
            <b>
              <center>Wednesday</center>
            </b>
          </td>
          <td width="70">
            <b>
              <center>Thursday</center>
            </b>
          </td>
          <td width="70">
            <b>
              <center>Friday</center>
            </b>
          </td>
          <td width="70">
            <b>
              <center>Saturday</center>
            </b>
          </td>
        </tr>
        <c:set var="d" value="1" />
        <c:set var="d" value="1" />
        <c:forEach var="x" begin="1" end="35">
          <c:if
          test="${(x==1)||(x==8)||(x==15)||(x==22)||(x==29)}">
            </tr><tr>
          </c:if>
          <td>
          <c:if
          test="${ (d<=max) && ((x>7)||(i<=x)) }">
            <c:out value="${d}" />
            <c:set var="d" value="${d+1}" />
          </c:if>
          &#160;
          <br />
          <br />
          <br />
          </td>
        </c:forEach>
      </table>
    </c:if>
  </body>
</html>
```

Download: JSTL-Component-Calendar.zip ( 853 K )
---
Related examples in the same category
1. JSTL Time Zone
2. JSTL Parse Date
3. JSTL Format: Date
4. Format Locale date in JSP
