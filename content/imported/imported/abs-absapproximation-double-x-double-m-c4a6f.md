---
title: Java Abs absApproximation(double x, double M)
nav: Java Abs absApproximation(...
description: Here you can find the source of absApproximation(double x, double M)
section: Imported
order: 20008
source: http://www.java2s.com/example/java-utility-method/abs/absapproximation-double-x-double-m-c4a6f.html
---
Here you can find the source of absApproximation(double x, double M)

## Description

abs Approximation

## License

Open Source License

## Declaration

```java title=Example.java
publicstaticdouble absApproximation(double x, double M)
```

## Method Source Code

```java title=Example.java
//package com.java2s;publicclass Main {
publicstaticdouble absApproximation(double x, double M) {return huberPenaltyFunction(x, M) / (2 * M);
    }/*fromwww.java2s.com*//**
     * This function computes the Huber penalty function of an
     * input. The Huber penalty function is equal to x^2 for |x| <= M,
     * and linear for |x| > M.
     * @param x the value at which to compute the Huber penalty function
     * @param M the parameter which determines the linear/quadratic region
     * @return The Huber penalty function at x
     */publicstaticdouble huberPenaltyFunction(double x, double M) {
        if (Math.abs(x) <= M) {
            return x * x;
        } else {
            return M * (2 * Math.abs(x) - M);
        }
    }
}
```

## Related

- abs2(double[][] IN)
- abs2(float[] f)
- abs_fractional(double number)
- abs_min(double a, double b)
- absAngleDifference(double angle1Radians, double angle2Radians)
- absCap(double value, double bounds)
- absClamp(double value, double bounds)
- absDegrees(double degrees)
- absDelta(double a, double b)

[HOME](http://www.java2s.com) | Copyright © www.java2s.com 2016
