---
title: Parsing and Formatting a Big Integer into decimal
nav: Parsing and Formatting a B...
description: Imported from the java2s.com archive: Parsing and Formatting a Big Integer into decimal
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaBigIntegerintodecimal.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("1023");
    String s = bi.toString();
  }
}
```
