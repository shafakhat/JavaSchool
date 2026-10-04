---
title: Java Sort short Array
nav: Java Sort short Array
description: Imported from the java2s.com archive: Java Sort short Array
section: Imported - java2s Archive
order: 1140
source: https://web.archive.org/web/20101020195313/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JavaSortshortArray.htm
---
```java title=Example.java
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    short[] s1 = new short[] { 31, 21, 51, 41, 11 };
    for (short s : s1) {
      System.out.print(" " + s);
    }
    Arrays.sort(s1);
    for (short s : s1) {
      System.out.print(" " + s);
    }
    short[] s2 = new short[] { 5, 2, 3, 1, 4 };
    Arrays.sort(s2, 1, 4);
    for (short s : s2) {
      System.out.print(" " + s);
    }
  }
}
```
