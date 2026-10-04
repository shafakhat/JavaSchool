---
title: Create BigInteger via string
nav: Create BigInteger via string
description: Imported from the java2s.com archive: Create BigInteger via string
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreateBigIntegerviastring.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    // Create via a string
    BigInteger bi1 = new BigInteger("1234567890123456890");
    // Create via a long
    BigInteger bi2 = BigInteger.valueOf(123L);
    bi1 = bi1.add(bi2);
  }
}
```
