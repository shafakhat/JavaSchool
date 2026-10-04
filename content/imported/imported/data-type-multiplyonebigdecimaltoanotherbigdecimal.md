---
title: Multiply one BigDecimal to another BigDecimal
nav: Multiply one BigDecimal to...
description: Imported from the java2s.com archive: Multiply one BigDecimal to another BigDecimal
section: Imported - java2s Archive
order: 1155
source: https://web.archive.org/web/20110204050854/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/MultiplyoneBigDecimaltoanotherBigDecimal.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigDecimal bd1 = new BigDecimal("123456789.0123456890");
    // Create via a long
    BigDecimal bd2 = BigDecimal.valueOf(123L);
    bd1 = bd1.multiply(bd2);
  }
}
```
