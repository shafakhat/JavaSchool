---
title: Demonstrate static variables, methods, and blocks.
nav: Demonstrate static variabl...
description: Imported from the java2s.com archive: Demonstrate static variables, methods, and blocks.
section: Imported - java2s Archive
order: 1207
source: https://web.archive.org/web/20140829084049/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratestaticvariablesmethodsandblocks.htm
---
```java title=Example.java
class UseStatic {
  static int a = 3;
  static int b;
  static void meth(int x) {
    System.out.println("x = " + x);
    System.out.println("a = " + a);
    System.out.println("b = " + b);
  }
  static {
    System.out.println("Static block initialized.");
    b = a * 4;
  }
  public static void main(String args[]) {
    meth(42);
  }
}
```
