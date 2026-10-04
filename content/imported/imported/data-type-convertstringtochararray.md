---
title: Convert string to char array
nav: Convert string to char array
description: Imported from the java2s.com archive: Convert string to char array
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertstringtochararray.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    String literal = "Examples";

    char[] temp = literal.toCharArray();

    for (int i = 0; i < temp.length; i++) {
      System.out.print(temp[i]);
    }
  }
}
```
