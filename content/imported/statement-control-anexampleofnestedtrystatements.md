---
title: An example of nested try statements.
nav: An example of nested try s...
description: Imported from the java2s.com archive: An example of nested try statements.
section: Imported - java2s Archive
order: 1183
source: https://web.archive.org/web/20140829081643/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Anexampleofnestedtrystatements.htm
---
```java title=Example.java
class NestTry {
  public static void main(String args[]) {
    try {
      int a = args.length;
      int b = 42 / a;
      System.out.println("a = " + a);
      try {
        if (a == 1)
          a = a / (a - a); // division by zero
        if (a == 2) {
          int c[] = { 1 };
          c[42] = 99; // generate an out-of-bounds exception
        }
      } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Array index out-of-bounds: " + e);
      }
    } catch (ArithmeticException e) {
      System.out.println("Divide by 0: " + e);
    }
  }
}
```
