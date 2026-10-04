---
title: Convert String to byte
nav: Convert String to byte
description: // Causes a NumberFormatException since the value is out of range
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertStringtobyte.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String s = "65";
    byte b = Byte.valueOf(s);
    System.out.println(b);
    // Causes a NumberFormatException since the value is out of range
    System.out.println(Byte.valueOf("129"));
  }
}
/*
65
Exception in thread "main" java.lang.NumberFormatException: Value out of range. Value:"129" Radix:10
  at java.lang.Byte.parseByte(Byte.java:153)
  at java.lang.Byte.valueOf(Byte.java:184)
  at java.lang.Byte.valueOf(Byte.java:208)
  at Main.main(Main.java:11)
*/
```
