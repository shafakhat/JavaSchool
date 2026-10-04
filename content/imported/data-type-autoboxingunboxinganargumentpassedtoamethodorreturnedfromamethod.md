---
title: Autoboxing/unboxing
nav: Autoboxing/unboxing
description: Autoboxing/unboxing takes place with method parameters and return values.
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autoboxingunboxinganargumentpassedtoamethodorreturnedfromamethod.htm
---
Autoboxing/unboxing takes place with method parameters and return values.

```java title=Example.java
publicclass MainClass {
  staticint m(Integer v) {
    return v ; // auto-unbox to int
  }
  publicstaticvoid main(String args[]) {
    Integer iOb = m(100);
    System.out.println(iOb);
  }
}
```

```java title=Example.java
100
```
