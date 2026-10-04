---
title: EL and Complex JavaBeans 1
nav: EL and Complex JavaBeans 1
description: <jsp:useBean id="person" class="com.java2s.Person" scope="request" />
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20070428132819/http://www.java2s.com:80/Code/Java/JSP/ELandComplexJavaBeans1.htm
---
EL and Complex JavaBeans 1

```java title=Example.java
<jsp:useBean id="person" class="com.java2s.Person" scope="request" />
<html>
<body>
    <h1>EL and Complex JavaBeans</h1>
    <table border="1">
      <tr>
        <td>${person.name}</td>
        <td>${person.age}</td>
        <td>${person["address"].line1}</td>
        <td>${person["address"].town}</td>
        <td>${person.address.phoneNumbers[0].std} ${person.address.phoneNumbers[0].number}</td>
        <td>${person.address.phoneNumbers[1].std} ${person.address.phoneNumbers[1].number}</td>
      </tr>
    </table>
  </body>
</html>
```

Related examples in the same category
---
1. EL and Complex JavaBeans
2. EL Arithmetic
