---
title: Get the value of a bit
nav: Get the value of a bit
description: Imported from the java2s.com archive: Get the value of a bit
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getthevalueofabit.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    boolean b = bi.testBit(3);
    b = bi.testBit(16);
  }
}
```
