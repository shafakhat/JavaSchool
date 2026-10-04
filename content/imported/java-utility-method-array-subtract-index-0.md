---
title: Java Utililty Methods Array Subtract
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Subtract are organized into topic(s).
section: Imported - java2s Archive
order: 50112
source: https://www.java2s.com/example/java-utility-method/array-subtract-index-0.html
---
List of utility methods to do Array Subtract

## Description

The list of methods to do Array Subtract are organized into topic(s).

## Method

double[]arraySubtract(double[] x1, double[] x2) array Subtract

```java title=Example.java
double[] result = newdouble[x1.length];
for (int i = 0; i < x1.length; i++) {
    result[i] = x1[i] - x2[i];
return result;
```

Double[]arraySubtract(final Double[] first, final Double[] second) Subtracts the elements of the arrays.

```java title=Example.java
finalDouble[] toret = newDouble[first.length];
for (int i = 0; i < first.length; i++) {
    toret[i] = first[i] - second[i];
return toret;
```

byte[]subtract(byte[] a, byte[] b) a - b

```java title=Example.java
if (a == null)
    thrownewIllegalArgumentException("b1 should not be null");
if (b == null)
    thrownewIllegalArgumentException("b2 should not be null");
if (a.length != b.length)
    thrownewIllegalArgumentException("byte array length should be same");
int len = a.length;
byte[] result = newbyte[len];
...
```

double[]subtract(double[] a, double[] b) subtract

```java title=Example.java
if (a.length != b.length) {
    thrownewIllegalArgumentException("Arrays must be equal length");
double[] c = newdouble[a.length];
for (int i = 0; i < a.length; i++) {
    c[i] = a[i] - b[i];
return c;
...
```

double[]subtract(double[] a, double[] b) Subtracts two points

```java title=Example.java
if (a.length != b.length)
    thrownewIllegalArgumentException("Subtracted two not matching Vectors.");
double[] erg = newdouble[a.length];
for (int i = 0; i < a.length; i++) {
    erg[i] = a[i] - b[i];
return erg;
```

double[]subtract(double[] a, double[] b) Subtracts the two arrays together (componentwise)

```java title=Example.java
if (a.length != b.length) {
    thrownewIllegalArgumentException(
            "To add two arrays, they must have the same length : " + a.length + ", " + b.length);
double[] ans = copy(a);
for (int i = 0; i < a.length; i++) {
    ans[i] -= b[i];
return (ans);
```

double[]subtract(double[] a, double[] b) Returns the array-wise difference between two vectors.

```java title=Example.java
double[] out = newdouble[a.length];
for (int i = 0; i < a.length; i++) {
    out[i] = a[i] - b[i];
return out;
```

double[]subtract(double[] accumulator, double[] values) Subtracts the elements of one array of

```java title=Example.java
double
```

s from another.

```java title=Example.java
if (accumulator == null) {
    accumulator = newdouble[values.length];
assert (accumulator.length == values.length);
for (int i = 0; i < accumulator.length; i++) {
    accumulator[i] -= values[i];
return accumulator;
...
```

voidsubtract(double[] array, double a) subtract

```java title=Example.java
for (int i = 0; i < array.length; ++i) {
    array[i] -= a;
```

double[]subtract(double[] array, double value) Subtracts a constant value from all items in an array

```java title=Example.java
double[] returnValues = newdouble[array.length];
for (int i = 0; i < returnValues.length; i++) {
    returnValues[i] = array[i] - value;
return returnValues;
```
