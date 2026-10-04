---
title: String.format()
nav: String.format()
description: Imported from the java2s.com archive: String.format()
section: Imported - java2s Archive
order: 1157
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Stringformatrightpadastring.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    System.out.println(">" + padRight("asdf", 10) + "<");
  }
  public static String padRight(String s, int n) {
    return String.format("%1$-" + n + "s", s);
  }
}
//>asdf      <
```
