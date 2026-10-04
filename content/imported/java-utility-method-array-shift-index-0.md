---
title: Java Utililty Methods Array Shift
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Shift are organized into topic(s).
section: Imported - java2s Archive
order: 50102
source: https://www.java2s.com/example/java-utility-method/array-shift-index-0.html
---
List of utility methods to do Array Shift

## Description

The list of methods to do Array Shift are organized into topic(s).

## Method

Object[]arrayShift(Object[] input, int shift) Shift all objects in an array by the number of places specified.

```java title=Example.java
Object[] newArray = newObject[input.length];
for (int i = 0; i < input.length; i++) {
    int newPos = (i + shift) % input.length;
    if (newPos < 0) {
        newPos += input.length;
    newArray[newPos] = input[i];
return newArray;
```

voidarrayShiftArgs(int[] array, int a) array Shift Args

```java title=Example.java
for (int i = 0; i < array.length; i++) {
    if (array[i] > a)
        array[i]--;
```

doubleshift(double[] a, int shift, double insert) each entry is moved from index to index+shift

```java title=Example.java
if (shift > 0) {
    double re = sum(a, a.length - shift, a.length);
    for (int i = a.length - 1; i >= shift; i--)
        a[i] = a[i - shift];
    Arrays.fill(a, 0, shift, insert);
    return re;
} else {
    double re = sum(a, 0, -shift);
...
```

double[]shift(double[] x, int N) shift

```java title=Example.java
if (N == 0)
    return x;
double[] y = newdouble[x.length];
int i;
if (N > 0) {
    for (i = 0; i < N; i++)
        y[i] = x[0];
    for (i = N; i < x.length - N; i++)
...
```

byte[]shift(final byte[] input, final int amount) shift

```java title=Example.java
finalbyte[] r = newbyte[input.length + amount];
System.arraycopy(input, 0, r, amount, Math.min(input.length, r.length));
return r;
```

double[]shift(final double[] values, final double constant) Shifts all the elements of

```java title=Example.java
values
```

by

```java title=Example.java
constant
```

.

```java title=Example.java
finaldouble ret[] = newdouble[values.length];
for (int i = values.length; i-- != 0;)
    ret[i] = values[i] + constant;
return ret;
```

voidshift(final Object[] array, int offset) Shifts the order of the given array.

```java title=Example.java
if (array == null) {
    return;
shift(array, 0, array.length, offset);
```

voidShift(int[] in, int amt, int spare) Shift

```java title=Example.java
if (amt > 0) {
    System.arraycopy(in, 0, in, amt, in.length - amt);
    Arrays.fill(in, 0, amt, spare);
} elseif (amt < 0) {
    System.arraycopy(in, -amt, in, 0, in.length + amt);
    Arrays.fill(in, in.length + amt, in.length, spare);
```

voidshift(int[] v, int n) shift

```java title=Example.java
int[] copy = newint[v.length];
for (int i = 0; i < v.length; i++)
    copy[i] = v[(i + n + v.length) % v.length];
System.arraycopy(copy, 0, v, 0, v.length);
```

int[][]shift(int[][] array, boolean inverse) shift

```java title=Example.java
int[][] result = newint[4][4];
for (int i = 0; i < 4; i++)
    result[i] = shift(array[i], inverse ? i : -i);
return result;
```
