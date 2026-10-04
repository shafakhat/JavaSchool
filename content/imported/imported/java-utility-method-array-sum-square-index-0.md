---
title: Java Utililty Methods Array Sum Square
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Sum Square are organized into topic(s).
section: Imported - java2s Archive
order: 50114
source: https://www.java2s.com/example/java-utility-method/array-sum-square-index-0.html
---
List of utility methods to do Array Sum Square

## Description

The list of methods to do Array Sum Square are organized into topic(s).

## Method

doublesumOfSquares(double[] vector) This returns the sum of squares for the given vector.

```java title=Example.java
double ret = 0;
for (double d : vector)
    ret += Math.pow(d, 2);
return ret;
```

doublesumOfSquares(double[] vector) sum Of Squares

```java title=Example.java
double sum = 0;
for (double d : vector)
    sum += sq(d);
return sum;
```

intsumOfSquares(int numberOfTerms) sum Of Squares

```java title=Example.java
return (int) (((double) numberOfTerms / 6) * (numberOfTerms + 1) * (2 * numberOfTerms + 1));
```

doublesumOfSquares(Number[] array) Returns sum of all the squared elements in the array.

```java title=Example.java
double result;
int i;
result = 0.0;
for (i = 0; i < array.length; i++)
    result += array[i].doubleValue() * array[i].doubleValue();
return result;
```

doublesumSq(double... values) sum Sq

```java title=Example.java
double sum = 0;
for (double v : values) {
    sum += v * v;
return sum;
```

doublesumSq(double[] a) Returns the sum of squares.

```java title=Example.java
return sumSq(a, 0, a.length);
```

intsumSqual(byte[] b) sum Squal

```java title=Example.java
int sum = 0;
for (int i = 0; i < b.length; i++) {
    sum += (int) Math.pow(b[i], 2);
return sum;
```

doublesumSquared(double[] data) sum Squared

```java title=Example.java
return sumSquared(data, 0.0);
```

doublesumSquared(double[] data, double term) sum Squared

```java title=Example.java
double sum = 0.0;
for (int i = 0; i < data.length; i++) {
    if (Double.isNaN(data[i]))
        continue;
    sum += (data[i] + term) * (data[i] + term);
return sum;
```

intSumSquared(Object in) Sum Squared

```java title=Example.java
if (in == null)
    return 0;
if (in instanceofint[]) {
    int[] inn = (int[]) in;
    int out = 0;
    for (int i = 0, s = inn.length; i < s; i++)
        out += inn[i] * inn[i];
    return out;
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
