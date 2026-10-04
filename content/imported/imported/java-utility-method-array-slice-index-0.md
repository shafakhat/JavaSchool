---
title: Java Utililty Methods Array Slice
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Slice are organized into topic(s).
section: Imported - java2s Archive
order: 50106
source: https://www.java2s.com/example/java-utility-method/array-slice-index-0.html
---
List of utility methods to do Array Slice

## Description

The list of methods to do Array Slice are organized into topic(s).

## Method

int[]arraySlice(int[] source, int start, int count) Returns a range of elements of source from start to end of the array.

```java title=Example.java
int[] slice = newint[count];
System.arraycopy(source, start, slice, 0, count);
return slice;
```

Object[]arraySlice(Object[] source, Object[] dest, int startIdx) array Slice

```java title=Example.java
for (int i = startIdx; i < dest.length; i++) {
    dest[i] = source[i];
return dest;
```

byte[]slice(byte[] buffer, int start, int end) slice

```java title=Example.java
returnArrays.copyOfRange(buffer, start, end);
```

byte[]slice(byte[] source, int start, int end) slice

```java title=Example.java
if (start < 0 || end > source.length) {
    thrownewIllegalArgumentException("start or end is out of bound");
byte[] target = newbyte[end - start];
System.arraycopy(source, start, target, 0, target.length);
return target;
```

Object[]slice(Object[] objects, int begin, int length) slice

```java title=Example.java
Object[] result = newObject[length];
for (int i = 0; i < length; i++) {
    result[i] = objects[begin + i];
return result;
```

String[]slice(String source[], int start, int end) slice

```java title=Example.java
if (source == null)
    return null;
if (start == end)
    returnnewString[0];
int e = Math.max(start, end);
e = Math.min(e, source.length);
int s = Math.min(start, end);
String newArray[] = newString[e - s];
...
```

String[]slice(String[] array, int a, int b) slice

```java title=Example.java
String[] newarray = newString[b - a];
if (!(a < array.length && b <= array.length)) {
    thrownewException("out of bound:" + a + "," + b);
for (int i = a; i < b; i++) {
    newarray[i - a] = array[i];
return newarray;
...
```

String[]slice(String[] array, int index, int length) slice

```java title=Example.java
String[] slice = newString[length];
for (int i = 0; i < length; i++) {
    slice[i] = array[index + i];
return slice;
```

String[]slice(String[] o, int index) Slices an array at the given index.

```java title=Example.java
String[] result = newString[o.length - index];
for (int i = index; i < o.length; i++) {
    result[i - index] = o[i];
return result;
```

String[]slice(String[] strings, int begin, int length) slice

```java title=Example.java
String[] result = newString[length];
System.arraycopy(strings, begin, result, 0, length);
return result;
```
