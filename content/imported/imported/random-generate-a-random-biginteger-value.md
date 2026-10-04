---
title: Java Algorithms How to - Generate a random BigInteger value
nav: Java Algorithms How to - G...
description: We would like to know how to generate a random BigInteger value.
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20160730062620/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_a_random_BigInteger_value.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate a random BigInteger value.

## Answer

```java title=Example.java
/*www.java2s.com*/import java.math.BigInteger;
import java.util.Random;

publicclass Main {
  publicstaticvoid main(String[] args) {
    BigInteger bigInteger = new BigInteger("2000000000000");// uper limit
    BigInteger min = new BigInteger("1000000000");// lower limit
    BigInteger bigInteger1 = bigInteger.subtract(min);
    Random rnd = new Random();
    int maxNumBitLength = bigInteger.bitLength();

    BigInteger aRandomBigInt;

    aRandomBigInt = new BigInteger(maxNumBitLength, rnd);
    if (aRandomBigInt.compareTo(min) < 0)
      aRandomBigInt = aRandomBigInt.add(min);
    if (aRandomBigInt.compareTo(bigInteger) >= 0)
      aRandomBigInt = aRandomBigInt.mod(bigInteger1).add(min);

    System.out.println(aRandomBigInt);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
