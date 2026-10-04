---
title: Truncates the big decimal value
nav: Truncates the big decimal ...
description: Imported from the java2s.com archive: Truncates the big decimal value
section: Imported - java2s Archive
order: 1133
source: https://web.archive.org/web/20110203023000/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Truncatesthebigdecimalvalue.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String[] argv) throws Exception {
    int decimalPlaces = 2;
    BigDecimal bd = new BigDecimal("123456789.0123456890");
    bd = bd.setScale(decimalPlaces, BigDecimal.ROUND_DOWN);
    String string = bd.toString();
  }
}
```
