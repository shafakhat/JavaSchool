---
title: Convert a number to negative and back
nav: Convert a number to negati...
description: Imported from the java2s.com archive: Convert a number to negative and back
section: Imported - java2s Archive
order: 1162
source: https://web.archive.org/web/20140829084332/http://www.java2s.com/Tutorial/Java/0060__Operators/Convertanumbertonegativeandback.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] a) {
    int i = 1;
    System.out.println(i);
    int j = ~i + 1;
    System.out.println(j);
    i = ~j + 1;
    System.out.println(i);
  }
}
/*
1
-1
1
*/
```
