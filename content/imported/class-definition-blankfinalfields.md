---
title: 'Blank' final fields
nav: 'Blank' final fields
description: Imported from the java2s.com archive: 'Blank' final fields
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Blankfinalfields.htm
---
```java title=Example.java
class A {
  private int i;
  A(int ii) {
    i = ii;
  }
}
public class MainClass {
  private final int i = 0; // Initialized final
 private final int j; // Blank final
 private final A a; // Blank final reference
 // Blank finals MUST be initialized in the constructor:
 public MainClass() {
    j = 1; // Initialize blank final
    a = new A(1); // Initialize blank final reference
  }
  public MainClass(int x) {
    j = x; // Initialize blank final
    a = new A(x); // Initialize blank final reference
  }
  public static void main(String[] args) {
    new MainClass();
    new MainClass(47);
  }
}
```
