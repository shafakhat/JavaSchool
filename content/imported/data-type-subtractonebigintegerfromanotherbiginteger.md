---
title: Subtract one BigInteger from another BigInteger
nav: Subtract one BigInteger fr...
description: Imported from the java2s.com archive: Subtract one BigInteger from another BigInteger
section: Imported - java2s Archive
order: 1298
source: https://web.archive.org/web/20140423020642/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SubtractoneBigIntegerfromanotherBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi1 = new BigInteger("1234567890123456890");
    BigInteger bi2 = BigInteger.valueOf(123L);
    bi1 = bi1.subtract(bi2);
  }
}
```
