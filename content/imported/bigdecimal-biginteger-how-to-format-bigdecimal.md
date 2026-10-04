---
title: How to format BigDecimal
nav: How to format BigDecimal
description: BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecim
section: Imported - java2s Archive
order: 1157
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_format_BigDecimal.htm
---
In this chapter you will learn:

- How to remove trailing zeros

### Remove trailing zeros

BigDecimal stripTrailingZeros() trailing zeros removed.

```java title=Example.java
import java.math.BigDecimal;
 public class Main {
    public static void main(String[] args) {
        BigDecimal first = new BigDecimal(100000f);
        System.out.println(first.stripTrailingZeros());
    }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- What are Java Classes
- How to create a class representing a box

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
