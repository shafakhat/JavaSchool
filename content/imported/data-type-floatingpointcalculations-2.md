---
title: Floating-Point Calculations
nav: Floating-Point Calculations
description: Imported from the java2s.com archive: Floating-Point Calculations
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FloatingPointCalculations.htm
---
The four arithmetic operators: +, -, *, /.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    double numA = 50.0E-1;   // 5.0
double numB = 1.0E1;     // 10.0
double averageC = 0.0;
    averageC = (numA + numB) / 2.0;
    System.out.println(averageC);
  }
}
java title=Example.java
7.5
```
