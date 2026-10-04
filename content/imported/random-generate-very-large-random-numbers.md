---
title: Java Algorithms How to - Generate very large random numbers
nav: Java Algorithms How to - G...
description: We would like to know how to generate very large random numbers.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20160730055239/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_very_large_random_numbers.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate very large random numbers.

## Answer

```java title=Example.java
import java.math.BigInteger;
import java.util.Random;
publicclass Main {
  publicstaticvoid main(String... a) {
    int n = 16;
    Random r = new Random();
    byte[] b = newbyte[n];
    r.nextBytes(b);
    BigInteger i = new BigInteger(b);
    System.out.println(i);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
