---
title: Java Utililty Methods acos
nav: Java Utililty Methods acos
description: doubleacos(double a) Returns the arc cosine of an angle, in the range of 0.0 through pi.
section: Imported - java2s Archive
order: 50009
source: https://www.java2s.com/example/java-utility-method/acos-index-0.html
---
List of utility methods to do acos

## Description

The list of methods to do acos are organized into topic(s).

## Method

doubleacos(double a) Returns the arc cosine of an angle, in the range of 0.0 through pi.

```java title=Example.java
returnMath.acos(a);
```

doubleacos(double a) Returns the arc cosine of an angle, in the range of 0 through pi.

```java title=Example.java
double z, p, q, r, w, s, c, df;
long hx = Double.doubleToLongBits(a);
long ix = hx & no_sign_mask;
if (Math.abs(a) >= 1) {
    if (ix == one) {
        if (hx > 0)
            return (0.0);
        else
...
```

doubleacos(double d) Wrapper implementation of

```java title=Example.java
Math.acos()
```

.

```java title=Example.java
returnMath.acos(d);
```

doubleacos(double x) acos

```java title=Example.java
double f = asin(x);
if (f == Double.NaN)
    return f;
returnMath.PI / 2 - f;
```

doubleacos(double x) acos

```java title=Example.java
return PI_2 - arcsin(x);
```

floatacos(final float a) acos

```java title=Example.java
return (float) java.lang.Math.acos(a);
```

floatacos(float value) acos

```java title=Example.java
return (float) Math.acos(value);
```

floatacos(float value) acos

```java title=Example.java
return (float) Math.acos(value);
```

floatacos(float value) acos

```java title=Example.java
return (float) Math.acos(value);
```

floatacos(float x) Arccos

```java title=Example.java
float f = asin(x);
if (Float.isNaN(f))
    return f;
return (float) Math.PI / 2 - f;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
