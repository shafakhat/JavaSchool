---
title: Java Utililty Methods Array Capacity
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Capacity are organized into topic(s).
section: Imported - java2s Archive
order: 50033
source: https://www.java2s.com/example/java-utility-method/array-capacity-index-0.html
---
List of utility methods to do Array Capacity

## Description

The list of methods to do Array Capacity are organized into topic(s).

## Method

byte[]ensureCapacity(byte array[], int capacity) ensure Capacity

```java title=Example.java
if (capacity <= 0 || capacity - array.length <= 0)
    return array;
int newCapacity = array.length * 2;
if (newCapacity - capacity < 0)
    newCapacity = capacity;
if (newCapacity < 0) {
    if (capacity < 0)
        thrownewOutOfMemoryError();
...
```

byte[]ensureCapacity(byte[] bytes, int capacity) Utility method used to ensure the capacity of byte array.

```java title=Example.java
if (bytes.length < capacity) {
    int newsize = Math.max(1, bytes.length) << 1;
    bytes = Arrays.copyOf(bytes, newsize);
return bytes;
```

double[]ensureCapacity(final double[] array, final int minCapacity) ensure Capacity

```java title=Example.java
if (array.length < minCapacity) {
    returnArrays.copyOf(array, minCapacity);
return array;
```

T[]ensureCapacity(final T[] oldElements, final int requiredLength) Ensure an array has the required capacity.

```java title=Example.java
T[] result = oldElements;
if (oldElements.length < requiredLength) {
    result = Arrays.copyOf(oldElements, requiredLength);
return result;
```

Object[]reduceCapacity(Object[] arrays) reduce Capacity

```java title=Example.java
if (arrays == null) {
    return null;
int lastIndex = arrays.length - 1;
int length = arrays.length;
for (int i = lastIndex; i >= 0; i--) {
    if (arrays[i] == null) {
        length--;
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
