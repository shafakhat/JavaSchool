---
title: Floating-Point Calculations
nav: Floating-Point Calculations
description: Imported from the java2s.com archive: Floating-Point Calculations
section: Imported - java2s Archive
order: 1157
source: https://web.archive.org/web/20140829075918/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FloatingPointCalculations.htm
---
The four arithmetic operators: +, -, *, /.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
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

| 2.10.1. | Floating-Point Data Types: memory and length |
|---|---|
| 2.10.2. | Write Floating-Point Literals with an exponent |
| 2.10.3. | Floating-Point Calculations |
| 2.10.4. | Using ++ and -- with floating-point variables |
| 2.10.5. | Applying the modulus operator, %, to floating-point values |
