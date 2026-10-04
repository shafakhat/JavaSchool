---
title: Java Utililty Methods Array Rotate
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Rotate are organized into topic(s).
section: Imported - java2s Archive
order: 50099
source: https://www.java2s.com/example/java-utility-method/array-rotate-index-0.html
---
List of utility methods to do Array Rotate

## Description

The list of methods to do Array Rotate are organized into topic(s).

## Method

ListfindAllPossibleRightRotations(int[][] matrix) returns all 360 rotations in clock-wise in given matrix

```java title=Example.java
List<int[][]> allPossibleRotations = newArrayList<>();
for (int i = 0; i < 3; i++) {
    matrix = rotateClockWise(matrix);
    allPossibleRotations.add(matrix);
return allPossibleRotations;
```

Object[]rotateArray(Object[] array, int amt) rotate Array

```java title=Example.java
Object[] arr = Arrays.copyOf(array, array.length);
if (arr == null || amt < 0) {
    thrownewIllegalArgumentException("Illegal argument!");
for (int i = 0; i < amt; i++) {
    for (int j = arr.length - 1; j > 0; j--) {
        Object temp = arr[j];
        arr[j] = arr[j - 1];
...
```

voidrotateArrayRange(int[] array, int from, int to, int n) rotate Array Range

```java title=Example.java
rotateArrayRange(array, from, to, n, Arrays.copyOfRange(array, from, to));
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
