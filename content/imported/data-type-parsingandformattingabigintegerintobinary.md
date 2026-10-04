---
title: Parsing and Formatting a Big Integer into Binary
nav: Parsing and Formatting a B...
description: Imported from the java2s.com archive: Parsing and Formatting a Big Integer into Binary
section: Imported - java2s Archive
order: 1307
source: https://web.archive.org/web/20140829080009/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaBigIntegerintoBinary.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("1023");
    // Parse and format to binary
    bi = new BigInteger("1111111111", 2);
    String s = bi.toString(2);
  }
}
```
