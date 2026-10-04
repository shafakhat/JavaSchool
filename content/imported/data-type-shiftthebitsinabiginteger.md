---
title: Shift the bits in a BigInteger
nav: Shift the bits in a BigInt...
description: Imported from the java2s.com archive: Shift the bits in a BigInteger
section: Imported - java2s Archive
order: 1304
source: https://web.archive.org/web/20140829075831/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ShiftthebitsinaBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] bytes = new byte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.shiftLeft(3);
  }
}
```
