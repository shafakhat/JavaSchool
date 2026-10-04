---
title: Using the increment and decrement operators in an expression
nav: Using the increment and de...
description: Imported from the java2s.com archive: Using the increment and decrement operators in an expression
section: Imported - java2s Archive
order: 1117
source: https://web.archive.org/web/20140829074857/http://www.java2s.com/Tutorial/Java/0060__Operators/Usingtheincrementanddecrementoperatorsinanexpression.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int numA = 5;
    int numB = 10;
    int numC = 0;
    numC = ++numA + numB;
    System.out.println(numA);
    System.out.println(numC);
  }
}
java title=Example.java
6
16
```
