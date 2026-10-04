---
title: Demonstrate throw.
nav: Demonstrate throw.
description: Imported from the java2s.com archive: Demonstrate throw.
section: Imported - java2s Archive
order: 1188
source: https://web.archive.org/web/20140829080141/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Demonstratethrow.htm
---
```java title=Example.java
class ThrowDemo {
  static void demoproc() {
    try {
      throw new NullPointerException("demo");
    } catch (NullPointerException e) {
      System.out.println("Caught inside demoproc.");
      throw e; // rethrow the exception
    }
  }
  public static void main(String args[]) {
    try {
      demoproc();
    } catch (NullPointerException e) {
      System.out.println("Recaught: " + e);
    }
  }
}
```
