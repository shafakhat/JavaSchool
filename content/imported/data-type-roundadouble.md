---
title: Round a double
nav: Round a double
description: Imported from the java2s.com archive: Round a double
section: Imported - java2s Archive
order: 1314
source: https://web.archive.org/web/2018/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Roundadouble.htm
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

| 2.46.1. | Round a double |
|---|---|
| 2.46.2. | Create Big Decimal Values via a long |
| 2.46.3. | Create a BigDecimal vis string |
| 2.46.4. | Multiply one BigDecimal to another BigDecimal |
| 2.46.5. | Subtract from one BigDecimal another BigDecimal |
| 2.46.6. | Divide one BigDecimal from another BigDecimal |
| 2.46.7. | Negate a BigDecimal |
| 2.46.8. | Setting the Decimal Place of a Big Decimal Value |
| 2.46.9. | Truncates the big decimal value |
| 2.46.10. | Do math operation for BigDecimal |
| 2.46.11. | Operate with big decimal values |
| 2.46.12. | Create Big Decimal Values via a string |
| 2.46.13. | Convert Object to BigDecimal |
