---
title: new String(textArray, 9, 3)
nav: new String(textArray, 9, 3)
description: char[] textArray = { 'T', 'o', ' ', 'b', 'e', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o',
section: Imported - java2s Archive
order: 1066
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/newStringtextArray93CreatingStringObjectsFromcertainpartofacharacterArray.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    char[] textArray = { 'T', 'o', ' ', 'b', 'e', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o',
        ' ', 'b', 'e' };
    String text = new String(textArray, 9, 3);
    System.out.println(text);
  }
}
java title=Example.java
not
```
