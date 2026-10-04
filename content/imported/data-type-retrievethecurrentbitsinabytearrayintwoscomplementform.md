---
title: Retrieve the current bits in a byte array in twos-complement form.
nav: Retrieve the current bits ...
description: Imported from the java2s.com archive: Retrieve the current bits in a byte array in twos-complement form.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Retrievethecurrentbitsinabytearrayintwoscomplementform.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[]  bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bytes = bi.toByteArray();
  }
}
```
