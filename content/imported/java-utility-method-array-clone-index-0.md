---
title: Java Utililty Methods Array Clone
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Clone are organized into topic(s).
section: Imported - java2s Archive
order: 50037
source: https://www.java2s.com/example/java-utility-method/array-clone-index-0.html
---
List of utility methods to do Array Clone

## Description

The list of methods to do Array Clone are organized into topic(s).

## Method

boolean[]clone(boolean[] array)

Clones an array returning a typecast result and handling null. if (array == null) { return null; return copyOf(array, array.length);

boolean[]clone(boolean[] array) clone

```java title=Example.java
boolean[] newArray = newboolean[array.length];
System.arraycopy(array, 0, newArray, 0, array.length);
return newArray;
```

boolean[]clone(boolean[] in) clone

```java title=Example.java
boolean[] ret = newboolean[in.length];
System.arraycopy(in, 0, ret, 0, in.length);
return ret;
```

byte[]clone(byte[] input) Clone a byte array.

```java title=Example.java
if (input == null) {
    return null;
byte[] ret = newbyte[input.length];
System.arraycopy(input, 0, ret, 0, input.length);
return ret;
```

byte[]clone(byte[] orig) Clone a byte array, maintaining awareness of null arrays

```java title=Example.java
if (orig == null)
    return null;
return (byte[]) orig.clone();
```

byte[][]clone(byte[][] im) clone

```java title=Example.java
byte[][] clone = newbyte[im.length][im[0].length];
copy(clone, im);
return clone;
```

double[]clone(double[] array) Return a new copy of a double aray holding the same elements

```java title=Example.java
if (array == null) {
    return null;
double[] clone = newdouble[array.length];
for (int i = 0; i < array.length; i++) {
    clone[0] = array[i];
return clone;
...
```

double[]clone(double[] p) clone

```java title=Example.java
double[] ret = newdouble[p.length];
System.arraycopy(p, 0, ret, 0, p.length);
return ret;
```

double[][]clone(double[][] source) Returns a clone of the specified array.

```java title=Example.java
if (source == null) {
    thrownewIllegalArgumentException("Null 'source' argument.");
double[][] clone = newdouble[source.length][];
for (int i = 0; i < source.length; i++) {
    if (source[i] != null) {
        double[] row = newdouble[source[i].length];
        System.arraycopy(source[i], 0, row, 0, source[i].length);
...
```

byte[]clone(final byte[] array) Clones an array of bytes.

```java title=Example.java
return clone(array, 0, array.length);
```
