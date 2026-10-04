---
title: Split a String
nav: Split a String
description: Imported from the java2s.com archive: Split a String
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20140216121412/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SplitaString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String str = "one,two,three,four,five";
    String[] elements = str.split(",");
    for (int i = 0; i < elements.length; i++)
      System.out.println(elements[i]);
  }
}
/*
one
two
three
four
five
*/
```
