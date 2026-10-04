---
title: Compare Two Java boolean Arrays Example
nav: Compare Two Java boolean A...
description: Imported from the java2s.com archive: Compare Two Java boolean Arrays Example
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CompareTwoJavabooleanArraysExample.htm
---
```java title=Example.java
import java.util.Arrays;
publicclass Main {
  publicstaticvoid main(String[] args) {
    boolean[] a1 = newboolean[] { true, false, true };
    boolean[] a2 = newboolean[] { true, false, true };
    System.out.println(Arrays.equals(a1, a2));
  }
}
```
