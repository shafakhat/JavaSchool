---
title: JSTL
nav: JSTL
description: Imported from the java2s.com archive: JSTL
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20060307045706/http://www.java2s.com:80/Code/Java/JSTL/JSTLparseXMLdocument.htm
---
JSTL: parse XML document

```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jstl/xml"  prefix="x" %>
<html>
  <head>
    <title>xml actions</title>
  </head>
  <body>
    This example parses XML and uses an XPath expression...
    <p/>
    <c:set var="someXML">
      <people>
        <person>
          <name>Joe</name>
          <age>30</age>
        </person>
        <person>
          <name>Rosy</name>
          <age>29</age>
        </person>
      </people>
    </c:set>
    <x:parse var="parsedDocument" xml="${someXML}" />
    Here is a list of people:
    <ul>
      <x:forEach select="$parsedDocument/people/person">
        <li> <x:out select="name" /> </li>
      </x:forEach>
    </ul>
  </body>
</html>
```

Related examples in the same category
---
1. JSTL XML Foreach
2. JSTL XML Map Value
3. JSTL XML Output
4. JSTL XML Parse
5. JSTL XML XPath
6. JSTL XML XPath Choose
7. JSTL XML XPath Select
8. JSTL XML XPath: Wired New
