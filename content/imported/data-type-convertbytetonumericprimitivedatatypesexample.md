---
title: Convert Byte to numeric primitive data types example
nav: Convert Byte to numeric pr...
description: Imported from the java2s.com archive: Convert Byte to numeric primitive data types example
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertBytetonumericprimitivedatatypesexample.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    Byte bObj = new Byte("10");
    byte b = bObj.byteValue();
    System.out.println(b);
    short s = bObj.shortValue();
    System.out.println(s);
    int i = bObj.intValue();
    System.out.println(i);
    float f = bObj.floatValue();
    System.out.println(f);
    double d = bObj.doubleValue();
    System.out.println(d);
    long l = bObj.longValue();
    System.out.println(l);
  }
}
```
