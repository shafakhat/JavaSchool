---
title: Several assignment operators
nav: Several assignment operators
description: Imported from the java2s.com archive: Several assignment operators
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20070613000729/http://www.java2s.com:80/Tutorial/Java/0060__Operators/Severalassignmentoperators.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int a = 1;
    int b = 2;
    int c = 3;
    a += 5;
    b *= 4;
    c += a * b;
    c %= 6;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
  }
}
java title=Example.java
a = 6
b = 8
c = 3
```
