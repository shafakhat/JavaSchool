---
title: Java Utililty Methods Array Length Get
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Length Get are organized into topic(s).
section: Imported - java2s Archive
order: 50079
source: https://www.java2s.com/example/java-utility-method/array-length-get-index-0.html
---
List of utility methods to do Array Length Get

## Description

The list of methods to do Array Length Get are organized into topic(s).

## Method

voidarrayBounds(int arrayLength, int offset, int length) array Bounds

```java title=Example.java
if (offset < 0 || length < 0 || length > arrayLength - offset) {
    thrownewIndexOutOfBoundsException(
            "array.length=" + arrayLength + ", offset=" + offset + ", length=" + length);
```

intarrayCounter(T[] x) array Counter

```java title=Example.java
int z = 0;
for (int i = 0; i < x.length; i++) {
    T y = x[i];
    if (y != null) {
        z++;
return z;
...
```

intarrayLenght(Object array) array Lenght

```java title=Example.java
if (array instanceofObject[]) {
    return ((Object[]) array).length;
} elseif (array instanceofint[]) {
    return ((int[]) array).length;
} elseif (array instanceoflong[]) {
    return ((long[]) array).length;
} elseif (array instanceofdouble[]) {
    return ((double[]) array).length;
...
```

intarrayLength(Object array, int defaultIfNull, int defaultIfNotArray) array Length

```java title=Example.java
if (array == null) {
    return defaultIfNull;
} elseif (array instanceofObject[]) {
    return ((Object[]) array).length;
} elseif (array instanceoflong[]) {
    return ((long[]) array).length;
} elseif (array instanceofint[]) {
    return ((int[]) array).length;
...
```

intarrayLength(Object o) array Length

```java title=Example.java
if (o instanceofObject[])
    return ((Object[]) o).length;
elseif (o instanceofboolean[])
    return ((boolean[]) o).length;
elseif (o instanceoffloat[])
    return ((float[]) o).length;
elseif (o instanceofdouble[])
    return ((double[]) o).length;
...
```

intarrayLength(Object[] ar) array Length

```java title=Example.java
return ar.length;
```

intlength(byte[] array) length

```java title=Example.java
return (array == null ? 0 : array.length);
```

Stringlength(byte[] array) length

```java title=Example.java
return"(" + array.length + " B)";
```

doublelength(double[] a) length

```java title=Example.java
double c = 0;
for (int i = 0; i < a.length; i++)
    c += a[i] * a[i];
returnMath.sqrt(c);
```

doublelength(double[] point) length

```java title=Example.java
returnMath.sqrt(stScalarProd(point, point));
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
