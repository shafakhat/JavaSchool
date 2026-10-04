---
title: Java Utililty Methods Array Dot Product
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Dot Product are organized into topic(s).
section: Imported - java2s Archive
order: 50058
source: https://www.java2s.com/example/java-utility-method/array-dot-product-index-0.html
---
List of utility methods to do Array Dot Product

## Description

The list of methods to do Array Dot Product are organized into topic(s).

## Method

doubledotProd(double x[], double y[]) dot Prod

```java title=Example.java
if (x.length != y.length)
    thrownewRuntimeException("Arrays must be same size");
double sum = 0;
for (int i = 0; i < x.length; i++)
    sum += x[i] * y[i];
return sum;
```

doubledotprod(double[] xlist, double[] ylist) dotprod

```java title=Example.java
double result = 0.0;
int size = Math.min(xlist.length, ylist.length);
int n = 0;
for (int i = 0; i < size; i++) {
    result += xlist[i] * ylist[i];
return result;
```

floatdotProd(float[] a, float[] b) dot Prod

```java title=Example.java
return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
```

doubledotProduct(double x1, double y1, double x2, double y2) dot Product

```java title=Example.java
return x1 * x2 + y1 * y2;
```

doubledotProduct(double x1, double y1, double x2, double y2, double x3, double y3) Return the dot product of the vector (x1, y1)(x2, y2) and the vector (x2, y2)(x3, y3).

```java title=Example.java
double nVx1 = x2 - x1;
double nVy1 = y2 - y1;
double nVx2 = x3 - x2;
double nVy2 = y3 - y2;
double nVMag1 = Math.sqrt(nVx1 * nVx1 + nVy1 * nVy1);
double nVMag2 = Math.sqrt(nVx2 * nVx2 + nVy2 * nVy2);
if ((nVMag1 == 0) || (nVMag2 == 0)) {
    return 1;
...
```

doubledotProduct(double[] a, double[] b) Computes the dot product of two vectors.

```java title=Example.java
if (a.length != b.length) {
    thrownewArithmeticException("The length of the vectors does not match!");
} else {
    double sum = 0;
    for (int i = 0; i < a.length; i++) {
        sum += a[i] * b[i];
    return sum;
...
```

doubledotProduct(double[] a, double[] b) Calculates the dot product between two vectors and returns as double

```java title=Example.java
double dotProduct = 0;
for (int i = 0; i < a.length; i++)
    dotProduct += a[i] * b[i];
return dotProduct;
```

floatdotProduct(double[] a, double[] b) Returns the dot product between two vectors

```java title=Example.java
if (a.length != b.length) {
    thrownewIllegalArgumentException(
            "Error computing dotProduct in Utilities.dotProduct: arrays should have the same length");
float sp = 0;
for (int i = 0; i < a.length; i++) {
    sp += a[i] * b[i];
return sp;
```

DoubledotProduct(Double[] a, Double[] b) dot Product

```java title=Example.java
return (a[0] * b[0]) + (a[1] * b[1]);
```

doubledotProduct(double[] array, int[] indices, double[] values) dot Product

```java title=Example.java
double result = 0;
for (int i = 0; i < indices.length; i++) {
    if (indices[i] == -1)
        continue;
    result += array[indices[i]] * values[i];
return result;
```
