---
title: Literals
nav: Literals
description: Imported from the java2s.com archive: Literals
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/20070716200929/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Literals.htm
---
```java title=Example.java
public class MainClass {
  char c = 0xffff; // max char hex value
  byte b = 0x7f; // max byte hex value
  short s = 0x7fff; // max short hex value
  int i1 = 0x2f; // Hexadecimal (lowercase)
  int i2 = 0X2F; // Hexadecimal (uppercase)
  int i3 = 0177; // Octal (leading zero)
  // Hex and Oct also work with long.
  long n1 = 200L; // long suffix
  long n2 = 200l; // long suffix (but can be confusing)
  long n3 = 200;
  // ! long l6(200); // not allowed
  float f1 = 1;
  float f2 = 1F; // float suffix
  float f3 = 1f; // float suffix
  float f4 = 1e-45f; // 10 to the power
  float f5 = 1e+9f; // float suffix
  double d1 = 1d; // double suffix
  double d2 = 1D; // double suffix
  double d3 = 47e47d; // 10 to the power
}
```
