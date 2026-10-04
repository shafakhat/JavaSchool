---
title: Demonstrates short-circuiting behavior
nav: Demonstrates short-circuit...
description: Imported from the java2s.com archive: Demonstrates short-circuiting behavior
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/Demonstratesshortcircuitingbehavior.htm
---
```java title=Example.java
publicclass MainClass {
  staticboolean test1(int val) {
    System.out.println("test1(" + val + ")");
    System.out.println("result: " + (val < 1));
    return val < 1;
  }
  staticboolean test2(int val) {
    System.out.println("test2(" + val + ")");
    System.out.println("result: " + (val < 2));
    return val < 2;
  }
  staticboolean test3(int val) {
    System.out.println("test3(" + val + ")");
    System.out.println("result: " + (val < 3));
    return val < 3;
  }
  publicstaticvoid main(String[] args) {
    if (test1(0) && test2(2) && test3(2))
      System.out.println("expression is true");
    else
      System.out.println("expression is false");
  }
}
java title=Example.java
test1(0)
result: true
test2(2)
result: false
expression is false
```
