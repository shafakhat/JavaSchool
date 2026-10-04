---
title: Java Utililty Methods Array Last Index Of
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Last Index Of are organized into topic(s).
section: Imported - java2s Archive
order: 50078
source: https://www.java2s.com/example/java-utility-method/array-last-index-of-index-0.html
---
List of utility methods to do Array Last Index Of

## Description

The list of methods to do Array Last Index Of are organized into topic(s).

## Method

intarrayLastIndexOf(final T[] array, final T value) array Last Index Of

```java title=Example.java
for (int i = array.length; i-- > 0;) {
    if (value == array[i])
        return i;
return -1;
```

intarrayLastIndexOf(Object[] array, Object objectToFind) array Last Index Of

```java title=Example.java
return arrayLastIndexOf(array, objectToFind, Integer.MAX_VALUE);
```

intlastIndexOf(boolean[] array, boolean valueToFind) last Index Of

```java title=Example.java
return lastIndexOf(array, valueToFind, 2147483647);
```

intlastIndexOf(byte value, byte[] array) last Index Of

```java title=Example.java
if (array == null)
    thrownewIllegalArgumentException("array cannot be null");
return lastIndexOf(value, array, 0, array.length);
```

intlastIndexOf(byte[] array, byte valueToFind) last Index Of

```java title=Example.java
return lastIndexOf(array, valueToFind, Integer.MAX_VALUE);
```

intlastIndexOf(byte[] ary, byte value) Search for the last matching byte in an array of bytes

```java title=Example.java
return lastIndexOf(ary, 0, ary.length, value);
```

intlastIndexOf(byte[] bytes, int pos, int len, byte b) Returns the index of the last occurrence of the specified byte in the specified array.

```java title=Example.java
for (int i = len - 1; i >= pos; i--) {
    if (bytes[i] == b) {
        return i;
return -1;
```

intlastIndexOf(byte[] data, int offset, int length, byte val) last Index Of

```java title=Example.java
int i = offset + length - 1;
for (; i >= offset; i--) {
    if (data[i] == val) {
        return i - offset;
return -1;
```

intlastIndexOf(byte[] pattern, byte[] block) last Index Of

```java title=Example.java
nextPos: for (int i = pattern.length - block.length; i >= 0; i--) {
    for (int j = block.length - 1; j >= 0; j--) {
        if (pattern[j + i] == block[j]) {
            continue;
        } else {
            continue nextPos;
    return i;
return -1;
```

intlastIndexOf(byte[] s, char c) last Index Of

```java title=Example.java
if (s == null) {
    return -1;
for (int i = s.length - 1; i >= 0; i--) {
    if (s[i] == c) {
        return i;
return -1;
```
