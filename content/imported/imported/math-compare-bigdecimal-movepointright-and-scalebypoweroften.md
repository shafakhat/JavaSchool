---
title: Java Algorithms How to - Compare BigDecimal movePointRight and scaleByPowerOfTen
nav: Java Algorithms How to - C...
description: We would like to know how to compare BigDecimal movePointRight and scaleByPowerOfTen.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20160731162528/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Compare_BigDecimal_movePointRight_and_scaleByPowerOfTen.htm
---
```java title=Example.java
Back to Math  ↑
```

## Question

We would like to know how to compare BigDecimal movePointRight and scaleByPowerOfTen.

## Answer

```java title=Example.java
import java.math.BigDecimal;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String... args) {
    long base = 12345;
    int scale = 4;

    BigDecimal number = BigDecimal.valueOf(base, scale);
    System.out.println(number);
    BigDecimal pointRight = number.movePointRight(5);
    System.out.println(pointRight + "; my scale is " + pointRight.scale());
    BigDecimal scaleBy = number.scaleByPowerOfTen(5);
    System.out.println(scaleBy + "; my scale is " + scaleBy.scale());
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Math  ↑
```
