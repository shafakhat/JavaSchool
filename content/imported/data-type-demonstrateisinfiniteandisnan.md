---
title: Demonstrate isInfinite() and isNaN()
nav: Demonstrate isInfinite() a...
description: System.out.println(d1 + ": " + d1.isInfinite() + ", " + d1.isNaN());
section: Imported - java2s Archive
order: 1077
source: https://web.archive.org/web/20140324195441/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DemonstrateisInfiniteandisNaN.htm
---
```java title=Example.java
class InfNaN {
  public static void main(String args[]) {
    Double d1 = new Double(1/0.);
    Double d2 = new Double(0/0.);
    System.out.println(d1 + ": " + d1.isInfinite() + ", " + d1.isNaN());
    System.out.println(d2 + ": " + d2.isInfinite() + ", " + d2.isNaN());
  }
}
```
