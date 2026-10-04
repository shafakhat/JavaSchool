---
title: How to control Java BigDecimal precision
nav: How to control Java BigDec...
description: BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecim
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20130821180432/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_control_Java_BigDecimal_precision.htm
---
In this chapter you will learn:

- Methods to control BigDecimal's precision

### Methods to control BigDecimal's precision

- int precision() Returns the precision.
- int scale() Returns the scale.
- BigDecimal setScale(int newScale) Change the scale.
- BigDecimal setScale(int newScale, int roundingMode) Set scale with rounding Mode.
- BigDecimal setScale(int newScale, RoundingMode roundingMode) Set scale with rounding Mode.
- int signum() Returns the signum function of this BigDecimal.
- BigInteger unscaledValue() Get the unscaled value.
- BigDecimal ulp() Returns the size of an ulp(a unit in the last place).

```java title=Example.java
import java.math.BigDecimal;
 //java2s.compublicclass Main {

    publicstaticvoid main(String[] args) {
        BigDecimal first = new BigDecimal(10f);
        System.out.println(first);
        System.out.println(first.precision());
        System.out.println(first.setScale(3));
    }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- How to remove trailing zeros

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
