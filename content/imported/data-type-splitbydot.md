---
title: Split by dot
nav: Split by dot
description: Imported from the java2s.com archive: Split by dot
section: Imported - java2s Archive
order: 1184
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Splitbydot.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) throws Exception {
    String s = "A.BB.CCC";
    String[] words = s.split("\\.");
    for (String str : words) {
      System.out.println(str);
    }
  }
}
/*
A
BB
CCC
*/
```
