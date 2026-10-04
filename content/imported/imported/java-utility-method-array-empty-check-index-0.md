---
title: Java Utililty Methods Array Empty Check
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Empty Check are organized into topic(s).
section: Imported - java2s Archive
order: 50062
source: https://www.java2s.com/example/java-utility-method/array-empty-check-index-0.html
---
List of utility methods to do Array Empty Check

## Description

The list of methods to do Array Empty Check are organized into topic(s).

## Method

booleanareArraysEqual(byte[] arr1, byte[] arr2, boolean dontDistinctNilAndEmpty) are Arrays Equal

```java title=Example.java
if (!dontDistinctNilAndEmpty)
    returnArrays.equals(arr1, arr2);
if (arr1 == null || arr1.length == 0)
    return arr2 == null || arr2.length == 0;
returnArrays.equals(arr1, arr2);
```

Object[][]getNonemptySubsets(Object[] objects) Gets all non-empty subsets of the given array of objects.

```java title=Example.java
Object[][] subsets = getAllSubsets(objects);
Object[][] nonempty = newObject[subsets.length - 1][];
for (int i = 0; i < nonempty.length; i++)
    nonempty[i] = subsets[i + 1];
return nonempty;
```

String[]getWithoutEmptyParams(String[] cmdarray) get Without Empty Params

```java title=Example.java
if (cmdarray == null) {
    return null;
ArrayList<String> list = newArrayList<String>();
for (String string : cmdarray) {
    if (string != null && string.length() > 0) {
        list.add(string);
return list.toArray(newString[list.size()]);
```

booleanhasOneEmpty(String[] args) has One Empty

```java title=Example.java
if (args == null)
    return false;
for (int i = 0; i < args.length; i++) {
    if (isEmpty(args[i]))
        return true;
return false;
```

booleanisEmpty(boolean[] values) is Empty

```java title=Example.java
return values == null || values.length == 0;
```

booleanisEmpty(byte[] array) is Empty

```java title=Example.java
byte[] empty = newbyte[array.length];
returnArrays.equals(array, empty);
```

booleanisEmpty(E[] array) is Empty

```java title=Example.java
return (array == null || array.length == 0);
```

booleanisEmpty(final int[] arr) is Empty

```java title=Example.java
return arr.length == 0;
```

booleanisEmpty(final Object[] array) Is the given array null or empty ?

```java title=Example.java
return array == null || array.length == 0;
```

booleanisEmpty(final X[] array) is Empty

```java title=Example.java
return (isNull(array) || 0 == array.length);
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
