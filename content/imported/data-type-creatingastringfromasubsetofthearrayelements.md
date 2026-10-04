---
title: Creating a string from a subset of the array elements
nav: Creating a string from a s...
description: char[] textArray = { 'T', 'o', ' ', 'b', 'e', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o',
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Creatingastringfromasubsetofthearrayelements.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    char[] textArray = { 'T', 'o', ' ', 'b', 'e', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o',
        ' ', 'b', 'e' };
    String text = String.copyValueOf(textArray, 9, 3);
    System.out.println(text);
  }
}
java title=Example.java
not
```
