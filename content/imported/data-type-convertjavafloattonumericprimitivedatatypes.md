---
title: Convert Java Float to Numeric Primitive Data Types
nav: Convert Java Float to Nume...
description: Imported from the java2s.com archive: Convert Java Float to Numeric Primitive Data Types
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavaFloattoNumericPrimitiveDataTypes.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Float fObj = new Float("10.50");
    byte b = fObj.byteValue();
    System.out.println(b);
    short s = fObj.shortValue();
    System.out.println(s);
    int i = fObj.intValue();
    System.out.println(i);
    float f = fObj.floatValue();
    System.out.println(f);
    double d = fObj.doubleValue();
    System.out.println(d);
  }
}
```
