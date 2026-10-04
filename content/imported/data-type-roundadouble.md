---
title: Round a double
nav: Round a double
description: Imported from the java2s.com archive: Round a double
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20110204053340/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Roundadouble.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String args[]) {
    BigDecimal bd = new BigDecimal(3.14159);
    bd = bd.setScale(2, BigDecimal.ROUND_HALF_UP);
    System.out.println(bd);
  }
}
//3.14
```
