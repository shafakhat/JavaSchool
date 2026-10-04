---
title: The Left Shift
nav: The Left Shift
description: Imported from the java2s.com archive: The Left Shift
section: Imported - java2s Archive
order: 1156
source: https://web.archive.org/web/20140309050235/http://www.java2s.com/Tutorial/Java/0060__Operators/TheLeftShift.htm
---
```java title=Example.java
// Left shifting a byte value.
public class MainClass {
  public static void main(String args[]) {
    byte a = 64, b;
    int i;
    i = a << 2;
    b = (byte) (a << 2);
    System.out.println("Original value of a: " + a);
    System.out.println("i and b: " + i + " " + b);
  }
}
java title=Example.java
Original value of a: 64
i and b: 256 0
```
