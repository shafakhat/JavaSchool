---
title: Java Utililty Methods acot
nav: Java Utililty Methods acot
description: doubleacot(final T value) Return the arcus cotangens of value in radian.
section: Imported - java2s Archive
order: 50011
source: https://www.java2s.com/example/java-utility-method/acot-index-0.html
---
List of utility methods to do acot

## Description

The list of methods to do acot are organized into topic(s).

## Method

doubleacot(double x) Returns the arc cotangent of a value.

```java title=Example.java
returnMath.atan(1.0 / x);
```

doubleacot(double x) acot

```java title=Example.java
if (x != 0) {
    returnMath.atan(1 / x);
} else {
    thrownewArithmeticException();
```

doubleacot(final T value) Return the arcus cotangens of value in radian.

```java title=Example.java
double rc;
double d = value.doubleValue();
if (0D == d) {
    rc = PI_HALF;
elseif (d > 0D) {
    rc = Math.atan(1D / d);
else {
    rc = Math.PI + Math.atan(1D / d);
return rc;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
