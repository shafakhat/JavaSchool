---
title: Java Algorithms How to - Get the prime numbers
nav: Java Algorithms How to - G...
description: Imported from the java2s.com archive: Java Algorithms How to - Get the prime numbers
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20160731162540/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Get_the_prime_numbers.htm
---
```java title=Example.java
Back to Math  ↑
```

## Question

We would like to know how to get the prime numbers.

## Answer

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] args) {
    int i = 0;
    while (true) {
      if (i > 1000) {
        break;
      }
      if (i > 1) {
        if (new BigInteger(i+"").isProbablePrime(i / 2)) {
          System.out.println(i);
        }
      }
      i++;
    }
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Math  ↑
```
