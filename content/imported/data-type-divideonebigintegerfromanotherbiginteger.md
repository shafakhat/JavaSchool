---
title: Divide one BigInteger from another BigInteger
nav: Divide one BigInteger from...
description: Imported from the java2s.com archive: Divide one BigInteger from another BigInteger
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DivideoneBigIntegerfromanotherBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    BigInteger bi1 = new BigInteger("1234567890123456890");
    BigInteger bi2 = BigInteger.valueOf(123L);
    bi1 = bi1.divide(bi2);
  }
}
```
