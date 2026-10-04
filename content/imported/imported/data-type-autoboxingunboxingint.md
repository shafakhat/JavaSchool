---
title: Autoboxing/unboxing int
nav: Autoboxing/unboxing int
description: Imported from the java2s.com archive: Autoboxing/unboxing int
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autoboxingunboxingint.htm
---
```java title=Example.java
class AutoBox {
  publicstaticvoid main(String args[]) {

    Integer iOb = 100; // autobox an int
int i = iOb; // auto-unbox

    System.out.println(i + " " + iOb); // displays 100 100
  }
}
```
