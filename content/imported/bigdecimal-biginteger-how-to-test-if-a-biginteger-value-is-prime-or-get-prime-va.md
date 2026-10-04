---
title: How to test if a BigInteger value is prime or get prime value from BigInteger
nav: How to test if a BigIntege...
description: boolean isProbablePrime(int certainty) returns true if this BigInteger is probably prime, false if it's definitely composite.
section: Imported - java2s Archive
order: 1158
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_test_if_a_BigInteger_value_is_prime_or_get_prime_value_from_BigInteger.htm
---
In this chapter you will learn:

- How to know if a BigInteger value prime
- How to generate a prime number from BigInteger

### Is a BigInteger value prime

boolean isProbablePrime(int certainty) returns true if this BigInteger is probably prime, false if it's definitely composite.

```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String args[]) {
    BigInteger n = new BigInteger("1000000000000");
    BigInteger one = new BigInteger("1");
    while (!n.isProbablePrime(7))
      n = n.add(one);
    System.out.println(n.toString(10) + " is probably prime.");
    System.out.println("It is " + n.bitLength() + " bits in length.");
  }
}
```

The output:

### Get a prime number from BigInteger

probablePrime(int bitLength, Random rnd) returns a positive BigInteger that is probably prime, with the specified bitLength.

```java title=Example.java
import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.Random;
public class MainClass {
  public static void main(String[] unused) {
    Random prng = new SecureRandom();  // self-seeding
    System.out.println(BigInteger.probablePrime(10, prng));
  }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- When to use BigDecimal
- Why BigDecimal is good for monetary values

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
