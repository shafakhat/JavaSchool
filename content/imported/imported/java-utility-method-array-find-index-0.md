---
title: Java Utililty Methods Array Find
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Find are organized into topic(s).
section: Imported - java2s Archive
order: 50066
source: https://www.java2s.com/example/java-utility-method/array-find-index-0.html
---
List of utility methods to do Array Find

## Description

The list of methods to do Array Find are organized into topic(s).

## Method

booleanfindAll(int[] arr1, int[] arr2) find All

```java title=Example.java
for (int a1 : arr1) {
    if (!find(a1, arr2)) {
        return false;
return true;
```

ListfindAllArgumentPermutations(Object[][] allArguments) Permute all possible parameters

```java title=Example.java
return findAllArgumentPermutations(allArguments, 0, 0, newObject[allArguments.length],
        newArrayList<Object[]>());
```

ListfindAllOrientations(int[][] matrix) find all orientations of any matrix or piece provided

```java title=Example.java
List<int[][]> allPossibleRotations = newArrayList<>();
allPossibleRotations.add(matrix);
allPossibleRotations.add(flipInPlace(matrix));
allPossibleRotations.add(mirror(matrix[0].length, matrix.length, matrix));
allPossibleRotations.addAll(findAllPossibleRightRotations(allPossibleRotations.get(0)));
allPossibleRotations.addAll(findAllPossibleRightRotations(allPossibleRotations.get(2)));
return allPossibleRotations;
```

intgetIndex(double income, String[] scopes) get Index

```java title=Example.java
int len = scopes.length;
len++;
double[] vals = newdouble[len];
vals[0] = income;
for (int i = 1; i < len; i++) {
    vals[i] = Long.parseLong(scopes[i - 1]);
Arrays.sort(vals);
...
```

intgetIndex(String[] array, String value) get Index

```java title=Example.java
if (array == null)
    thrownewRuntimeException("Can't do index. Collection is Null");
for (int i = 0; i < array.length; i++)
    if (array[i].equals(value))
        return i;
return -1;
```

intgetIndexObject(Object[] data, Object object) Find the index of an element in an array.

```java title=Example.java
int x = newArrayList<>(Arrays.asList(data)).indexOf(object);
if (x == -1) {
    thrownewNoSuchElementException("StringUtils : index lookup in array failed for object " + object
            + ". Data length is " + data.length);
return x;
```

ArrayListgetIndexOf(int i, int[] array) get Index Of

```java title=Example.java
if (isEmpty(array)) {
    return null;
ArrayList<Integer> result = newArrayList<Integer>();
for (int index = 0; index < array.length; index++) {
    int num = array[index];
    if (i == num) {
        result.add(index);
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
