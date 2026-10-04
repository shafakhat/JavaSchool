---
title: Negate a BigDecimal
nav: Negate a BigDecimal
description: Imported from the java2s.com archive: Negate a BigDecimal
section: Imported - java2s Archive
order: 1157
source: https://web.archive.org/web/20110204050957/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/NegateaBigDecimal.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigDecimal bd1 = new BigDecimal("123456789.0123456890");
    bd1 = bd1.negate();
  }
}
```
