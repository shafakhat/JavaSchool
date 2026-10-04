---
title: Demonstrate multiple catch statements.
nav: Demonstrate multiple catch...
description: Imported from the java2s.com archive: Demonstrate multiple catch statements.
section: Imported - java2s Archive
order: 1181
source: https://web.archive.org/web/20140829082406/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Demonstratemultiplecatchstatements.htm
---
```java title=Example.java
class MultiCatch {
  public static void main(String args[]) {
    try {
      int a = args.length;
      System.out.println("a = " + a);
      int b = 42 / a;
      int c[] = { 1 };
      c[42] = 99;
    } catch (ArithmeticException e) {
      System.out.println("Divide by 0: " + e);
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Array index oob: " + e);
    }
    System.out.println("After try/catch blocks.");
  }
}
```
