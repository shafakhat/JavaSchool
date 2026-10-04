---
title: Do math operation for BigInteger
nav: Do math operation for BigI...
description: Imported from the java2s.com archive: Do math operation for BigInteger
section: Imported - java2s Archive
order: 1311
source: https://web.archive.org/web/20140829080012/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DomathoperationforBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] args) {
    BigInteger numberA = new BigInteger("98765432123456789");
    BigInteger numberB = BigInteger.TEN;
    numberA = numberA.add(numberB);
    System.out.println("numberA = " + numberA);
    numberA = numberA.multiply(numberB);
    System.out.println("numberA = " + numberA);
    numberA = numberA.subtract(numberB);
    System.out.println("numberA = " + numberA);
    numberA = numberA.divide(numberB);
    System.out.println("numberA = " + numberA);
    numberA = numberA.mod(numberB);
    System.out.println("numberA = " + numberA);
    numberA = numberA.pow(2);
    System.out.println("numberA = " + numberA);
    numberA = numberA.negate();
    System.out.println("numberA = " + numberA);
  }
}
```
