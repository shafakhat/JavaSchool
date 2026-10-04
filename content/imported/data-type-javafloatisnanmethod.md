---
title: Java Float isNaN Method
nav: Java Float isNaN Method
description: Imported from the java2s.com archive: Java Float isNaN Method
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/20140829080615/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaFloatisNaNMethod.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    float f = (float) Math.sqrt(-10);
    boolean b1 = Float.isNaN(f);
    System.out.println(b1);
    Float fObj = new Float(f);
    boolean b2 = fObj.isNaN();
    System.out.println(b2);
  }
}
```
