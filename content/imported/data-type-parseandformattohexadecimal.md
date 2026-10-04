---
title: Parse and format to hexadecimal
nav: Parse and format to hexade...
description: Imported from the java2s.com archive: Parse and format to hexadecimal
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20140316034835/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parseandformattohexadecimal.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("3ff", 16);
    String s = bi.toString(16);
  }
}
```
