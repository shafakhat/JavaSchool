---
title: JSTL For Each
nav: JSTL For Each
description: <%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/xml" prefix="x" %>
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20060503161859/http://www.java2s.com:80/Code/Java/JSTL/JSTLforeach.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %><%@ taglib uri="http://java.sun.com/jstl/xml" prefix="x" %>
<html>
  <head>
    <title>Reading RSS</title>
  </head>
  <body>
    <c:import var="news"
    url="http://www.wired.com/news_drop/netcenter/netcenter.rdf" />
    <x:parse var="doc" xml="${news}" />
    <table border="1" width="100%">
      <tr bgcolor="blue">
        <td align="center">
          <font color="white" size="+2">
            <b>
              <x:out select="$doc/rss/channel/title" />
            </b>
          </font>
          <br />
          <font color="white" size="-2">
            <x:out select="$doc/rss/channel/pubDate" />
          </font>
        </td>
      </tr>
      <tr>
        <td valign="top">
          <x:out select="$doc/rss/channel/description" />
        </td>
      </tr>
      <x:forEach var="story" select="$doc/rss/channel/item">
        <tr bgcolor="blue">
          <td align="center">
            <a href="&lt;x:out select=">"&gt;
            <font color="white">
              <x:out select="title" />
            </font>
            </a>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <x:out select="description" />
          </td>
        </tr>
      </x:forEach>
    </table>
  </body>
</html>
```

Download: JSTL-ForEach.zip (6552 K)
---
Related examples in the same category
1. JSTL: Conditional Support -- Simple Conditional Execution Example
2. JSTL Tag collaboration with a fixed loop
3. JSTL: fortokens
4. JSTL: another for each and status
5. JSTL: for each and status
6. JSTL: for each and scoped variable
7. JSTL: for each loop
8. JSTL: for each
9. Count to 10 Example using JSTL
10. Count to 10 Example: tracking even and odd
11. JSTL Form Value and ForEach Loop
