---
title: Java Sort long Array Example
nav: Java Sort long Array Example
description: Imported from the java2s.com archive: Java Sort long Array Example
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20090912060600/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JavaSortlongArrayExample.htm
---
```java title=Example.java
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    long[] l1 = new long[] { 3L, 2L, 5L, 4L, 1L };
    for (long l: l1){
      System.out.print(" " + l);
    }
    Arrays.sort(l1);
    for (long l: l1){
      System.out.print(" " + l);
    }
    long[] l2 = new long[] { 5, 2, 3, 1, 4 };
    Arrays.sort(l2, 1, 4);
    for (long l: l2){
      System.out.print(" " + l);
    }
  }
}
```
