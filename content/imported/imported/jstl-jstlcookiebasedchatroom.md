---
title: JSTL Cookie based Chat Room
nav: JSTL Cookie based Chat Room
description: <%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20060715205909/http://www.java2s.com:80/Code/Java/JSTL/JSTLCookiebasedChatRoom.htm
---
JSTL Cookie based Chat Room

```java title=Example.java
//File: chat.jsp
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/core-rt" prefix="c-rt" %>
<c:if test="${pageContext.request.method=='POST'}">
<%
  Cookie mycookie = new Cookie("login",request.getParameter("uid"));
  mycookie.setMaxAge(0x7ffffff);
  response.addCookie(mycookie);
%>
  <c:redirect url="main.jsp">
    <c:param name="uid" value="${param.uid}"/>
  </c:redirect>
</c:if>
<html>
  <head>
    <meta http-equiv="Content-Language" content="en-us" />
    <title>Simple Chat with Cookie</title>
  </head>
  <body>
    <c-rt:forEach var="aCookie" items="<%=request.getCookies()%>">
      <c:if test="${aCookie.name=='login'}">
        <c:set var="uid" value="${aCookie.value}"/>
      </c:if>
    </c-rt:forEach>
    <form method="post">
      <table border="1" cellpadding="0" cellspacing="0"
      style="border-collapse: collapse" bordercolor="#111111"
      width="33%" id="AutoNumber1">
        <tbody>
          <tr>
            <td width="100%" colspan="2" bgcolor="#0000FF">
              <p align="center">
                <b>
                  <font size="4" color="#FFFFFF">Chat Login</font>
                </b>
              </p>
            </td>
          </tr>
          <tr>
            <td width="23%">User ID</td>
            <td width="77%">
              <input type="text" name="uid" value="<c:out value="${uid}"/>" size="20" />
            </td>
          </tr>
          <tr>
            <td width="100%" colspan="2">
              <p align="center">
                <input type="submit" value="Submit"
                name="action" />
                <input type="reset" value="Reset" />
              </p>
            </td>
          </tr>
        </tbody>
      </table>
      <p>&#160;</p>
    </form>
    <p>
      <i>Note: You may use any User ID you wish</i>
    </p>
  </body>
</html>
//File: main.jsp
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Chat Joined</title>
  </head>
  <body>
    <c:if test="${pageContext.request.method=='POST'}">
      <c:choose>
        <c:when test="${param.send!=null}">
          <c:set var="chat"
          value="${chat}<b>${param.uid}:</b>${param.text}<br />"
           scope="application" />
        </c:when>
        <c:when test="${param.clear!=null}">
          <c:set var="chat" value="" scope="application" />
        </c:when>
      </c:choose>
    </c:if>
    <table border="0">
      <tbody>
        <tr>
          <td>
            <h3>User:
            <c:out value="${param.uid}" />
            </h3>
            <hr />
          </td>
        </tr>
        <tr>
          <td>
            <c:out value="${chat}" escapeXml="false" />
          </td>
        </tr>
        <tr>
          <td>
            <hr />
            <form method="post">Message:
            <input type="text" name="text" size="20" />
            <input type="submit" name="send" value="Send" />
            <input type="submit" name="refresh" value="Refresh" />
            <input type="submit" name="clear" value="Clear" />
            <input type="hidden" name="uid"
            value="<c:out value="${param.uid}"/>" />
            <br />
            </form>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
```

Download: JSTL-Chat-Cookie-JSTL-Redirect.zip ( 855 K )
---
Related examples in the same category
1. Small Application: Game
2. Simple Chat Application
