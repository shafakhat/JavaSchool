---
title: Demonstrate the clone() method.
nav: Demonstrate the clone() me...
description: Imported from the java2s.com archive: Demonstrate the clone() method.
section: Imported - java2s Archive
order: 1239
source: https://web.archive.org/web/20140829080239/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratetheclonemethod.htm
---
```java title=Example.java
class TestClone implements Cloneable {
  int a;
  double b;
  TestClone cloneTest() {
    try {
      return (TestClone) super.clone();
    } catch (CloneNotSupportedException e) {
      System.out.println("Cloning not allowed.");
      return this;
    }
  }
}
class CloneDemo {
  public static void main(String args[]) {
    TestClone x1 = new TestClone();
    TestClone x2;
    x1.a = 10;
    x1.b = 20.98;
    x2 = x1.cloneTest(); // clone x1
    System.out.println("x1: " + x1.a + " " + x1.b);
    System.out.println("x2: " + x2.a + " " + x2.b);
  }
}
```
