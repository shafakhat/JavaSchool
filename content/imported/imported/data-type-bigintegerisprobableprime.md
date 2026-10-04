---
title: BigInteger.isProbablePrime
nav: BigInteger.isProbablePrime
description: System.out.println("It is " + n.bitLength() + " bits in length.");
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/BigIntegerisProbablePrime.htm
---
```java title=Example.java
import java.math.BigInteger;

publicclass BigNumApp {
  publicstaticvoid main(String args[]) {
    BigInteger n = new BigInteger("1000000000000");
    BigInteger one = new BigInteger("1");
    while (!n.isProbablePrime(7))
      n = n.add(one);
    System.out.println(n.toString(10) + " is probably prime.");
    System.out.println("It is " + n.bitLength() + " bits in length.");
  }
}
```
