---
title: JSTL Iteration over tokens
nav: JSTL Iteration over tokens
description: JSTL Iteration over tokens : Java examples (example source code) » JSTL » Collections
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20060513070942/http://www.java2s.com/Code/Java/JSTL/JSTLIterationovertokens.htm
---
JSTL Iteration over tokens : Java examples (example source code) » JSTL » Collections

JSTL Iteration over tokens

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
  <head>
    <title>Updatable Collections</title>
  </head>
  <body>
    <table border="0">
      <form method="post">
        <tr bgcolor="blue">
          <td>
            <p align="center">
              <b>
                <font color="#FFFFFF">Parse for Tokens</font>
              </b>
            </p>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <p align="left">Enter a sentence:
            <br />
            <input width="20" maxwidth="20" name="text"
            size="50" />
            <br />
            &#160;</p>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <p align="center">
              <input type="submit" name="parse" value="Parse" />
            </p>
          </td>
        </tr>
      </form>
    </table>
    <c:if test="${pageContext.request.method=='POST'}">
      <table border="1">
        <c:set var="i" value="1" />
        <c:forTokens items="${param.text}" var="word"
        delims=" ,.?!">
          <c:set var="i" value="${i}" />
          <tr>
            <td>
              <b>Word
              <c:out value="${i}" />
              </b>
            </td>
            <td>
              <c:out value="${word}" />
            </td>
          </tr>
        </c:forTokens>
      </table>
    </c:if>
  </body>
</html>
```

Download: JSTL-Iteration-over-tokens.zip (852 K)
---
Related examples in the same category
1. JSTL Modify a collection
2. String Collection Examples
