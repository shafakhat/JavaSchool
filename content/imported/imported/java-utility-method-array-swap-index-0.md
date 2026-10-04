---
title: Java Utililty Methods Array Swap
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Swap are organized into topic(s).
section: Imported - java2s Archive
order: 50115
source: https://www.java2s.com/example/java-utility-method/array-swap-index-0.html
---
List of utility methods to do Array Swap

## Description

The list of methods to do Array Swap are organized into topic(s).

## Method

voidswap(boolean[] array, int i1, int i2) Swaps two elements of a vector

```java title=Example.java
boolean temp = array[i1];
array[i1] = array[i2];
array[i2] = temp;
```

voidswap(byte size, byte[] target, short targetOffset, byte[] a, short aOffset) swap

```java title=Example.java
for (byte i = 0; i < size; i++) {
    target[(short) (targetOffset + size - 1 - i)] = a[(short) (aOffset + i)];
```

byte[]swap(byte[] b1) swap

```java title=Example.java
for (int i = 0; i < (b1.length - 4); i = i + 4) {
    byte temp = b1[i];
    b1[i] = b1[i + 1];
    b1[i + 1] = b1[i + 2];
    b1[i + 2] = b1[i + 3];
    b1[i + 3] = temp;
return b1;
...
```

byte[]swap(byte[] buffer, int i, int j) swap

```java title=Example.java
finalbyte[] result = buffer.clone();
finalbyte c = result[i];
result[i] = result[j];
result[j] = c;
return result;
```

voidswap(byte[] bytes) swap

```java title=Example.java
int half = bytes.length / 2;
for (int i = 0; i < half; i++) {
    byte temp = bytes[i];
    bytes[i] = bytes[half + i];
    bytes[half + i] = temp;
```

byte[]swap(byte[] data) swap

```java title=Example.java
int count = data.length;
byte[] result = newbyte[count];
for (int i = 0; i < count; i++) {
    result[i] = data[count - 1 - i];
return result;
```

voidswap(byte[] data, int p, int q) swap

```java title=Example.java
int len = data.length * 8;
for (int i = 0; i < len; i += p) {
    int j = i + q;
    if (j < len) {
        byte b1 = data[i / 8];
        byte b2 = data[j / 8];
        int f1 = b1 & (1 << (i % 8));
        int f2 = b2 & (1 << (j % 8));
...
```

byte[]swap(byte[] rv, int offsetA, int offsetB) swap

```java title=Example.java
byte tmp = rv[offsetA];
rv[offsetA] = rv[offsetB];
rv[offsetB] = tmp;
return rv;
```

voidswap(Comparable[] a, int oldIndex, int newIndex) swap

```java title=Example.java
Comparable t = a[oldIndex];
a[oldIndex] = a[newIndex];
a[newIndex] = t;
```

voidswap(double x[], Object[] corr, int a, int b) swap

```java title=Example.java
finaldouble tmpX = x[a];
x[a] = x[b];
x[b] = tmpX;
finalObject tmpCorr = corr[a];
corr[a] = corr[b];
corr[b] = tmpCorr;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
