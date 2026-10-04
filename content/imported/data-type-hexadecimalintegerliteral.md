---
title: Hexadecimal integer literal
nav: Hexadecimal integer literal
description: Put 0x or 0X in front of the numbers. Use the letters A to F (or a to f) to represent digits with values 10 to 15, respectively.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20140829091126/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Hexadecimalintegerliteral.htm
---
Put 0x or 0X in front of the numbers. Use the letters A to F (or a to f) to represent digits with values 10 to 15, respectively.

```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    int hexValue1 = 0x100;
    int hexValue2 = 0x1234;
    int hexValue3 = 0xDEAF;
    int hexValue4 = 0xCAB;
    System.out.println(hexValue1);
    System.out.println(hexValue2);
    System.out.println(hexValue3);
    System.out.println(hexValue4);
  }
}
java title=Example.java
256
4660
57007
3243
```
