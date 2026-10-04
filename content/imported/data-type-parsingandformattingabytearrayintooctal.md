---
title: Parsing and Formatting a Byte Array into Octal
nav: Parsing and Formatting a B...
description: byte[] bytes = new byte[] { (byte) 0x12, (byte) 0x0F, (byte) 0xF0 };
section: Imported - java2s Archive
order: 1308
source: https://web.archive.org/web/20140829080241/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingandFormattingaByteArrayintoOctal.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] bytes = new byte[] { (byte) 0x12, (byte) 0x0F, (byte) 0xF0 };
    BigInteger bi = new BigInteger(bytes);
    // Format to octal
    String s = bi.toString(8);
    System.out.println(s);
  }
}
```
