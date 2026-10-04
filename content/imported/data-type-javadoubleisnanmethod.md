---
title: Java Double isNaN method
nav: Java Double isNaN method
description: Imported from the java2s.com archive: Java Double isNaN method
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaDoubleisNaNmethod.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    double d = Math.sqrt(-10);
    boolean b1 = Double.isNaN(d);
    System.out.println(b1);
    Double dObj = new Double(d);
    boolean b2 = dObj.isNaN();
    System.out.println(b2);
  }
}
```
