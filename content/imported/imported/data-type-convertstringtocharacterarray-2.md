---
title: Convert String to character array
nav: Convert String to characte...
description: Imported from the java2s.com archive: Convert String to character array
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertStringtocharacterarray.htm
---
```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    String str = "Abcdefg";
    char[] cArray = str.toCharArray();

    for (char c : cArray)
      System.out.println(c);
  }
}
/*
A
b
c
d
e
f
g
*/
```
