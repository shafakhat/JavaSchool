---
title: JSTL Form Value and ForEach Loop
nav: JSTL Form Value and ForEac...
description: JSTL Form Value and ForEach Loop : Java examples (example source code) » JSTL » Loop
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20060503161918/http://www.java2s.com:80/Code/Java/JSTL/JSTLFormValueandForEachLoop.htm
---
JSTL Form Value and ForEach Loop : Java examples (example source code) » JSTL » Loop

```java title=Example.java
<html>
  <head>
    <title>Page Data Example</title>
  </head>
  <body>
    <table border="1">
      <form method="POST" action="params2.jsp">
        <tr>
          <td width="33%">
            <b>First Name</b>
          </td>
          <td width="73%">
            <input type="text" name="first" size="40" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>Last Name</b>
          </td>
          <td width="73%">
            <input type="text" name="last" size="40" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>Address</b>
          </td>
          <td width="73%">
            <input type="text" name="address" size="40" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>City</b>
          </td>
          <td width="73%">
            <input type="text" name="city" size="20" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>State</b>
          </td>
          <td width="73%">
            <input type="text" name="state" size="20" />
          </td>
        </tr>
        <tr>
          <td width="33%">
            <b>ZIP</b>
          </td>
          <td width="73%">
            <input type="text" name="zip" size="20" />
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <input type="submit" value="Submit" name="action" />
            <input type="reset" value="Reset" name="action" />
          </td>
        </tr>
      </form>
    </table>
  </body>
</html>
/////////////////////////////////////////////////////////////////////////////////////
//File: params2.zip
```

Download: JSTL-FormValue-ForEachLoop.zip (853 K)
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
10. JSTL For Each
11. Count to 10 Example: tracking even and odd
