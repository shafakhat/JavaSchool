---
title: Subtract from one BigDecimal another BigDecimal
nav: Subtract from one BigDecim...
description: Imported from the java2s.com archive: Subtract from one BigDecimal another BigDecimal
section: Imported - java2s Archive
order: 1211
source: https://web.archive.org/web/20110204051224/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/SubtractfromoneBigDecimalanotherBigDecimal.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigDecimal bd1 = new BigDecimal("123456789.0123456890");
    // Create via a long
    BigDecimal bd2 = BigDecimal.valueOf(123L);
    bd1 = bd1.subtract(bd2);
  }
}
```
