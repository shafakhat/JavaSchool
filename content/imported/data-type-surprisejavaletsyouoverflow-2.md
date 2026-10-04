---
title: Surprise! Java lets you overflow
nav: Surprise! Java lets you ov...
description: Imported from the java2s.com archive: Surprise! Java lets you overflow
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SurpriseJavaletsyouoverflow.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    int big = 0x7fffffff; // max int value
    System.out.println("big = " + big);
    int bigger = big * 4;
    System.out.println("bigger = " + bigger);
  }
}
java title=Example.java
big = 2147483647
bigger = -4
```
