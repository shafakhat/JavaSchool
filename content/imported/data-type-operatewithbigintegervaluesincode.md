---
title: Operate with big integer values in code
nav: Operate with big integer v...
description: Imported from the java2s.com archive: Operate with big integer values in code
section: Imported - java2s Archive
order: 1313
source: https://web.archive.org/web/20140829075926/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Operatewithbigintegervaluesincode.htm
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
    bi1 = bi1.multiply(bi2);
    bi1 = bi1.subtract(bi2);
    bi1 = bi1.divide(bi2);
    bi1 = bi1.negate();
    int exponent = 2;
    bi1 = bi1.pow(exponent);
  }
}
```
