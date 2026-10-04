---
title: Compare Two Java byte Arrays Example
nav: Compare Two Java byte Arra...
description: Imported from the java2s.com archive: Compare Two Java byte Arrays Example
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CompareTwoJavabyteArraysExample.htm
---
```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    byte[] a1 = newbyte[] { 7, 25, 12 };
    byte[] a2 = newbyte[] { 7, 25, 12 };

    System.out.println(Arrays.equals(a1, a2));
  }
}
```
