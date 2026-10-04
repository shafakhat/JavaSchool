---
title: How to create Java BigInteger
nav: How to create Java BigInte...
description: BigInteger(byte[] val) Translates a byte array containing the two's-complement binary representation of a BigInteger into a BigInteger.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_create_Java_BigInteger.htm
---
In this chapter you will learn:

- How to create BigInteger from byte array
- How to create BigInteger from String
- How to use different radix to create BigInteger from String
- How to create BigInteger with random number

### Create BigInteger from byte array

BigInteger(byte[] val) Translates a byte array containing the two's-complement binary representation of a BigInteger into a BigInteger.

The following code use new BigInteger(byte[] val) to create a BigInteger.

```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    // A negative value
 byte[] bytes = new byte[] { (byte) 0xFF, 0x00, 0x00 }; // -65536
 // A positive value
    bytes = new byte[] { 0x1, 0x00, 0x00 }; // 65536
    BigInteger bi = new BigInteger(bytes);
  }
}
```

### Create BigInteger from String

BigInteger(String val) translates the decimal String representation of a BigInteger into a BigInteger.

The following code use new BigInteger(String val)to create a BigInteger.

```java title=Example.java
import java.math.BigInteger;
public class MainClass {
  public static void main(String[] args) {
    System.out.println("Here's Long.MAX_VALUE: " + Long.MAX_VALUE);
    BigInteger bInt = new BigInteger("3419229223372036854775807");
    System.out.println("Here's a bigger number: " + bInt);
    System.out.println("Here it is as a double: " + bInt.doubleValue());
  }
}
```

The code above generates the following result.

### Use different radix to create BigInteger from String

BigInteger(String val, int radix) translates the String representation of a BigInteger in the specified radix into a BigInteger.

You can set the radix for the string value passed in with new BigInteger(String val, int radix).

```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    BigInteger bi = new BigInteger("4407760", 8);
  }
}
```

### Create BigInteger with random number

new BigInteger(int bitLength, int certainty, Random rnd) creates a BigInteger with a random number

```java title=Example.java
import java.math.BigInteger;
import java.security.SecureRandom;
public class Main {
  public static void main(String[] args) throws Exception {
    int bitLength = 512; // 512 bits
    SecureRandom rnd = new SecureRandom();
    int certainty = 90; // 1 - 1/2(90) certainty
    BigInteger mod = new BigInteger(bitLength, certainty, rnd);
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- How to add two BigInteger values together
- How to subtract one BigInteger with another BigInteger
- How to multiply two BigInteger values
- How ot divide one BigInteger from another BigInteger

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
