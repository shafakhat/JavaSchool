---
title: Setting the Decimal Place of a Big Decimal Value
nav: Setting the Decimal Place ...
description: Imported from the java2s.com archive: Setting the Decimal Place of a Big Decimal Value
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20110202234942/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/SettingtheDecimalPlaceofaBigDecimalValue.htm
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
