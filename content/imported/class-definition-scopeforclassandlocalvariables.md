---
title: Scope for Class and Local Variables
nav: Scope for Class and Local ...
description: Imported from the java2s.com archive: Scope for Class and Local Variables
section: Imported - java2s Archive
order: 1202
source: https://web.archive.org/web/20140829081416/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ScopeforClassandLocalVariables.htm
---
```java title=Example.java
public class MainClass {
  static int x;
  public static void main(String[] args) {
    x = 5;
    System.out.println("main: x = " + x);
    myMethod();
  }
  public static void myMethod() {
    int y;
    y = 10;
    if (y == x + 5) {
      int z;
      z = 15;
      System.out.println("myMethod: z = " + z);
    }
    System.out.println("myMethod: x = " + x);
    System.out.println("myMethod: y = " + y);
  }
}
```
