---
title: How to do BigInteger bit and,or,xor,test,flip,negate
nav: How to do BigInteger bit a...
description: BigInteger andNot(BigInteger val) Returns a BigInteger whose value is (this & ~val).
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20130821213106/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_do_BigInteger_bit_and_or_xor_test_flip_negate.htm
---
In this chapter you will learn:

- How to calculate Big andNot on BigInteger
- How to get the number of bit in a BigInteger
- How to clear designated bit from BigInteger
- How to flip designated bit in BigInteger
- How to negate a BigInteger
- How to do not operation on BigInteger
- How to do or operation on a BigInteger
- How to set bit value on BigInteger
- If the designated bit is set
- How to do bit xor calculation on BigInteger

### Big andNot on BigInteger

BigInteger andNot(BigInteger val) Returns a BigInteger whose value is (this & ~val).

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.andNot(bi);
  }
}
```

The output:

### Get the number of bit in a BigInteger

int bitLength() Returns the number of bits in the minimal two's-complement representation of this BigInteger, excluding a sign bit.

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String args[]) {
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

### Clear designated bit from BigInteger

BigInteger clearBit(int n) Returns a BigInteger whose value is equivalent to this BigInteger with the designated bit cleared.

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.clearBit(3);
  }
}
```

The output:

### Flip designated bit in BigInteger

BigInteger flipBit(int n) returns a BigInteger whose value is equivalent to this BigInteger with the designated bit flipped.

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.flipBit(3);
    System.out.println(bi);
  }
}
```

The output:

### Negate a BigInteger

BigInteger negate() returns a BigInteger whose value is (-this).

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    BigInteger bi1 = new BigInteger("1234567890123456890");
    bi1 = bi1.negate();
    System.out.println(bi1);
  }
}
```

The output:

### Not operation on BigInteger

BigInteger not() returns a BigInteger whose value is (~this).

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.not();
  }
}
```

### or a BigInteger

BigInteger or(BigInteger val) returns a BigInteger whose value is (this | val).

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.or(bi);
  }
}
```

### Set bit value on BigInteger

BigInteger setBit(int n) returns a BigInteger whose value is equivalent to this BigInteger with the designated bit set.

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.setBit(3);
    System.out.println(bi);
  }
}
```

The output:

### If the designated bit is set

boolean testBit(int n) Returns true if and only if the designated bit is set.

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    boolean b = bi.testBit(3);
    b = bi.testBit(16);
    System.out.println(b);
  }
}
```

The output:

### Bit xor calculation on BigInteger

BigInteger xor(BigInteger val) Returns a BigInteger whose value is (this ^ val).

```java title=Example.java
import java.math.BigInteger;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    byte[] bytes = newbyte[] { 0x1, 0x00, 0x00 };
    BigInteger bi = new BigInteger(bytes);
    bi = bi.xor(bi);
    System.out.println(bi);
  }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- How to left shift bit value on BigInteger
- How to right shift bit on BigInteger

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
