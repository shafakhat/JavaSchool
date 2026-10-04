---
title: Java Utililty Methods Array Combine
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Combine are organized into topic(s).
section: Imported - java2s Archive
order: 50038
source: https://www.java2s.com/example/java-utility-method/array-combine-index-0.html
---
List of utility methods to do Array Combine

## Description

The list of methods to do Array Combine are organized into topic(s).

## Method

Object[]combine(int size, Object[]... arrays) combine

```java title=Example.java
int offset = 0;
Object[] target = newObject[size];
for (Object[] arr : arrays) {
    System.arraycopy(arr, 0, target, offset, arr.length);
    offset += arr.length;
return target;
```

int[]combine(int[][] arr, int[] terms) Combine elements in a given two level array and an optional second array of terms, combine them all in a single array of terms

```java title=Example.java
int c = 0;
if (arr != null)
    for (int i = 0; i < arr.length; i++)
        c += arr[i].length;
if (terms != null)
    c += terms.length;
int[] r = newint[c];
c = 0;
...
```

voidcombine(Object[] array1, Object[] array2, Object[] combinedArray) combine

```java title=Example.java
System.arraycopy(array1, 0, combinedArray, 0, array1.length);
System.arraycopy(array2, 0, combinedArray, array1.length, array2.length);
```

Object[]combine(Object[] first, Object[] last) combine

```java title=Example.java
if (first.length == 0 && last.length == 0) {
    return null;
Object[] result = newObject[first.length + last.length];
System.arraycopy(first, 0, result, 0, first.length);
System.arraycopy(last, 0, result, first.length, last.length);
return result;
```

Stringcombine(Object[] objects, String glue) combine

```java title=Example.java
int l = objects.length;
int m = l - 1;
int x;
if (l == 0) {
    return null;
StringBuilder r = newStringBuilder();
for (x = 0; x < m; x++) {
...
```

floatcombineAlpha(float[] partsAlpha, int partsN) Combine multiple alpha values.

```java title=Example.java
float sumAlpha = 0.f;
int count = 0;
for (int i = 0; i < partsN; i++) {
    if (!Float.isNaN(partsAlpha[i])) {
        sumAlpha += partsAlpha[i];
        count++;
if (count > 0) {
    return sumAlpha / count;
} else {
    return 0.f;
```

voidcombineArrays(final Object[] array1, final Object[] array2, final Object[] targetArray) Combines two array into a target array, inserting all elements of the first array and then all elements of the second array in the target array.

```java title=Example.java
finalint lengthOfFirst = array1.length;
int i;
for (i = 0; i < lengthOfFirst; i++) {
    targetArray[i] = array1[i];
for (i = 0; i < array2.length; i++) {
    targetArray[i + lengthOfFirst] = array2[i];
```

float[]combineArrays(float[]... arrays) combine Arrays

```java title=Example.java
int size = arrays[0].length;
float[] result = newfloat[arrays.length * arrays[0].length];
for (int i = 0; i < arrays.length; i++) {
    for (int j = 0; j < size; j++) {
        result[i * size + j] = arrays[i][j];
return result;
...
```

byte[]combineByteArray(byte[] one, byte[] two) combine Byte Array

```java title=Example.java
byte[] out = newbyte[one.length + two.length];
System.arraycopy(one, 0, out, 0, one.length);
System.arraycopy(two, 0, out, one.length, two.length);
return out;
```

voidcombineChannels(int[][] a, int[][] r, int[][] g, int[][] b, int[][] pixels) combine Channels

```java title=Example.java
int w = pixels.length;
int h = pixels[0].length;
for (int x = 0; x < w; ++x) {
    for (int y = 0; y < h; ++y) {
        pixels[x][y] = (a[x][y] << 24) | (r[x][y] << 16) | (g[x][y] << 8) | b[x][y];
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
