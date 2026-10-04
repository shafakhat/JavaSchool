---
title: Java JSON Tutorial - JSON Introduction
nav: Java JSON Tutorial - JSON ...
description: JSON stands for JavaScript Object Notation. It is a lightweight, text-based, human-readable data format.
section: Imported - java2s Archive
order: 50042
source: https://www.java2s.com/Tutorials/Java/JSON/index.html
---
JSON stands for JavaScript Object Notation. It is a lightweight, text-based, human-readable data format.

JSON is Language independent.

The JSON format is specified in RFC 4627

The official Internet media type for JSON is application/json. The JSON filename extension is .json.

JSON is often used with JavaScript based application.

JSON format is used for serializing and transmitting data over network.

## JSON Example

The following JSON data shows how to store Books information.

```java title=Example.java
{
    "book": [
    {
       "id":"01",
       "language": "Java",
       "edition": "third",
       "author": "JavaSchool"
    },
    {
       "id":"02",
       "language": "JSON",
       "edition": "second""author": "Jack"
    }]
}
```

## Output JSON

The following code shows how to output JSON format data using Javascript. Save the code as json.htm:

```java title=Example.java
<html>
<head>
<script language="javascript" >
  var object1 = { "language" : "Java", "author"  : "JavaSchool" };
  document.write("<h3>Language = " + object1.language+"</h3>");
  document.write("<h3>Author = " + object1.author+"</h3>");
  var object2 = { "language" : "JSON", "author"  : "Jack" };
  document.write("<br>");
  document.write("<h3>Language = " + object2.language+"</h3>");
  document.write("<h3>Author = " + object2.author+"</h3>");
  document.write("<hr />");
  document.write(object2.language +"<br/> "+ object2.author);
  document.write("<hr />");
</script>
</head>
<body>
</body>
</html>
```

## JSON Comparison with XML

JSON and XML are both human readable, language independent data formats.

XML is more verbose than JSON and used to describe structured data.

JSON supports arrays.

The following JSON specify the company and its name.

```java title=Example.java
{
   "company": "JavaSchool",
   "name": "Java2s"
}
```

Rewrite the above JSON in XML as follows.

```java title=Example.java
<car>
   <company>JavaSchool</company>
   <name>Java2s</name>
</car>
```
