---
title: Java Utililty Methods Array Multiply
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Multiply are organized into topic(s).
section: Imported - java2s Archive
order: 50086
source: https://www.java2s.com/example/java-utility-method/array-multiply-index-0.html
---
List of utility methods to do Array Multiply

## Description

The list of methods to do Array Multiply are organized into topic(s).

## Method

double[][]mult(double[][] A, double[][] B) mult

```java title=Example.java
if (A.length != B.length)
    thrownewIllegalArgumentException("dim A != dim B");
double[][] AB = buildZeroMatrix(A.length);
for (int i = 0; i < A.length; i++) {
    for (int j = 0; j < A.length; j++) {
        AB[i][j] = 0;
        for (int k = 0; k < A.length; k++) {
            AB[i][j] += A[i][k] * B[k][j];
...
```

float[]mult(float[] nums, float n) mult

```java title=Example.java
assert !Float.isInfinite(n) : "Trying to multiply " + Arrays.toString(nums) + " by  " + n;
for (int i = 0; i < nums.length; i++)
    nums[i] *= n;
return nums;
```

float[]mult(float[] nums, float n) mult

```java title=Example.java
assert !Float.isInfinite(n) : "Trying to multiply " + Arrays.toString(nums) + " by  " + n;
for (int i = 0; i < nums.length; i++)
    nums[i] *= n;
return nums;
```

byte[]multiply(byte[] a, byte b) a * b

```java title=Example.java
if (a == null)
    thrownewIllegalArgumentException("a should not be null");
int len = a.length;
byte[] result = newbyte[len];
int carry = 0;
int i2 = byte2int(b);
for (int i = len - 1; 0 <= i; i--) {
    int i1 = byte2int(a[i]);
...
```

double[]multiply(double factor, double[] vector) multiply

```java title=Example.java
double[] result = newdouble[vector.length];
for (int i = 0; i < vector.length; i++) {
    result[i] = vector[i] * factor;
return result;
```

double[]multiply(double[] a, double m) Multiply each element in the given array by the given factor.

```java title=Example.java
for (int i = 0; i < a.length; i++) {
    a[i] *= m;
return a;
```

voidmultiply(double[] a, double v) Multiplies a constant to all elements in the array.

```java title=Example.java
for (int i = 0; i < a.length; i++) {
    a[i] *= v;
```

double[]multiply(double[] a, double[] b) multiply

```java title=Example.java
if (a.length != b.length) {
    thrownewIllegalArgumentException("Arrays must be equal length");
double[] c = newdouble[a.length];
for (int i = 0; i < a.length; i++) {
    c[i] = a[i] * b[i];
return c;
...
```

double[]multiply(double[] a, double[] b) multiply

```java title=Example.java
finaldouble[] res = Arrays.copyOf(a, a.length);
for (int i = 0; i < res.length; ++i) {
    res[i] *= b[i];
return res;
```

double[]multiply(double[] a, double[] b) multiply

```java title=Example.java
double[] out = newdouble[a.length];
for (int i = 0; i < a.length; i++) {
    out[i] = a[i] * b[i];
return out;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
