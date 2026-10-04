---
title: String.format()
nav: String.format()
description: Imported from the java2s.com archive: String.format()
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Stringformatleftpadastring.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    System.out.println(">" + padLeft("asdf", 10) + "<");
  }
  publicstatic String padLeft(String s, int n) {
    return String.format("%1$#" + n + "s", s);
  }
}
//>      asdf<
```
