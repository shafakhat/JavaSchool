---
title: Convert BigInteger into another radix number
nav: Convert BigInteger into an...
description: Imported from the java2s.com archive: Convert BigInteger into another radix number
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertBigIntegerintoanotherradixnumber.htm
---
```java title=Example.java
import java.math.BigInteger;

publicclass Main {
  publicstaticvoid main(String[] args) {
    BigInteger number = new BigInteger("2008");

    System.out.println("Number      = " + number);
    System.out.println("Binary      = " + number.toString(2));
    System.out.println("Octal       = " + number.toString(8));
    System.out.println("Hexadecimal = " + number.toString(16));

    number = new BigInteger("FF", 16);
    System.out.println("Number      = " + number);
    System.out.println("Number      = " + number.toString(16));
  }
}
```
