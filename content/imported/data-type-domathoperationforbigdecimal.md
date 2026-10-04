---
title: Do math operation for BigDecimal
nav: Do math operation for BigD...
description: Imported from the java2s.com archive: Do math operation for BigDecimal
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20110204051520/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/DomathoperationforBigDecimal.htm
---
```java title=Example.java
import java.math.BigDecimal;
public class Main {
  public static void main(String[] args) {
    BigDecimal decimalA = new BigDecimal("123456789012345");
    BigDecimal decimalB = new BigDecimal("10");
    decimalA = decimalA.add(decimalB);
    System.out.println("decimalA = " + decimalA);
    decimalA = decimalA.multiply(decimalB);
    System.out.println("decimalA = " + decimalA);
    decimalA = decimalA.subtract(decimalB);
    System.out.println("decimalA = " + decimalA);
    decimalA = decimalA.divide(decimalB);
    System.out.println("decimalA = " + decimalA);
    decimalA = decimalA.pow(2);
    System.out.println("decimalA = " + decimalA);
    decimalA = decimalA.negate();
    System.out.println("decimalA = " + decimalA);
  }
}
```
