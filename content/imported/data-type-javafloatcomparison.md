---
title: Java Float Comparison
nav: Java Float Comparison
description: Imported from the java2s.com archive: Java Float Comparison
section: Imported - java2s Archive
order: 1066
source: https://web.archive.org/web/20140829080625/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaFloatComparison.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    float f1 = 5.5f;
    float f2 = 5.4f;
    int i1 = Float.compare(f1, f2);
    if (i1 > 0) {
      System.out.println(">");
    } else if (i1 < 0) {
      System.out.println("<");
    } else {
      System.out.println("=");
    }
    Float fObj1 = new Float("5.5");
    Float fObj2 = new Float("5.4");
    int i2 = fObj1.compareTo(fObj2);
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
