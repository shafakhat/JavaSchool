---
title: Java Double compare example
nav: Java Double compare example
description: Imported from the java2s.com archive: Java Double compare example
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20140324195446/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaDoublecompareexample.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    double d1 = 5.5;
    double d2 = 5.4;
    int i1 = Double.compare(d1, d2);
    if (i1 > 0) {
      System.out.println(">");
    } else if (i1 < 0) {
      System.out.println("<");
    } else {
      System.out.println("=");
    }
    Double dObj1 = new Double("5.5");
    Double dObj2 = new Double("5.4");
    int i2 = dObj1.compareTo(dObj2);
    if (i2 > 0) {
      System.out.println(">");
    } else if (i2 < 0) {
      System.out.println("<");
    } else {
      System.out.println("=");
    }
  }
}
```
