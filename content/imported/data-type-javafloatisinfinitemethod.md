---
title: Java Float isInfinite Method
nav: Java Float isInfinite Method
description: Imported from the java2s.com archive: Java Float isInfinite Method
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20140829080150/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaFloatisInfiniteMethod.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    float f = (float) 1 / 0;
    boolean b1 = Float.isInfinite(f);
    System.out.println(b1);
    Float fObj = new Float(f);
    boolean b2 = fObj.isInfinite();
    System.out.println(b2);
  }
}
```
