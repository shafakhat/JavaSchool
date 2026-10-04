---
title: Demonstrate lifetime of a variable
nav: Demonstrate lifetime of a ...
description: Imported from the java2s.com archive: Demonstrate lifetime of a variable
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Demonstratelifetimeofavariable.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    int x;
    for (x = 0; x < 3; x++) {
      int y = -1; // y is initialized each time block is entered
      System.out.println("y is: " + y); // this always prints -1
      y = 100;
      System.out.println("y is now: " + y);
    }
  }
}
java title=Example.java
y is: -1
y is now: 100
y is: -1
y is now: 100
y is: -1
y is now: 100
```
