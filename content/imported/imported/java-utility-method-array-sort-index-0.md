---
title: Java Utililty Methods Array Sort
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Sort are organized into topic(s).
section: Imported - java2s Archive
order: 50107
source: https://www.java2s.com/example/java-utility-method/array-sort-index-0.html
---
List of utility methods to do Array Sort

## Description

The list of methods to do Array Sort are organized into topic(s).

## Method

int[]addSorted(int[] array, int[] newValues) add Sorted

```java title=Example.java
if (newValues.length == 0) {
    return array;
int[] interim = newint[array.length + newValues.length];
System.arraycopy(array, 0, interim, 0, array.length);
System.arraycopy(newValues, 0, interim, array.length, newValues.length);
Arrays.sort(interim);
int count = 1;
...
```

intaddSortedUnique(T[] array, T object, int start) Adds an object to an array that presumably contains sorted elements, but only if it isn't found via binary search.

```java title=Example.java
if (Arrays.binarySearch(array, 0, start, object) < 0)
    return addSorted(array, object, start);
elsereturn -1;
```

int[]addToSortedIntArray(int[] a, int value) insert value into the sorted array a, at the index returned by java.util.Arrays.binarySearch()

```java title=Example.java
if (a == null || a.length == 0) {
    returnnewint[] { value };
int insertionPoint = -java.util.Arrays.binarySearch(a, value) - 1;
if (insertionPoint < 0) {
    thrownewIllegalArgumentException(String.format("Element %d already exists in array", value));
int[] array = newint[a.length + 1];
...
```

voidbitReversalSort(final short[] real) bit Reversal Sort

```java title=Example.java
finalint mapping[][] = newint[real.length][2];
for (int i = 0; i < mapping.length; ++i) {
    mapping[i][0] = i;
    mapping[i][1] = bitReverse31(i);
Arrays.sort(mapping, intPairComparator);
for (int i = 0; i < real.length; ++i) {
    finalint j = mapping[i][0];
...
```

doublecalculatePValueForDataPoint(double dataPoint, double[] sortedNullHypothesisSample) Calculate a p-value for the data point, given the sorted null distribution sample.

```java title=Example.java
if (sortedNullHypothesisSample.length == 0) {
    thrownewIllegalArgumentException("can't calculate a p-value with zero permutations");
} else {
    int searchResult = Arrays.binarySearch(sortedNullHypothesisSample, dataPoint);
    int permutationIndexMarker;
    if (searchResult < 1) {
        permutationIndexMarker = (-searchResult) - 1;
    } else {
...
```

Object[]collectionToSortedArray(Collection objects) collection To Sorted Array

```java title=Example.java
Object[] sortedArray = objects.toArray(newObject[] {});
Arrays.sort(sortedArray, newComparator<Object>() {
    @Overridepublicint compare(Object o1, Object o2) {
        return o1.toString().compareTo(o2.toString());
});
return sortedArray;
...
```

String[]copyAndSort(String[] input) Copy an sort the input array.

```java title=Example.java
String[] result = newString[input.length];
System.arraycopy(input, 0, result, 0, input.length);
Arrays.sort(result);
return result;
```

T[]copyAndSort(T[] builtinFunctions) copy And Sort

```java title=Example.java
T[] result = builtinFunctions.clone();
Arrays.sort(result);
return result;
```

String[]copySortArray(String[] values) copy Sort Array

```java title=Example.java
if (values == null) {
    return null;
String[] copy = newString[values.length];
System.arraycopy(values, 0, copy, 0, values.length);
Arrays.sort(copy);
return copy;
```

voidcountingSort(int[] a, int low, int high) Counting sort that sorts the integer array in O(n+k) where n is the number of elements and k is the length of the integer intervals given (high - low).

```java title=Example.java
finalint[] counts = newint[high - low + 1];
for (int x : a) {
    counts[x - low]++;
int current = 0;
for (int i = 0; i < counts.length; i++) {
    Arrays.fill(a, current, current + counts[i], i + low);
    current += counts[i];
...
```
