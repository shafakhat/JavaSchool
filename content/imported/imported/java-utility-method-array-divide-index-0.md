---
title: Java Utililty Methods Array Divide
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Divide are organized into topic(s).
section: Imported - java2s Archive
order: 50057
source: https://www.java2s.com/example/java-utility-method/array-divide-index-0.html
---
List of utility methods to do Array Divide

## Description

The list of methods to do Array Divide are organized into topic(s).

## Method

double[]arrayDivide(double[] a, double[] b) Divides two vectors of doubles, array-wise.

```java title=Example.java
double[] out = newdouble[a.length];
for (int i = 0; i < a.length; i++) {
    out[i] = a[i] / b[i];
return out;
```

double[]arrayDivide(double[] d1, double denominator) Divides each element of an array by a number.

```java title=Example.java
if (d1 == null) {
    thrownewIllegalArgumentException("Array cannot be null.");
double[] dDivide = newdouble[d1.length];
for (int i = 0; i < d1.length; i++) {
    dDivide[i] = d1[i] / denominator;
return dDivide;
...
```

double[]arrayDivision(double[] array, double number) A quick method for simple array division in Java.

```java title=Example.java
double[] newArray = newdouble[array.length];
for (int i = 0; i < array.length; i++) {
    newArray[i] = array[i] / number;
return newArray;
```

double[]div(double a, double[] b) div

```java title=Example.java
if (a == 0)
    thrownewIllegalArgumentException("Divison by zero");
double[] erg = newdouble[b.length];
for (int i = 0; i < b.length; i++) {
    erg[i] = b[i] / a;
return erg;
```

int[]div(final int[] result, final int[] vector, final int[] scale) Divides a vector by param using given result int[], result = vector / scale

```java title=Example.java
for (int i = 0; i < result.length; i++) {
    result[i] = vector[i] / scale[i];
return result;
```

float[]div(float[] items, int offset, int length, float divisor) div

```java title=Example.java
return mul(items, offset, length, 1 / divisor);
```

float[]div(float[] items, int offset, int length, float divisorX, float divisorY) div

```java title=Example.java
for (int i = offset; i < offset + length; i += 2) {
    items[i] /= divisorX;
    items[i + 1] /= divisorY;
return items;
```

float[]div(float[] nums, float n) div

```java title=Example.java
assert !Float.isInfinite(n) : "Trying to divide " + Arrays.toString(nums) + " by  " + n;
for (int i = 0; i < nums.length; i++)
    nums[i] /= n;
return nums;
```

float[]div(float[] nums, int n) div

```java title=Example.java
for (int i = 0; i < nums.length; i++)
    nums[i] /= n;
return nums;
```

float[]div(float[] nums, int n) div

```java title=Example.java
for (int i = 0; i < nums.length; i++)
    nums[i] /= n;
return nums;
```
