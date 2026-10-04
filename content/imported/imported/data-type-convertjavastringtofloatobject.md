---
title: Convert Java String to Float Object
nav: Convert Java String to Flo...
description: Imported from the java2s.com archive: Convert Java String to Float Object
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavaStringtoFloatObject.htm
---
```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    Float fObj1 = new Float("10.64");
    System.out.println(fObj1);

    Float fObj2 = Float.valueOf("10.76");
    System.out.println(fObj2);

    float f = Float.parseFloat("7.39");
    System.out.println(f);
  }
}
/*
10.64
10.76
7.39
*/
```
