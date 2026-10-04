---
title: Java Utililty Methods Array Boolean Operation
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Boolean Operation are organized into topic(s).
section: Imported - java2s Archive
order: 50032
source: https://www.java2s.com/example/java-utility-method/array-boolean-operation-index-0.html
---
List of utility methods to do Array Boolean Operation

## Description

The list of methods to do Array Boolean Operation are organized into topic(s).

## Method

voidfillArrayAND(final short[] container, final long[] bitmap1, final long[] bitmap2) Compute the bitwise AND between two long arrays and write the set bits in the container.

```java title=Example.java
int pos = 0;
if (bitmap1.length != bitmap2.length) {
    thrownewIllegalArgumentException("not supported");
for (int k = 0; k < bitmap1.length; ++k) {
    long bitset = bitmap1[k] & bitmap2[k];
    while (bitset != 0) {
        long t = bitset & -bitset;
...
```
