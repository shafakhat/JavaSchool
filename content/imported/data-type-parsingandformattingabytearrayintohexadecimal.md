---
title: Parsing and Formatting a Byte Array into Hexadecimal
nav: Parsing and Formatting a B...
description: byte[] bytes = newbyte[] { (byte) 0x12, (byte) 0x0F, (byte) 0xF0 };
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaByteArrayintoHexadecimal.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { (byte) 0x12, (byte) 0x0F, (byte) 0xF0 };
    BigInteger bi = new BigInteger(bytes);
    // Format to hexadecimal
    String s = bi.toString(16);
    if (s.length() % 2 != 0) {
      s = "0" + s;
    }
  }
}
```
