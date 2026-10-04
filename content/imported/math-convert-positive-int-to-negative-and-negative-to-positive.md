---
title: Java Algorithms How to - Convert positive int to negative and negative to positive
nav: Java Algorithms How to - C...
description: We would like to know how to convert positive int to negative and negative to positive.
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20160731162403/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Convert_positive_int_to_negative_and_negative_to_positive.htm
---
```java title=Example.java
Back to Math  ↑
```

## Question

We would like to know how to convert positive int to negative and negative to positive.

## Answer

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) throws java.lang.Exception {
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

```java title=Example.java
Back to Math  ↑
```
