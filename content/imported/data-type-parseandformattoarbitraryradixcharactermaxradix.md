---
title: Parse and format to arbitrary radix <= Character.MAX_RADIX
nav: Parse and format to arbitr...
description: Imported from the java2s.com archive: Parse and format to arbitrary radix <= Character.MAX_RADIX
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParseandformattoarbitraryradixCharacterMAXRADIX.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    int radix = 32;
    BigInteger bi = new BigInteger("vv", radix);
    String s = bi.toString(radix);
  }
}
```
