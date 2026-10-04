---
title: Override the clone() method.
nav: Override the clone() method.
description: Imported from the java2s.com archive: Override the clone() method.
section: Imported - java2s Archive
order: 1237
source: https://web.archive.org/web/20140829080319/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Overridetheclonemethod.htm
---
```java title=Example.java
class TestClone implements Cloneable {
  int a;
  double b;
  public Object clone() {
    try {
      return super.clone();
    } catch (CloneNotSupportedException e) {
      System.out.println("Cloning not allowed.");
      return this;
    }
  }
}
class CloneDemo2 {
  public static void main(String args[]) {
    TestClone x1 = new TestClone();
    TestClone x2;
    x1.a = 10;
    x1.b = 20.98;
    x2 = (TestClone) x1.clone();
    System.out.println("x1: " + x1.a + " " + x1.b);
    System.out.println("x2: " + x2.a + " " + x2.b);
  }
}
```
