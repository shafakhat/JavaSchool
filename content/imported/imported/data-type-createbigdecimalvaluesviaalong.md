---
title: Create Big Decimal Values via a long
nav: Create Big Decimal Values ...
description: Imported from the java2s.com archive: Create Big Decimal Values via a long
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20110204050844/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/CreateBigDecimalValuesviaalong.htm
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
  }
}
```
