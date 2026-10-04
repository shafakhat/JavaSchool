---
title: Java Algorithms How to - Convert positive int to negative and negative to positive
nav: Java Algorithms How to - C...
description: We would like to know how to convert positive int to negative and negative to positive.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Convert_positive_int_to_negative_and_negative_to_positive.htm
---
## Question

We would like to know how to convert positive int to negative and negative to positive.

## Answer

```java title=Example.java
public class Main {
  public static void main(String[] args) throws java.lang.Exception {
    int iPositive = 15;
    int iNegative = (~(iPositive - 1));
    System.out.println(iNegative);
    iPositive = ~(iNegative - 1);
    System.out.println(iPositive);
    iNegative = 0;
    iPositive = ~(iNegative - 1);
    System.out.println(iPositive);
  }
}
```

The code above generates the following result.
