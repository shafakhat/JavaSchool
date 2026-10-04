---
title: Autoboxing/unboxing takes place with method parameters and return values.
nav: Autoboxing/unboxing takes ...
description: Imported from the java2s.com archive: Autoboxing/unboxing takes place with method parameters and return values.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autoboxingunboxingtakesplacewithmethodparametersandreturnvalues.htm
---
```java title=Example.java
class AutoBox2 {
  staticint m(Integer v) {
    return v; // auto-unbox to int
  }

  publicstaticvoid main(String args[]) {
    Integer iOb = m(100);

    System.out.println(iOb);
  }
}
```
