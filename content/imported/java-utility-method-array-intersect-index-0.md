---
title: Java Utililty Methods Array Intersect
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Intersect are organized into topic(s).
section: Imported - java2s Archive
order: 50075
source: https://www.java2s.com/example/java-utility-method/array-intersect-index-0.html
---
List of utility methods to do Array Intersect

## Description

The list of methods to do Array Intersect are organized into topic(s).

## Method

doublearrayInterp(double[] inputArray, double index) array Interp

```java title=Example.java
int cap = inputArray.length - 1;
if (index <= 0) {
    return inputArray[0];
} elseif (index >= cap) {
    return inputArray[cap];
} else {
    int first = (int) Math.floor(index);
    double offset = index - first;
...
```

booleanarraysIntersect(Object[] array1, Object[] array2) Check if two arrays have at least one common element.

```java title=Example.java
boolean intersect = false;
for (int i = 0; i < array1.length && !intersect; ++i) {
    Object e1 = array1[i];
    if (e1 != null) {
        for (int j = 0; j < array2.length && !intersect; ++j) {
            Object e2 = array2[j];
            intersect = e1.equals(e2);
return intersect;
```

byte[]byteIntersection(byte[] a, byte[] b) byte Intersection

```java title=Example.java
int max = Math.max(a.length, b.length);
byte[] newarray = newbyte[max];
Arrays.fill(newarray, (byte) 0);
for (int i = 0; i < max; i++) {
    byte aval = 0;
    byte bval = 0;
    if (i >= a.length) {
        aval = 0;
...
```

int[]getArrayIntersection(int a[], int b[]) get Array Intersection

```java title=Example.java
returnArrays.stream(a).flatMap(i -> Arrays.stream(b).filter(j -> i == j)).distinct().toArray();
```

ListgetNonIntersection(int[] interval, int[] intervalToRemove) Returns interval(s) of non-intersection area for interval1

```java title=Example.java
List<int[]> outList = newArrayList<int[]>();
int[] intersection = getIntersection(interval, intervalToRemove);
if (intersection[0] == interval[0]) {
    if (intersection[1] == interval[1]) {
    } else {
        outList.add(newint[] { intersection[1] + 1, interval[1] });
    return outList;
...
```

booleanhasIntersection(String a1[], String a2[], int mode) has Intersection

```java title=Example.java
if (a1 == null || a2 == null)
    return false;
if (a1 == a2)
    return a1.length > 0;
java.util.List<String> v = newArrayList<String>();
createIntersection(a1, a2, mode, v, false);
return v.size() > 0;
```

intintersect(boolean[] mask, int[] examples, boolean[] intersection) A generic intersect function that

```java title=Example.java
if (intersection.length != mask.length)
    thrownewRuntimeException("Argument and return value have different length.");
Arrays.fill(intersection, false);
int count = 0;
for (int i = 0; i < examples.length; i++)
    if (mask[examples[i]]) {
        intersection[examples[i]] = true;
        count++;
...
```

int[]intersect(int[] sorted1, int[] sorted2) intersect

```java title=Example.java
int[] result = newint[Math.min(sorted1.length, sorted2.length)];
int i = 0, j = 0, k = 0;
while (i < sorted1.length && j < sorted2.length) {
    if (sorted1[i] < sorted2[j])
        i++;
    elseif (sorted1[i] > sorted2[j])
        j++;
    else {
...
```

int[]intersect(int[]... arrays) Returns the intersection vector of a series of input arrays.

```java title=Example.java
if (arrays.length == 0)
    returnnewint[0];
Set<Integer> intersectionSet = newLinkedHashSet<Integer>();
intersectionSet.addAll(toList(arrays[0]));
for (int i = 1; i < arrays.length; i++)
    intersectionSet.retainAll(toList(arrays[i]));
return toArray(intersectionSet);
```

String[]intersect(String[] arr1, String[] arr2) intersect

```java title=Example.java
Map<String, Boolean> map = newHashMap<String, Boolean>();
LinkedList<String> list = newLinkedList<String>();
for (String str : arr1) {
    if (!map.containsKey(str)) {
        map.put(str, Boolean.FALSE);
for (String str : arr2) {
...
```
