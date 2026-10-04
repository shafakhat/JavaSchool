---
title: Match Name Formats
nav: Match Name Formats
description: Imported from the java2s.com archive: Match Name Formats
section: Imported - java2s Archive
order: 1174
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/MatchNameFormats.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    boolean retval = false;
    String name = "first last";
    String nameToken = "\\p{Upper}(\\p{Lower}+\\s?)";
    String namePattern = "(" + nameToken + "){2,3}";
    retval = name.matches(namePattern);
  }
}
```
