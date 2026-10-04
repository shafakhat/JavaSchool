---
title: Replace multiple whitespaces between words with single blank
nav: Replace multiple whitespac...
description: System.out.println(">" + " asdf ".replaceAll("\\b\\s{2,}\\b", " ") + "<");
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Replacemultiplewhitespacesbetweenwordswithsingleblank.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    System.out.println(">" + "  asdf  ".replaceAll("\\b\\s{2,}\\b", " ") + "<");
  }
}
//>  asdf  <
```
