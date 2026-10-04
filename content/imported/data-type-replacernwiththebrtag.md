---
title: Replace \r\n with the <br> tag
nav: Replace \r\n with the <br>...
description: System.out.println("\r\n|\r|\n|\n\r".replaceAll("(\r\n|\r|\n|\n\r)", "<br>"));
section: Imported - java2s Archive
order: 1079
source: https://web.archive.org/web/20140829080259/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Replacernwiththebrtag.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    System.out.println("\r\n|\r|\n|\n\r".replaceAll("(\r\n|\r|\n|\n\r)", "<br>"));
  }
}
//<br>|<br>|<br>|<br><br>
```
