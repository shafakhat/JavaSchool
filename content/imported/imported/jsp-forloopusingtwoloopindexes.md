---
title: For loop
nav: For loop
description: Imported from the java2s.com archive: For loop
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20070504031600/http://www.java2s.com:80/Code/Java/JSP/ForloopUsingTwoLoopIndexes.htm
---
For loop: Using Two Loop Indexes

```java title=Example.java
<HTML>
  <HEAD>
    <TITLE>Using Two Loop Indexes</TITLE>
  </HEAD>
  <BODY>
    <H1>Using Two Loop Indexes</H1>
    <%
        for (int i = 0, doubleIndex = 0; i <= 10;
            i++, doubleIndex = 2 * i) {
            out.println("i: " + i +
                " doubleIndex: " + doubleIndex + "<BR>");
        }
    %>
  </BODY>
</HTML>
```

Related examples in the same category
---
1. Using the continue Statement
2. Using the break Statement
3. While statement
4. While: Finding a Factorial
5. Using the while Loop
6. Using the if Statement
7. Testing for Multiple Conditions
8. Using the switch Statement
9. Using an if-else Ladder
10. Nested if Statements
11. Using Compound Statements
