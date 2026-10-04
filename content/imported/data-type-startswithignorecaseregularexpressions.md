---
title: Starts with, ignore case( regular expressions )
nav: Starts with, ignore case( ...
description: Imported from the java2s.com archive: Starts with, ignore case( regular expressions )
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Startswithignorecaseregularexpressions.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    String string = "I am Java";
    boolean b = string.matches("(?i)i am.*");
  }
}
```
