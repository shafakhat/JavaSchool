---
title: Operating with Big Integer Values
nav: Operating with Big Integer...
description: Imported from the java2s.com archive: Operating with Big Integer Values
section: Imported - java2s Archive
order: 1297
source: https://web.archive.org/web/20140829075838/http://www.java2s.com/Tutorial/Java/0040__Data-Type/OperatingwithBigIntegerValues.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Create via a string
    BigInteger bi1 = new BigInteger("1234567890123456890");
    // Create via a long
    BigInteger bi2 = BigInteger.valueOf(123L);
    bi1 = bi1.add(bi2);
  }
}
```
