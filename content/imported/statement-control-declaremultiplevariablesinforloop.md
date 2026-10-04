---
title: Declare multiple variables in for loop
nav: Declare multiple variables...
description: Imported from the java2s.com archive: Declare multiple variables in for loop
section: Imported - java2s Archive
order: 1320
source: https://web.archive.org/web/20140829091946/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Declaremultiplevariablesinforloop.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    for (int i = 0, j = 1, k = 2; i < 5; i++){
      System.out.println("I : " + i + ",j : " + j + ", k : " + k);
    }
  }
}
/*
I : 0,j : 1, k : 2
I : 1,j : 1, k : 2
I : 2,j : 1, k : 2
I : 3,j : 1, k : 2
I : 4,j : 1, k : 2
*/
```
