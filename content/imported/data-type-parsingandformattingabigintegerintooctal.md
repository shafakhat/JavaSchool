---
title: Parsing and Formatting a Big Integer into octal
nav: Parsing and Formatting a B...
description: Imported from the java2s.com archive: Parsing and Formatting a Big Integer into octal
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaBigIntegerintooctal.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("1000", 8);
    s = bi.toString(8);
  }
}
```
