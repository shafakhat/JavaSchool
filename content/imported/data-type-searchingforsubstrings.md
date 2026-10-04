---
title: Searching for Substrings
nav: Searching for Substrings
description: Imported from the java2s.com archive: Searching for Substrings
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SearchingforSubstrings.htm
---
```java title=Example.java
public class MainClass{
  public static void main(String[] arg){
    String str = "abcdeabcdef";
    int startIndex = 3;
    int index = 0;
    index = str.indexOf("ab", startIndex);
    System.out.println(index);
  }
}
java title=Example.java
5
```
