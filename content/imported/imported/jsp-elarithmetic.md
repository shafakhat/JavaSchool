---
title: EL Arithmetic
nav: EL Arithmetic
description: Imported from the java2s.com archive: EL Arithmetic
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20070428084706/http://www.java2s.com:80/Code/Java/JSP/ELArithmetic.htm
---
EL Arithmetic

```java title=Example.java
<html>
<body>
    <h1>EL Arithmetic</h1>
    <table border="1">
      <tr>
        <td><b>Concept</b></td>
        <td><b>EL Expression</b></td>
        <td><b>Result</b></td>
      </tr>
      <tr>
        <td>Literal</td>
        <td>${'${'}10}</td>
        <td>${10}</td>
      </tr>
      <tr>
        <td>Addition</td>
        <td>${'${'}10 + 10 }</td>
        <td>${10 + 10}</td>
      </tr>
      <tr>
        <td>Subtraction</td>
        <td>${'${'}10 - 10 }</td>
        <td>${10 - 10}</td>
      </tr>
      <tr>
        <td>Multiplication</td>
        <td>${'${'}10 * 10 }</td>
        <td>${10 * 10}</td>
      </tr>
      <tr>
        <td>Division / </td>
        <td>${'${'}10 / 3 }</td>
        <td>${10 / 3}</td>
      </tr>
      <tr>
        <td>Division DIV</td>
        <td>${'${'}10 div 3 }</td>
        <td>${10 div 3}</td>
      </tr>
      <tr>
        <td>Modulus</td>
        <td>${'${'}10 % 10 }</td>
        <td>${10 % 3}</td>
      </tr>
      <tr>
        <td>Modulus</td>
        <td>${'${'}10 mod 10 }</td>
        <td>${10 mod 3}</td>
      </tr>
      <tr>
        <td>Division by Zero</td>
        <td>${'${'}10 / 0 }</td>
        <td>${10 / 0}</td>
      </tr>
      <tr>
        <td>Exponential</td>
        <td>${'${'}2E2}</td>
        <td>${2E2}</td>
      </tr>
      <tr>
        <td>Unary Minus</td>
        <td>${'${'}-10}</td>
        <td>${-10}</td>
      </tr>
    </table>
  </body>
</html>
```

Related examples in the same category
---
1. EL and Complex JavaBeans
2. EL and Complex JavaBeans 1
