---
title: Parsing and Formatting a Byte Array into Binary
nav: Parsing and Formatting a B...
description: byte[] bytes = newbyte[] { (byte) 0x12, (byte) 0x0F, (byte) 0xF0 };
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaByteArrayintoBinary.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { (byte) 0x12, (byte) 0x0F, (byte) 0xF0 };
    // Create a BigInteger using the byte array
    BigInteger bi = new BigInteger(bytes);
    String s = bi.toString(2);
    System.out.println(s);
  }
}
```
