---
title: Creating Character Arrays From String Objects
nav: Creating Character Arrays ...
description: Imported from the java2s.com archive: Creating Character Arrays From String Objects
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreatingCharacterArraysFromStringObjects.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    String text = "To be or not to be";
    char[] textArray = text.toCharArray();
    for(char ch: textArray){
      System.out.println(ch);
    }
  }
}
java title=Example.java
T
o
b
e
o
r
n
o
t
t
o
b
e
```
