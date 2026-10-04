---
title: Java Utililty Methods Array Fill
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Fill are organized into topic(s).
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/https://www.java2s.com/example/java-utility-method/array-fill-index-0.html
---
List of utility methods to do Array Fill

## Description

The list of methods to do Array Fill are organized into topic(s).

## Method

T[]fill( T[] a, T val) Assigns the specified T reference

```java title=Example.java
val
```

to each element of the array

```java title=Example.java
a
```

.

```java title=Example.java
Arrays.fill(a, val);
return a;
```

Listfill(byte[] arr) fill

```java title=Example.java
List<Byte> list = null;
if (arr == null) {
    return new ArrayList<Byte>(0);
int size = arr.length;
list = new ArrayList<Byte>(size);
for (byte by : arr) {
    list.add(by);
...
```

byte[]fill(byte[] val, byte b) fill

```java title=Example.java
if (val == null)
    throw new IllegalArgumentException("val should not be null");
Arrays.fill(val, b);
return val;
```

char[]fill(char[] chars, int fromIndex, int toIndex, char c) fill

```java title=Example.java
int length = toIndex - fromIndex;
if (length < 20) {
    for (int i = fromIndex; i < toIndex; i++)
        chars[i] = c;
} else if (c != ' ' || length > WHITESPACE_BUFFER.length) {
    Arrays.fill(chars, fromIndex, toIndex, c);
} else {
    System.arraycopy(WHITESPACE_BUFFER, 0, chars, fromIndex, length);
...
```

voidfill(double[][] array, double s) fill

```java title=Example.java
for (int i = 0; i < array.length; i++) {
    Arrays.fill(array[i], s);
```

voidfill(double[][] d, double val) fill

```java title=Example.java
for (double[] aD : d) {
    Arrays.fill(aD, val);
```

double[][]fill(final double[][] arr, final double val) Fills the given two-dimensional double array with the value val .

```java title=Example.java
for (final double[] line : arr) {
    Arrays.fill(line, val);
return arr;
```

voidfill(final Object[] array, final int start, final int end, final Object value) Fill the specified segment of an array with the provided value.

```java title=Example.java
assert start >= 0 && start <= end;
assert end <= array.length;
assert array.length == 0 || array.length == pow2(array.length);
final int n = LINE_SIZE;
int i = Math.min(n, end);
Arrays.fill(array, start, i, value);
while (i < end) {
    System.arraycopy(array, i - n, array, i, n);
...
```

T[]fill(final T[] array, final int size) fill

```java title=Example.java
if (array.length >= size) {
    return array;
final T[] result = Arrays.copyOf(array, size);
return result;
```

T[]fill(final T[] array, final T value) Fill the given array with the given value

```java title=Example.java
Arrays.fill(array, value);
return array;
```
