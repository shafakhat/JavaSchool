---
title: Try statements can be implicitly nested via calls to methods
nav: Try statements can be impl...
description: Imported from the java2s.com archive: Try statements can be implicitly nested via calls to methods
section: Imported - java2s Archive
order: 1192
source: https://web.archive.org/web/20140829081641/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Trystatementscanbeimplicitlynestedviacallstomethods.htm
---
```java title=Example.java
class MethNestTry {
  static void nesttry(int a) {
    try {
      if (a == 1)
        a = a / (a - a);
      if (a == 2) {
        int c[] = { 1 };
        c[42] = 99; // generate an out-of-bounds exception
      }
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Array index out-of-bounds: " + e);
    }
  }
  public static void main(String args[]) {
    try {
      int a = args.length;
      int b = 42 / a;
      System.out.println("a = " + a);
      nesttry(a);
    } catch (ArithmeticException e) {
      System.out.println("Divide by 0: " + e);
    }
  }
}
```
