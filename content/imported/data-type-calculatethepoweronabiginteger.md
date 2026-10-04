---
title: Calculate the power on a BigInteger
nav: Calculate the power on a B...
description: Imported from the java2s.com archive: Calculate the power on a BigInteger
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CalculatethepoweronaBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    BigInteger bi1 = new BigInteger("1234567890123456890");
    int exponent = 2;
    bi1 = bi1.pow(exponent);
  }
}
```
