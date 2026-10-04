---
title: Use varargs with standard arguments.
nav: Use varargs with standard ...
description: Imported from the java2s.com archive: Use varargs with standard arguments.
section: Imported - java2s Archive
order: 1235
source: https://web.archive.org/web/20140829084016/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Usevarargswithstandardarguments.htm
---
```java title=Example.java
public class MainClass {
  static void vaTest(String msg, int... v) {
    System.out.print(msg + v.length + " Contents: ");
    for (int x : v)
      System.out.print(x + " ");
    System.out.println();
  }
  public static void main(String args[]) {
    vaTest("One vararg: ", 10);
    vaTest("Three varargs: ", 1, 2, 3);
    vaTest("No varargs: ");
  }
}
```
