---
title: Demonstrate variable-length arguments.
nav: Demonstrate variable-lengt...
description: System.out.print("Number of args: " + v.length + " Contents: ");
section: Imported - java2s Archive
order: 1232
source: https://web.archive.org/web/20140829083926/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratevariablelengtharguments.htm
---
```java title=Example.java
class VarArgs {
  // vaTest() now uses a vararg.
  static void vaTest(int... v) {
    System.out.print("Number of args: " + v.length + " Contents: ");
    for (int x : v)
      System.out.print(x + " ");
    System.out.println();
  }
  public static void main(String args[]) {
    vaTest(10); // 1 arg
    vaTest(1, 2, 3); // 3 args
    vaTest(); // no args
  }
}
```
