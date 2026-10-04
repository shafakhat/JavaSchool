---
title: Integer Calculations
nav: Integer Calculations
description: Imported from the java2s.com archive: Integer Calculations
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20070319193623/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/IntegerCalculations.htm
---
- The basic operators in calculations +, -, *, and /, and these have the usual meanings: add, subtract, multiply, and divide, respectively.
- Using parentheses in arithmetic calculations to change the sequence of operations.

```java title=Example.java
public class MainClass{
  public static void main(String[] argv){
    int a = (20 - 3) * (3 - 9) / 3;
    int b = 20 - 3 * 3 - 9 / 3;
    System.out.println(a);
    System.out.println(b);
  }
}
```

```java title=Example.java
-34
8
```
