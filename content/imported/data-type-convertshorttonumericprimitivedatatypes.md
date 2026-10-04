---
title: Convert Short to numeric primitive data types
nav: Convert Short to numeric p...
description: Imported from the java2s.com archive: Convert Short to numeric primitive data types
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertShorttonumericprimitivedatatypes.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Short sObj = new Short("10");
    byte b = sObj.byteValue();
    System.out.println(b);
    short s = sObj.shortValue();
    System.out.println(s);
    int i = sObj.intValue();
    System.out.println(i);
    float f = sObj.floatValue();
    System.out.println(f);
    double d = sObj.doubleValue();
    System.out.println(d);
    long l = sObj.longValue();
    System.out.println(l);
  }
}
/*
10
10
10
10.0
10.0
10
*/
```
