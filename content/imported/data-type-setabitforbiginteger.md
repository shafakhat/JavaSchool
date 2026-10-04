---
title: Set a bit for BigInteger
nav: Set a bit for BigInteger
description: Imported from the java2s.com archive: Set a bit for BigInteger
section: Imported - java2s Archive
order: 1300
source: https://web.archive.org/web/20140829075634/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SetabitforBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] bytes = new byte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.setBit(3);
  }
}
```
