---
title: Java Utililty Methods Array Merge
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Merge are organized into topic(s).
section: Imported - java2s Archive
order: 50082
source: https://www.java2s.com/example/java-utility-method/array-merge-index-0.html
---
List of utility methods to do Array Merge

## Description

The list of methods to do Array Merge are organized into topic(s).

## Method

voidarrayMerge16bit(byte[] sourceArray, int sourceStart, byte[] destinationArray, int destinationStart, int length) Merges two byte arrays -- source and destination -- together by summing field-wise where a field is a 16bit word, which is two of these array bytes.

```java title=Example.java
if (sourceArray.length - sourceStart < length || destinationArray.length - destinationStart < length) {
    thrownewIllegalStateException("Length too large for input arrays.");
for (int i = 0; i < length; i = i + 2) {
    int srcValue = (sourceArray[sourceStart + i] & 0xFF) | (sourceArray[sourceStart + i + 1] << 8);
    int dstValue = (destinationArray[destinationStart + i] & 0xFF)
            | (destinationArray[destinationStart + i + 1] << 8);
    int sum = srcValue + dstValue;
...
```

double[]concat(double[] merged, double[] is) Concatenates two double arrays.

```java title=Example.java
double result[] = newdouble[merged.length + is.length];
result = Arrays.copyOf(merged, merged.length + is.length);
System.arraycopy(is, 0, result, merged.length, is.length);
return result;
```

intmerge(final Item[] values, final Item[] auxiliary, final int first, final int middle, final int last) merge

```java title=Example.java
int numberOfInversions = 0;
int i = first;
int j = middle + 1;
int k = first;
for (; i <= middle && j <= last; k++)
    if (!isLess(values[j], values[i])) {
        auxiliary[k] = values[i];
        i++;
...
```

byte[]merge(byte[] a, byte[] b) merge

```java title=Example.java
int total = a.length + b.length;
byte[] c = newbyte[total];
for (int i = 0; i < a.length; i++) {
    c[i] = a[i];
for (int i = 0; i < b.length; i++) {
    c[a.length + i] = b[i];
return c;
```

byte[]merge(byte[] array1, byte[] array2) merge

```java title=Example.java
byte[] result = newbyte[array1.length + array2.length];
int saltOffset = array1.length;
for (int i = 0; i < result.length; i++) {
    if (i < saltOffset) {
        result[i] = array1[i];
    } else {
        result[i] = array2[i - saltOffset];
return result;
```

byte[]merge(byte[] signature, byte[] message) merge

```java title=Example.java
byte[] result = newbyte[signature.length + message.length];
System.arraycopy(signature, 0, result, 0, signature.length);
System.arraycopy(message, 0, result, signature.length, message.length);
return result;
```

byte[]merge(byte[] src, byte[] src2, int start, int length) merge

```java title=Example.java
byte[] dest = newbyte[src.length + length];
System.arraycopy(src, 0, dest, 0, src.length);
System.arraycopy(src2, start, dest, src.length, length);
return dest;
```

byte[]merge(byte[] src1, byte[] src2) merge

```java title=Example.java
if (null == src1 || src1.length == 0)
    return src2;
if (null == src2 || src2.length == 0)
    return src1;
int alen = src1.length;
int blen = src2.length;
byte[] dest = Arrays.copyOf(src1, alen + blen);
System.arraycopy(src2, 0, dest, alen, blen);
...
```

byte[]merge(byte[]... arrays) merge

```java title=Example.java
int arrCount = 0;
int count = 0;
for (byte[] array : arrays) {
    arrCount++;
    count += array.length;
byte[] mergedArray = newbyte[count];
int start = 0;
...
```

byte[]merge(byte[]... bytes) merge

```java title=Example.java
byte[] result = null;
int length = 0;
for (byte[] t : bytes) {
    length += t.length;
result = newbyte[length];
int index = 0;
for (byte[] t : bytes) {
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
