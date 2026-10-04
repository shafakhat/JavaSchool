---
title: How to calculate exponent and mod power of BigInteger
nav: How to calculate exponent ...
description: BigInteger pow(int exponent) returns a BigInteger whose value is (thisexponent).
section: Imported - java2s Archive
order: 1165
source: https://web.archive.org/web/2018/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_calculate_exponent_and_mod_power_of_BigInteger.htm
---
In this chapter you will learn:

- How to calculate Power of BigInteger
- How to BigInteger Mod Power

### BigInteger's Power

BigInteger pow(int exponent) returns a BigInteger whose value is (thisexponent).

```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi1 = new BigInteger("1234567890123456890");
    int exponent = 2;
    bi1 = bi1.pow(exponent);
    System.out.println(bi1);
  }
}
```

The output:

### BigInteger Mod Power

BigInteger modPow(BigInteger exponent, BigInteger m) returns a BigInteger whose value is (thisexponent mod m).

```java title=Example.java
import java.math.BigInteger;
import java.security.SecureRandom;
public class Main {
  public static void main(String[] args) throws Exception {
    int bitLength = 512; // 512 bits
    SecureRandom rnd = new SecureRandom();
    int certainty = 90; // 1 - 1/2(90) certainty
    System.out.println("BitLength : " + bitLength);
    BigInteger mod = new BigInteger(bitLength, certainty, rnd);
    BigInteger exponent = BigInteger.probablePrime(bitLength, rnd);
    BigInteger n = BigInteger.probablePrime(bitLength, rnd);
    BigInteger result = n.modPow(exponent, mod);
    System.out.println("Number ^ Exponent MOD Modulus = Result");
    System.out.println("Number");
    System.out.println(n);
    System.out.println("Exponent");
    System.out.println(exponent);
    System.out.println("Modulus");
    System.out.println(mod);
    System.out.println("Result");
    System.out.println(result);
  }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- How to convert BigInteger to double value
- How to convert BigInteger to byte array
- How to convert long type value to BigInteger

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
