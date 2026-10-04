---
title: not operation for BigInteger
nav: not operation for BigInteger
description: Imported from the java2s.com archive: not operation for BigInteger
section: Imported - java2s Archive
order: 1312
source: https://web.archive.org/web/20140829075730/http://www.java2s.com/Tutorial/Java/0040__Data-Type/notoperationforBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] bytes = new byte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.not();
  }
}
```
