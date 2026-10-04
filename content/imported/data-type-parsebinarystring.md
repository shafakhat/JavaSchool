---
title: Parse binary string
nav: Parse binary string
description: Imported from the java2s.com archive: Parse binary string
section: Imported - java2s Archive
order: 1310
source: https://web.archive.org/web/20140829080442/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parsebinarystring.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("100101000111111110000", 2);
    byte[] bytes = bi.toByteArray();
  }
}
```
