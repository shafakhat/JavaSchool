---
title: or operation for BigInteger
nav: or operation for BigInteger
description: Imported from the java2s.com archive: or operation for BigInteger
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/oroperationforBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.or(bi);
  }
}
```
