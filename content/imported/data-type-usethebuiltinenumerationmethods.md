---
title: Use the built-in enumeration methods.
nav: Use the built-in enumerati...
description: Imported from the java2s.com archive: Use the built-in enumeration methods.
section: Imported - java2s Archive
order: 1095
source: https://web.archive.org/web/20140829083650/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usethebuiltinenumerationmethods.htm
---
```java title=Example.java
enum Apple {
  A, B, C, D, E
}
class EnumDemo2 {
  public static void main(String args[]) {
    Apple ap;
    System.out.println("Here are all Apple constants:");
    // use values()
    Apple allapples[] = Apple.values();
    for (Apple a : allapples)
      System.out.println(a);
    System.out.println();
    // use valueOf()
    ap = Apple.valueOf("D");
    System.out.println("ap contains " + ap);
  }
}
```
