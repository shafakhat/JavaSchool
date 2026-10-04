---
title: Java Algorithms How to - Parse a mathematical expression and operators and solve it
nav: Java Algorithms How to - P...
description: We would like to know how to parse a mathematical expression and operators and solve it.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20160731162408/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Parse_a_mathematical_expression_and_operators_and_solve_it.htm
---
```java title=Example.java
Back to Math  ↑
```

## Question

We would like to know how to parse a mathematical expression and operators and solve it.

## Answer

```java title=Example.java
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String xyz = "3*3+3";
    String kkk = "(100 % 6)* 7";
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine se = manager.getEngineByName("JavaScript");
    Object result1 = se.eval(xyz);
    Object result2 = se.eval(kkk);
    System.out.println("result1: " + result1);
    System.out.println("result2: " + result2);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Math  ↑
```
