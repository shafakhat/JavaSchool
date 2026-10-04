---
title: Overloading Vararg Methods
nav: Overloading Vararg Methods
description: System.out.print("vaTest(int ...): " + "Number of args: " + v.length + " Contents: ");
section: Imported - java2s Archive
order: 1234
source: https://web.archive.org/web/20140829083608/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/OverloadingVarargMethods.htm
---
```java title=Example.java
class MainClass {
  static void vaTest(int... v) {
    System.out.print("vaTest(int ...): " + "Number of args: " + v.length + " Contents: ");
    for (int x : v)
      System.out.print(x + " ");
    System.out.println();
  }
  static void vaTest(boolean... v) {
    System.out.print("vaTest(boolean ...) " + "Number of args: " + v.length + " Contents: ");
    for (boolean x : v)
      System.out.print(x + " ");
    System.out.println();
  }
  static void vaTest(String msg, int... v) {
    System.out.print("vaTest(String, int ...): " + msg + v.length + " Contents: ");
    for (int x : v)
      System.out.print(x + " ");
    System.out.println();
  }
  public static void main(String args[]) {
    vaTest(1, 2, 3);
    vaTest("Testing: ", 10, 20);
    vaTest(true, false, false);
  }
}
```
