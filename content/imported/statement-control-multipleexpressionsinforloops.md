---
title: Multiple expressions in for loops
nav: Multiple expressions in fo...
description: Imported from the java2s.com archive: Multiple expressions in for loops
section: Imported - java2s Archive
order: 1321
source: https://web.archive.org/web/20140829091720/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Multipleexpressionsinforloops.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    for (int i = 0, j = 0; i < 5; i++, j--)
      System.out.println("i = " + i + " j= " + j);
  }
}
/*
i = 0 j= 0
i = 1 j= -1
i = 2 j= -2
i = 3 j= -3
i = 4 j= -4
*/
```
