---
title: Java Utililty Methods Array Search
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Search are organized into topic(s).
section: Imported - java2s Archive
order: 50101
source: https://www.java2s.com/example/java-utility-method/array-search-index-0.html
---
List of utility methods to do Array Search

## Description

The list of methods to do Array Search are organized into topic(s).

## Method

intarraySearch(byte[] array, byte[] search) array Search

```java title=Example.java
if (search.length == 0) {
    return -1;
int found = 0;
loop: while (true) {
    found = binarySearch(array, search[0], found + 1);
    if (found < 0 || found > array.length) {
        return -1;
...
```

intarraySearch(int[] arr, int i) array Search

```java title=Example.java
for (int j = 0; j < arr.length; j++) {
    if (arr[j] == i)
        return j;
return -1;
```

intbyteArraySearch(byte[] data, byte[] searchData) byte Array Search

```java title=Example.java
for (int i = 0; i <= data.length - searchData.length; i++) {
    if (data[i] == searchData[0] && Arrays.equals(searchData, extractBytes(data, i, searchData.length)))
        return i;
return -1;
```

booleancontains(byte[] array, byte toSearch) contains

```java title=Example.java
byte[] copy = newbyte[array.length];
System.arraycopy(array, 0, copy, 0, array.length);
Arrays.sort(copy);
returnArrays.binarySearch(copy, toSearch) >= 0;
```

intgetFoundIdx(char to_find, char[] to_search, boolean do_orderAsc)

Get the (first) index at which a char exists in a char-array.

```java title=Example.java
if (to_search == null) {
    thrownewNullPointerException("to_search");
if (do_orderAsc) {
    returnArrays.binarySearch(to_search, to_find);
for (int i = 0; i < to_search.length; i++) {
    if (to_find == to_search[i]) {
...
```

intindexOf(T[] array, T toSearch) Returns the index of the element to search in the given array.

```java title=Example.java
int index = -1;
if (array != null) {
    int i = 0;
    while (i < array.length && index < 0) {
        if (array[i] != null ? array[i].equals(toSearch) : toSearch == null) {
            index = i;
        i++;
...
```

booleanisIn(char to_find, char[] to_search)

Is the char in the char-array?.

```java title=Example.java
return (getFoundIdx(to_find, to_search) > -1);
```

booleanisIn(String name, String[] array) Inspects the array to see if it contains the passed string.

```java title=Example.java
if (array == null || name == null)
    return false;
returnArrays.binarySearch(array, name) >= 0;
```

booleanisIn(String name, String[] array) Inspects the array to see if it contains the passed string.

```java title=Example.java
if (array == null || name == null)
    return false;
returnArrays.binarySearch(array, name) >= 0;
```

booleanisInArray(final T ch, final T[] a) is In Array

```java title=Example.java
returnArrays.stream(a).anyMatch(item -> ch.equals(item));
```
