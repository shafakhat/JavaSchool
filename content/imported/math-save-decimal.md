---
title: Java Algorithms How to - Save decimal
nav: Java Algorithms How to - S...
description: System.out.println(String.format("operation : %s", operation));
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Save_decimal.htm
---
## Question

We would like to know how to save decimal.

## Answer

```java title=Example.java
import java.math.BigDecimal;
import java.math.RoundingMode;
public class Main {
  public static void main(String[] args) {
    double operation = 890.0 / 1440.0;
    BigDecimal big = new BigDecimal(operation);
    big = big.setScale(4, RoundingMode.HALF_UP);
    double d2 = big.doubleValue();
    System.out.println(String.format("operation : %s", operation));
    System.out.println(String.format("scaled : %s", d2));
  }
}
```

The code above generates the following result.
