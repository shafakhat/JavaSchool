---
title: Remove a character at a specified position using String.substring
nav: Remove a character at a sp...
description: Imported from the java2s.com archive: Remove a character at a specified position using String.substring
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/RemoveacharacterataspecifiedpositionusingStringsubstring.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    String str = "this is a test";
    System.out.println(removeCharAt(str, 3));
  }
  publicstatic String removeCharAt(String s, int pos) {
    return s.substring(0, pos) + s.substring(pos + 1);
  }
}
```
