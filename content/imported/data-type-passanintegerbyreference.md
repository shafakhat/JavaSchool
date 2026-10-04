---
title: Pass an integer by reference
nav: Pass an integer by reference
description: Imported from the java2s.com archive: Pass an integer by reference
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Passanintegerbyreference.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    int[] a = newint[1];
    a[0] = 1;
    add(a);
    System.out.println(a[0]);
  }
  staticvoid add(int[] a) {
    a[0] = a[0] + 2;
  }
}
// 3
```
