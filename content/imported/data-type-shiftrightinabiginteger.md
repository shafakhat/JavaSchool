---
title: Shift right in a BigInteger
nav: Shift right in a BigInteger
description: Imported from the java2s.com archive: Shift right in a BigInteger
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ShiftrightinaBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] bytes = new byte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.shiftRight(1);
  }
}
```
