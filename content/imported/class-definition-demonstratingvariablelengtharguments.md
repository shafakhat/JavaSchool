---
title: Demonstrating variable-length arguments
nav: Demonstrating variable-len...
description: A variable-length argument is specified by three periods (...).
section: Imported - java2s Archive
order: 1228
source: https://web.archive.org/web/20140829090044/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratingvariablelengtharguments.htm
---
A variable-length argument is specified by three periods (...).

```java title=Example.java
static void yourMethodInVarargs(int ... v) {}
```

yourMethodInVarargs( ) can be called with zero or more arguments.
---
v is implicitly declared as an array of type int[ ].
Inside vaTest( ), v is accessed using the normal array syntax.

```java title=Example.java
public class MainClass {
  // vaTest() now uses a vararg.
  public static void vaTest(int... v) {
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
java title=Example.java
Number of args: 1 Contents: 10
Number of args: 3 Contents: 1 2 3
Number of args: 0 Contents:
```
