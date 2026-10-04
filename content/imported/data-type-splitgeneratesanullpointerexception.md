---
title: " ".split(" ") generates a NullPointerException
nav: " ".split(" ") generates a...
description: Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 0
section: Imported - java2s Archive
order: 1172
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/splitgeneratesaNullPointerException.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) throws Exception {
    String[] words = " ".split(" ");
    String firstWord = words[0];
    System.out.println(firstWord);
  }
}
/*
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 0
  at Main.main(Main.java:5)
*/
```
