---
title: Operate with big decimal values
nav: Operate with big decimal v...
description: Imported from the java2s.com archive: Operate with big decimal values
section: Imported - java2s Archive
order: 1162
source: https://web.archive.org/web/20110204051336/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Operatewithbigdecimalvalues.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Create via a string
    BigDecimal bd1 = new BigDecimal("123456789.0123456890");
    // Create via a long
    BigDecimal bd2 = BigDecimal.valueOf(123L);
    bd1 = bd1.add(bd2);
    bd1 = bd1.multiply(bd2);
    bd1 = bd1.subtract(bd2);
    bd1 = bd1.divide(bd2, BigDecimal.ROUND_UP);
    bd1 = bd1.negate();
  }
}
```
