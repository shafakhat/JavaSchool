---
title: Parsing and Formatting a Number into Binary
nav: Parsing and Formatting a N...
description: Imported from the java2s.com archive: Parsing and Formatting a Number into Binary
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20140829091426/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaNumberintoBinary.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    int i = 1023;
    i = Integer.parseInt("1111111111", 2);
    String s = Integer.toString(i, 2);
    System.out.println(s);
  }
}
```
