---
title: Convert java Double to numeric primitive data types
nav: Convert java Double to num...
description: Imported from the java2s.com archive: Convert java Double to numeric primitive data types
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertjavaDoubletonumericprimitivedatatypes.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    Double dObj = new Double("10.50");
    byte b = dObj.byteValue();
    System.out.println(b);

    short s = dObj.shortValue();
    System.out.println(s);

    int i = dObj.intValue();
    System.out.println(i);

    float f = dObj.floatValue();
    System.out.println(f);

    double d = dObj.doubleValue();
    System.out.println(d);
  }
}
/*
10
10
10
10.5
10.5
*/
```
