---
title: Creating String Objects From Character Arrays using String.copyValueOf()
nav: Creating String Objects Fr...
description: char[] textArray = { 'T', 'o', ' ', 'b', 'e', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o',
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreatingStringObjectsFromCharacterArraysusingStringcopyValueOf.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    char[] textArray = { 'T', 'o', ' ', 'b', 'e', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o',
        ' ', 'b', 'e' };
    String text = String.copyValueOf(textArray);
    System.out.println(text);
  }
}
java title=Example.java
To be or not to be
```
