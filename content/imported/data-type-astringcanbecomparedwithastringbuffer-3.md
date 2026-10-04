---
title: A string can be compared with a StringBuffer
nav: A string can be compared w...
description: Imported from the java2s.com archive: A string can be compared with a StringBuffer
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AstringcanbecomparedwithaStringBuffer.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    String s1 = "s1";
    StringBuffer sbuf = new StringBuffer("a");
    boolean b = s1.contentEquals(sbuf);
  }
}
```
