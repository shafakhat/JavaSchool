---
title: Java Algorithms How to - Calculate powers
nav: Java Algorithms How to - C...
description: int num = 2;//from w w w . j av a 2 s . c o m int pow = 3;
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Calculate_powers.htm
---
## Question

We would like to know how to calculate powers.

## Answer

```java title=Example.java
public class Main {
  public static void main(String args[]) {
    int num = 2;int pow = 3;
    System.out.print(power(num, pow));
  }
  public static int power(int a, int b) {
    int power = 1;
    for (int c = 0; c < b; c++)
      power *= a;
    return power;
  }
}
```

The code above generates the following result.
