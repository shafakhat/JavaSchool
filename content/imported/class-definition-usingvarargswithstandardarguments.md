---
title: Using varargs with standard arguments
nav: Using varargs with standar...
description: A method can have "normal' parameters along with a variable-length parameter. However, the variable-length parameter must be the last parameter.
section: Imported - java2s Archive
order: 1231
source: https://web.archive.org/web/20140829084051/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Usingvarargswithstandardarguments.htm
---
A method can have "normal' parameters along with a variable-length parameter. However, the variable-length parameter must be the last parameter.
There must be only one varargs parameter.

```java title=Example.java
int aMethod(int a, int b, double c, int ... vals) {}
java title=Example.java
int aMethod(int a, int b, double c, int ... vals, double ... morevals) { // Error!
java title=Example.java
public class MainClass {
  static void vaTest(String msg, int... v) {
    System.out.print(msg + v.length + " Contents: ");
    for (int x : v) {
      System.out.print(x + " ");
    }
    System.out.println();
  }
  public static void main(String args[]) {
    vaTest("One vararg: ", 10);
    vaTest("Three varargs: ", 1, 2, 3);
    vaTest("No varargs: ");
  }
}
java title=Example.java
One vararg: 1 Contents: 10
Three varargs: 3 Contents: 1 2 3
No varargs: 0 Contents:
```
