---
title: Get byte array from BigInteger
nav: Get byte array from BigInt...
description: Imported from the java2s.com archive: Get byte array from BigInteger
section: Imported - java2s Archive
order: 1318
source: https://web.archive.org/web/20140829075841/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetbytearrayfromBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("100100100111111110000", 2);
    byte[] bytes = bi.toByteArray();
  }
}
```
