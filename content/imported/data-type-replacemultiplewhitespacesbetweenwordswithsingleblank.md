---
title: Replace multiple whitespaces between words with single blank
nav: Replace multiple whitespac...
description: System.out.println(">" + " asdf ".replaceAll("\\b\\s{2,}\\b", " ") + "<");
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20140829080608/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Replacemultiplewhitespacesbetweenwordswithsingleblank.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    System.out.println(">" + "  asdf  ".replaceAll("\\b\\s{2,}\\b", " ") + "<");
  }
}
//>  asdf  <
```
