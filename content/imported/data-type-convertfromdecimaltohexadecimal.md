---
title: Convert from decimal to hexadecimal
nav: Convert from decimal to he...
description: Imported from the java2s.com archive: Convert from decimal to hexadecimal
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertfromdecimaltohexadecimal.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    int i = 42;
    String hexstr = Integer.toString(i, 16);
    System.out.println(hexstr);
    hexstr = Integer.toHexString(i);
    System.out.println(hexstr);
  }
}
/*
2a
2a
*/
```
