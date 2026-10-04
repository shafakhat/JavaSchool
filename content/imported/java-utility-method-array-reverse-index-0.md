---
title: Java Utililty Methods Array Reverse
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Reverse are organized into topic(s).
section: Imported - java2s Archive
order: 50098
source: https://www.java2s.com/example/java-utility-method/array-reverse-index-0.html
---
List of utility methods to do Array Reverse

## Description

The list of methods to do Array Reverse are organized into topic(s).

## Method

voidarrayReverse(byte[] array, int begin, int length) array Reverse

```java title=Example.java
int i = begin;
int j = begin + length - 1;
byte tmp;
while (i < j) {
    tmp = array[i];
    array[i] = array[j];
    array[j] = tmp;
    ++i;
...
```

voidarrayReverse(Object[] array) array Reverse

```java title=Example.java
if (array == null) {
    return;
Object tmp;
for (int i = 0, j = array.length - 1; j > i; i++, j--) {
    tmp = array[j];
    array[j] = array[i];
    array[i] = tmp;
...
```

voidarrayReverse(Object[] array) array Reverse

```java title=Example.java
if (array == null) {
    return;
Object tmp;
for (int i = 0, j = array.length - 1; j > i; i++, j--) {
    tmp = array[j];
    array[j] = array[i];
    array[i] = tmp;
...
```

T[]arrayReverse(T[] array) Reverses the given array.

```java title=Example.java
Object[] reverseArray = newObject[array.length];
for (int i = 0; i < array.length; i++) {
    reverseArray[array.length - 1 - i] = array[i];
return (T[]) reverseArray;
```

byte[]ArraysReverse(byte[] array) Arrays Reverse

```java title=Example.java
for (int i = 0; i < array.length / 2; i++) {
    byte temp = array[i];
    array[i] = array[array.length - i - 1];
    array[array.length - i - 1] = temp;
return array;
```

ListgetReverseOffsets(long fileLength, long position, byte[] buffer, int size) get Reverse Offsets

```java title=Example.java
List<Long> offsets = newArrayList<Long>();
if (size > 0) {
    for (int ii = size - 1; ii >= 0; ii--) {
        if ('\n' == buffer[ii] && (fileLength != position + ii + 1)) {
            offsets.add(position + ii + 1);
return offsets;
```

T[]reverse(T[] array) reverse

```java title=Example.java
List<T> list = Arrays.asList(array);
Collections.reverse(list);
return (T[]) list.toArray();
```

T[]reverse(T[] array) reverse

```java title=Example.java
T[] sub = Arrays.copyOf(array, array.length);
for (int i = 0; i < array.length; i++) {
    sub[i] = array[array.length - i - 1];
return sub;
```

voidreverse(T[] array) Reverses the order of the elements in the specified array.

```java title=Example.java
if (array != null) {
    finalList<T> list = Arrays.asList(array);
    Collections.reverse(list);
```

T[]reverse(T[] array) reverse

```java title=Example.java
if (array != null && array.length > 1) {
    for (int i = 0; i < array.length / 2; i++) {
        swap(array, i, array.length);
return array;
```
