---
title: Create a BigDecimal vis string
nav: Create a BigDecimal vis st...
description: Imported from the java2s.com archive: Create a BigDecimal vis string
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreateaBigDecimalvisstring.htm
---
```java title=Example.java
import java.math.BigDecimal;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    // Create via a string
    BigDecimal bd1 = new BigDecimal("123456789.0123456890");
    // Create via a long
    BigDecimal bd2 = BigDecimal.valueOf(123L);
    bd1 = bd1.add(bd2);
  }
}
```
