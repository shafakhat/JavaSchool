---
title: catch divide-by-zero error
nav: catch divide-by-zero error
description: Imported from the java2s.com archive: catch divide-by-zero error
section: Imported - java2s Archive
order: 1203
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/catchdividebyzeroerror.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int d, a;
    try {
      d = 0;
      a = 42 / d;
      System.out.println("This will not be printed.");
    } catch (ArithmeticException e) { //
      System.out.println("Division by zero.");
    }
    System.out.println("After catch statement.");
  }
}
```
