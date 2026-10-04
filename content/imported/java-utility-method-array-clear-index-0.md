---
title: Java Utililty Methods Array Clear
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Clear are organized into topic(s).
section: Imported - java2s Archive
order: 50036
source: https://www.java2s.com/example/java-utility-method/array-clear-index-0.html
---
List of utility methods to do Array Clear

## Description

The list of methods to do Array Clear are organized into topic(s).

## Method

voidzero(float[][] M) zero

```java title=Example.java
for (int i = 0; i < M.length; i++) {
    Arrays.fill(M[i], 0);
```

voidZeroByteArray(byte[] pbArray) Zero Byte Array

```java title=Example.java
assert pbArray != null;
if (pbArray == null)
    thrownewIllegalArgumentException("pbArray");
Arrays.fill(pbArray, (byte) 0);
```

long[]zeroI(long[] v) Zero the given set Low-endian layout for the array.

```java title=Example.java
Arrays.fill(v, 0);
return v;
```

voidzeros(final float[] input) zeros

```java title=Example.java
Arrays.fill(input, 0, input.length, 0.0f);
```
