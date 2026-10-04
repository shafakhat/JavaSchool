---
title: Java Utililty Methods Array Invert
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Invert are organized into topic(s).
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/https://www.java2s.com/example/java-utility-method/array-invert-index-0.html
---
List of utility methods to do Array Invert

## Description

The list of methods to do Array Invert are organized into topic(s).

## Method

boolean[]invert(boolean[] binary) Invert binary array (apply a negation to each value).

```java title=Example.java
final boolean[] inverted = new boolean[binary.length];
for (int i = 0; i < inverted.length; i++) {
    inverted[i] = !binary[i];
return inverted;
```

boolean[]invert(boolean[] result) invert

```java title=Example.java
for (int i = 0; i < result.length; i++)
    result[i] = !result[i];
return result;
```

byte[]invert(byte abyte0[]) invert

```java title=Example.java
if (abyte0 == null || abyte0.length == 0)
    return abyte0;
byte abyte1[] = new byte[abyte0.length];
for (int i = 0; i < abyte0.length; i++)
    abyte1[i] = abyte0[abyte0.length - i - 1];
return abyte1;
```

byte[]invert(byte[] array) invert

```java title=Example.java
byte[] newArray = new byte[array.length];
for (int i = 0; i < array.length; ++i)
    newArray[newArray.length - i - 1] = array[i];
return newArray;
```

byte[]invert(byte[] bytes) Invert the provided byte array.

```java title=Example.java
byte[] invertedBytes = new byte[bytes.length];
for (int i = 0; i < bytes.length; i++) {
    invertedBytes[i] = (byte) (~bytes[i]);
return invertedBytes;
```

byte[]invert(byte[] key) invert

```java title=Example.java
byte[] inverted = Arrays.copyOf(key, key.length);
for (int i = 0; i < inverted.length; i++) {
    inverted[i] = (byte) (inverted[i] & 0xFF);
return inverted;
```

byte[]invert(byte[] v) Flips all the bits in the byte array

```java title=Example.java
return invert(v, 0, v.length);
```

double[]invert(double[] ary) invert

```java title=Example.java
if (ary == null)
    return null;
for (int i = 0; i < ary.length; i++)
    ary[i] = 1. / ary[i];
return ary;
```

float[]invert(float[] a) invert

```java title=Example.java
if (a == null) {
    throw new IllegalArgumentException("Argument cannot be null");
float[] c = new float[a.length];
for (int i = 0; i < a.length; i++) {
    c[i] = 1.0f / a[i];
return c;
...
```

booleaninvert(float[] m, float[] invOut) invert

```java title=Example.java
float[] inv = new float[16];
float det;
int i;
inv[0] = m[5] * m[10] * m[15] - m[5] * m[11] * m[14] - m[9] * m[6] * m[15] + m[9] * m[7] * m[14]
        + m[13] * m[6] * m[11] - m[13] * m[7] * m[10];
inv[4] = -m[4] * m[10] * m[15] + m[4] * m[11] * m[14] + m[8] * m[6] * m[15] - m[8] * m[7] * m[14]
        - m[12] * m[6] * m[11] + m[12] * m[7] * m[10];
inv[8] = m[4] * m[9] * m[15] - m[4] * m[11] * m[13] - m[8] * m[5] * m[15] + m[8] * m[7] * m[13]
...
```
