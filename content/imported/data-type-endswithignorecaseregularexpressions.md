---
title: Ends with, ignore case( regular expressions )
nav: Ends with, ignore case( re...
description: Imported from the java2s.com archive: Ends with, ignore case( regular expressions )
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Endswithignorecaseregularexpressions.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    String string = "I am Java";
    boolean b = string.matches("(?i).*Java");
  }
}
```
