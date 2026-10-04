---
title: How to create Java BigDecimal
nav: How to create Java BigDeci...
description: BigDecimal(BigInteger unscaledVal, int scale, MathContext mc) converts a BigInteger and an int scale into a BigDecimal, with rounding according to the context settings.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20130831023920/http://java2s.com/Tutorials/Java/BigDecimal_BigInteger/How_to_create_Java_BigDecimal.htm
---
In this chapter you will learn:

- How to create BigDecimal from MathContext

### Create BigDecimals

BigDecimal(double val) converts a double into a BigDecimal.

```java title=Example.java
import java.math.BigDecimal;
 /*java2s.com*/publicclass Main {

    publicstaticvoid main(String[] args) {
        System.out.println(new BigDecimal(1f));
        System.out.println(new BigDecimal(2f));

    }
}
```

The output:

### Create BigDecimal from MathContext

BigDecimal(BigInteger unscaledVal, int scale, MathContext mc) converts a BigInteger and an int scale into a BigDecimal, with rounding according to the context settings.

```java title=Example.java
import java.math.BigDecimal;
import java.math.MathContext;
 //java2s.compublicclass Main {

    publicstaticvoid main(String[] args) {
        BigDecimal first = new BigDecimal(1f);
        BigDecimal second = new BigDecimal(1000f);

        BigDecimal result1 = new BigDecimal(first.doubleValue() / second.doubleValue());
        BigDecimal result2 = first.divide(second, MathContext.DECIMAL128);

        System.out.println(result1);
        System.out.println(result2);
        System.out.println((first.doubleValue() / second.doubleValue()));

    }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- What methods to use to do calculation on BigDecimal
- How to get absolute value from BigDecimal
- How to add two BigDecimal value together
- Calculating Euler's number e with BigDecimal
- Multiply one BigDecimal to another BigDecimal

#### BigDecimal

BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format

#### BigInteger

BigInteger class BigInteger creation BigInteger add, subtract, multiply and divide BigInteger power and modPow BigInteger conversion BigInteger to String BigInteger bit and,or,xor,test,flip,negate BigInteger bit shift left and right BigInteger prime value BigDecimal BigDecimal constants BigDecimal Rounding mode BigDecimal creation BigDecimal calculation BigDecimal convert BigDecimal Comparison BigDecimal to String BigDecimal decimal point BigDecimal precision BigDecimal format
