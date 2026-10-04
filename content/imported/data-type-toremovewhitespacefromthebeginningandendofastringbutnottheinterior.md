---
title: To remove whitespace from the beginning and end of a string (but not the interior)
nav: To remove whitespace from ...
description: Imported from the java2s.com archive: To remove whitespace from the beginning and end of a string (but not the interior)
section: Imported - java2s Archive
order: 1128
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toremovewhitespacefromthebeginningandendofastringbutnottheinterior.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String sample = "   This is a string   ";
    String result = sample.trim();
    System.out.println(">"+sample+"<");
    System.out.println(">"+result+"<");
  }
}
java title=Example.java
>   This is a string   <
>This is a string<
```
