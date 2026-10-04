---
title: Java Utililty Methods Array
nav: Java Utililty Methods Array
description: int[]array_intAddLimit(int[] in, int value, int limit) arraint Add Limit
section: Imported - java2s Archive
order: 50027
source: https://www.java2s.com/example/java-utility-method/array-index-0.html
---
List of utility methods to do Array

## Description

The list of methods to do Array are organized into topic(s).

## Method

booleanarray_equals(byte[] foo, byte bar[]) arraequals

```java title=Example.java
int i = foo.length;
if (i != bar.length)
    return false;
for (int j = 0; j < i; j++) {
    if (foo[j] != bar[j])
        return false;
return true;
...
```

float[]array_int2float(int ai[]) arraintfloat

```java title=Example.java
float af[] = newfloat[ai.length];
for (int i = 0; i < af.length; i++)
    af[i] = (float) ai[i];
return af;
```

int[]array_intAddLimit(int[] in, int value, int limit) arraint Add Limit

```java title=Example.java
int[] ret = newint[Math.min(in.length + 1, limit)];
System.arraycopy(in, Math.max(0, in.length - limit), ret, 0, in.length);
ret[Math.min(in.length, limit - 1)] = value;
return ret;
```

Stringarrayed(int arrays, String inner) arrayed

```java title=Example.java
return repeat("jni::Array< ", arrays) + inner + repeat(" >", arrays);
```

booleanarrayEndsWith(final byte[] array, final byte[] str) Check that a byte array ends with some byte values.

```java title=Example.java
boolean result = false;
if (array.length >= str.length) {
    result = true;
    int index = str.length;
    int arrindex = array.length;
    while (--index >= 0) {
        if (array[--arrindex] != str[index]) {
            result = false;
...
```

double[]arrayExclude(double[] src, int excludeIndex) Excludes an element from a provided array and returns a copy without the element.

```java title=Example.java
double[] temp = newdouble[src.length - 1];
System.arraycopy(src, 0, temp, 0, excludeIndex);
System.arraycopy(src, excludeIndex + 1, temp, excludeIndex, src.length - excludeIndex - 1);
return temp;
```

intarrayFirstIndexOf(final T[] array, final T value) array First Index Of

```java title=Example.java
for (int i = 0; i < array.length; i++) {
    if (value == array[i])
        return i;
return -1;
```

int[]arrayFlatten(final int[][] arr) Flatten a 2D array into a 1D array.

```java title=Example.java
int size = 0;
for (int[] e : arr) {
    size += e.length;
int[] result = newint[size];
int i = 0;
for (int[] e : arr) {
    for (int v : e) {
...
```

byte[]arrayGetCenter(byte[] array, int location, int length) array Get Center

```java title=Example.java
if (length <= 0) {
    returnnewbyte[0];
byte[] result;
result = newbyte[length];
try {
    System.arraycopy(array, location, result, 0, length);
} catch (Exception e) {
...
```

booleanarrayIsHave(String[] strs, String str) array Is Have

```java title=Example.java
for (int i = 0; i < strs.length; i++) {
    if (strs[i].equalsIgnoreCase(str)) {
        return true;
return false;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
