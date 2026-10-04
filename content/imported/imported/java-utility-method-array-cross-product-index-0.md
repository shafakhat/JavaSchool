---
title: Java Utililty Methods Array Cross Product
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Cross Product are organized into topic(s).
section: Imported - java2s Archive
order: 50047
source: https://www.java2s.com/example/java-utility-method/array-cross-product-index-0.html
---
List of utility methods to do Array Cross Product

## Description

The list of methods to do Array Cross Product are organized into topic(s).

## Method

doublecross(double v0x, double v0y, double v1x, double v1y) Calculates the 'cross product' of two vectors.

```java title=Example.java
return v0x * v1y - v0y * v1x;
```

double[]cross(double v1[], double v2[]) Calculates cross product of two vectors.

```java title=Example.java
double v[] = newdouble[3];
v[0] = v1[1] * v2[2] - v1[2] * v2[1];
v[1] = v1[2] * v2[0] - v1[0] * v2[2];
v[2] = v1[0] * v2[1] - v1[1] * v2[0];
return v;
```

double[]cross(double[] p, double[] q) cross

```java title=Example.java
returnnewdouble[] { p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0] };
```

voidcross(double[] vec1, double[] vec2, double[] outvec) cross

```java title=Example.java
outvec[0] = vec1[1] * vec2[2] - vec1[2] * vec2[1];
outvec[1] = vec1[2] * vec2[0] - vec1[0] * vec2[2];
outvec[2] = vec1[0] * vec2[1] - vec1[1] * vec2[0];
```

voidcross(final double[] a, final double[] b, final double[] c) compute cross product, set c = a ^ b.

```java title=Example.java
c[0] = a[1] * b[2] - a[2] * b[1];
c[1] = a[2] * b[0] - a[0] * b[2];
c[2] = a[0] * b[1] - a[1] * b[0];
```

double[]cross(final double[] left, final double[] right) cross product or 2 3x1 vectors

```java title=Example.java
if ((left.length != 3) || (right.length != 3)) {
    System.out.println("ERROR: Invalid dimension in Cross(Vector,Vector)");
double[] Result = newdouble[3];
Result[0] = left[1] * right[2] - left[2] * right[1];
Result[1] = left[2] * right[0] - left[0] * right[2];
Result[2] = left[0] * right[1] - left[1] * right[0];
returnResult;
...
```

voidcross(float[] v1, float[] v2, float[] out) cross

```java title=Example.java
out[0] = v1[1] * v2[2] - v1[2] * v2[1];
out[1] = v1[2] * v2[0] - v1[0] * v2[2];
out[2] = v1[0] * v2[1] - v1[1] * v2[0];
```

float[]cross(float[] vec1, float[] vec2) cross product vec1 x vec2

```java title=Example.java
float[] out = newfloat[3];
out[0] = vec2[2] * vec1[1] - vec2[1] * vec1[2];
out[1] = vec2[0] * vec1[2] - vec2[2] * vec1[0];
out[2] = vec2[1] * vec1[0] - vec2[0] * vec1[1];
return out;
```

doublecross(int x1, int y1, int x2, int y2) cross

```java title=Example.java
return (x1 * y2) - (y1 * x2);
```

floatcross2D(final float[] v1, final float[] v2) Computes the cross product of two 2D vectors.

```java title=Example.java
return v1[0] * v2[1] - v1[1] * v2[0];
```
