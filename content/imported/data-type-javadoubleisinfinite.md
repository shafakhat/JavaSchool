---
title: Java Double isInfinite
nav: Java Double isInfinite
description: Imported from the java2s.com archive: Java Double isInfinite
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20140324200402/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaDoubleisInfinite.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    double d = (double) 4 / 0;
    boolean b1 = Double.isInfinite(d);
    System.out.println(b1);
    Double dObj = new Double(d);
    boolean b2 = dObj.isInfinite();
    System.out.println(b2);
  }
}
```
