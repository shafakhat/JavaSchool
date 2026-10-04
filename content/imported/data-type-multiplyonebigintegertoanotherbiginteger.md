---
title: Multiply one BigInteger to another BigInteger
nav: Multiply one BigInteger to...
description: Imported from the java2s.com archive: Multiply one BigInteger to another BigInteger
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/MultiplyoneBigIntegertoanotherBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi1 = new BigInteger("1234567890123456890");
    BigInteger bi2 = BigInteger.valueOf(123L);
    bi1 = bi1.multiply(bi2);
  }
}
```
