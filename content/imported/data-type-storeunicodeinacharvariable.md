---
title: Store unicode in a char variable
nav: Store unicode in a char va...
description: Imported from the java2s.com archive: Store unicode in a char variable
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20140829083150/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Storeunicodeinacharvariable.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int x = 75;
    char y = (char) x;
    char half = '\u00AB';
    System.out.println("y is " + y + " and half is " + half);
  }
}
```
