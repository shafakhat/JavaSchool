---
title: Divide one BigDecimal from another BigDecimal
nav: Divide one BigDecimal from...
description: Imported from the java2s.com archive: Divide one BigDecimal from another BigDecimal
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DivideoneBigDecimalfromanotherBigDecimal.htm
---
```java title=Example.java
import java.math.BigDecimal;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    BigDecimal bd1 = new BigDecimal("123456789.0123456890");
    // Create via a long
    BigDecimal bd2 = BigDecimal.valueOf(123L);
    bd1 = bd1.divide(bd2, BigDecimal.ROUND_UP);
  }
}
```
