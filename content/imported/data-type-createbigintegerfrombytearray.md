---
title: Create BigInteger from byte array
nav: Create BigInteger from byt...
description: byte[] bytes = new byte[] { (byte) 0xFF, 0x00, 0x00 }; // -65536
section: Imported - java2s Archive
order: 1302
source: https://web.archive.org/web/20140829075838/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreateBigIntegerfrombytearray.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    // A negative value
    byte[] bytes = new byte[] { (byte) 0xFF, 0x00, 0x00 }; // -65536
    // A positive value
    bytes = new byte[] { 0x1, 0x00, 0x00 }; // 65536
    BigInteger bi = new BigInteger(bytes);
  }
}
```
