---
title: Convert String to character array
nav: Convert String to characte...
description: Imported from the java2s.com archive: Convert String to character array
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/20101009070932/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConvertStringtocharacterarray.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
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
