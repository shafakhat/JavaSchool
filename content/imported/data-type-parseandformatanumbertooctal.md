---
title: Parse and format a number to octal
nav: Parse and format a number ...
description: Imported from the java2s.com archive: Parse and format a number to octal
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20140316035031/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parseandformatanumbertooctal.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    int i = Integer.parseInt("1000", 8);
    String s = Integer.toString(i, 8);
    System.out.println(s);
  }
}
```
