---
title: Convert Java String to Double
nav: Convert Java String to Dou...
description: Imported from the java2s.com archive: Convert Java String to Double
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavaStringtoDouble.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Double dObj1 = new Double("100.564");
    System.out.println(dObj1);
    Double dObj2 = Double.valueOf("10.6");
    System.out.println(dObj2);
    double d = Double.parseDouble("76.39");
    System.out.println(d);
  }
}
```
