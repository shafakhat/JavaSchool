---
title: Java Utililty Methods Array Normalize
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Normalize are organized into topic(s).
section: Imported - java2s Archive
order: 50087
source: https://www.java2s.com/example/java-utility-method/array-normalize-index-0.html
---
List of utility methods to do Array Normalize

## Description

The list of methods to do Array Normalize are organized into topic(s).

## Method

shortnorm(byte[] tab) Computes the number of 1's in the byte array

```java title=Example.java
short count = 0;
for (byte b : tab) {
    count += bitCount(b);
return count;
```

doublenorm(double[] a) Description of the Method

```java title=Example.java
return (double) Math.sqrt(innerproduct(a, a));
```

doublenorm(double[] a) vector 2-norm

```java title=Example.java
double c = 0.0;
for (double num : a) {
    c += num * num;
returnMath.sqrt(c);
```

doublenorm(double[] a) Calculates the euclidean norm of a vector.

```java title=Example.java
double result = 0;
for (int i = 0; i < a.length; i++)
    result += Math.pow(a[i], 2);
result = Math.sqrt(result);
return result;
```

doublenorm(double[] array) Returns the norm of the vector

```java title=Example.java
if (array != null) {
    int n = array.length;
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += array[i] * array[i];
    returnMath.pow(sum, 0.5);
} else
...
```

doublenorm(double[] data) Computes the L2 norm of an array (Euclidean norm or "length").

```java title=Example.java
return (Math.sqrt(sumSquares(data)));
```

doublenorm(double[] v) returns the norm of the vector

```java title=Example.java
return (Math.sqrt(dotprod(v, v)));
```

doublenorm(double[] vector) norm

```java title=Example.java
double result = 0.0;
for (int i = 0; i < vector.length; i++) {
    result += vector[i] * vector[i];
return result;
```

doublenorm(double[] vector, int n) This method takes the Ln vector norm of the vector according to the formula: Norm = [E(i=0 to vector.length) |vector[i]|^n]^(1.0/n)

```java title=Example.java
double norm = 0.0;
for (int i = 0; i < vector.length; ++i) {
    double inner = 1.0;
    double comp = Math.abs(vector[i]);
    for (int dim = 0; dim < n; ++dim)
        inner *= comp;
    norm += inner;
if (n != 1)
    norm = Math.pow(norm, 1.0 / n);
return norm;
```

doublenorm(final double[] vec) Returns the euclidean norm of a vector.

```java title=Example.java
assert vec != null;
double s = 0;
for (double i : vec) {
    s += Math.pow(i, 2);
returnMath.sqrt(s);
```
