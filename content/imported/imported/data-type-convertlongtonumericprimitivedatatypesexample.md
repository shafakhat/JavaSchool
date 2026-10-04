---
title: Convert Long to numeric primitive data types example
nav: Convert Long to numeric pr...
description: Imported from the java2s.com archive: Convert Long to numeric primitive data types example
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertLongtonumericprimitivedatatypesexample.htm
---
```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    Long lObj = new Long("10");
    byte b = lObj.byteValue();
    System.out.println(b);

    short s = lObj.shortValue();
    System.out.println(s);

    int i = lObj.intValue();
    System.out.println(i);

    float f = lObj.floatValue();
    System.out.println(f);

    double d = lObj.doubleValue();
    System.out.println(d);
  }
}
```
