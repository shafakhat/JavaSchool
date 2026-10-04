---
title: Java Utililty Methods Array Has
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Has are organized into topic(s).
section: Imported - java2s Archive
order: 50070
source: https://www.java2s.com/example/java-utility-method/array-has-index-0.html
---
List of utility methods to do Array Has

## Description

The list of methods to do Array Has are organized into topic(s).

## Method

booleanarrayHas(int[] arr, int val) Helper method to check if an int array contains an int.

```java title=Example.java
for (int element : arr)
    if (element == val)
        return true;
return false;
```

booleanarrayHasContent(Object[] array) Helper method to determine whether an array has any content.

```java title=Example.java
if (array != null) {
    for (int i = 0; i < array.length; ++i) {
        if (array[i] != null) {
            return true;
return false;
...
```

booleanarrayHasContiguousRowEntries(double[] aVector) Test a vector to see if there is a block of contiguous nonzero values present.

```java title=Example.java
int nnz = numberOfNonZeroElementsInVector(aVector);
if (nnz == 0) {
    return true;
if (nnz == 1) {
    return true;
int dataStartsAt = 0;
...
```

booleanarrayHasElements(Object[] obj) array Has Elements

```java title=Example.java
if (obj != null && obj.length != 0) {
    for (Object object : obj) {
        if (object != null) {
            return true;
return false;
...
```

booleanarrayHasTaints(int[] a) array Has Taints

```java title=Example.java
for (int i : a)
    if (i != 0)
        return true;
return false;
```

booleaninArray(byte needle, byte[] haystack) in Array

```java title=Example.java
for (byte item : haystack) {
    if (item == needle) {
        return true;
return false;
```

booleaninArray(byte needle, byte[] haystack) in Array

```java title=Example.java
for (byte item : haystack) {
    if (item == needle) {
        return true;
return false;
```

booleaninArray(char[] array, char c) in Array

```java title=Example.java
char[] arr$ = array;
int len$ = array.length;
for (int i$ = 0; i$ < len$; ++i$) {
    char ch = arr$[i$];
    if (ch == c) {
        return true;
return false;
```

booleaninArray(final String s, final String[] array) in Array

```java title=Example.java
for (String item : array) {
    if (item != null && item.equals(s)) {
        return true;
return false;
```

booleaninArray(final T[] array, final U search) Check whether the given array contains the given search object.

```java title=Example.java
for (final T element : array)
    if (search.equals(element))
        return true;
return false;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
