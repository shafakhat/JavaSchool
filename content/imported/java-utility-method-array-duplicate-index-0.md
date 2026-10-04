---
title: Java Utililty Methods Array Duplicate
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Duplicate are organized into topic(s).
section: Imported - java2s Archive
order: 50060
source: https://www.java2s.com/example/java-utility-method/array-duplicate-index-0.html
---
List of utility methods to do Array Duplicate

## Description

The list of methods to do Array Duplicate are organized into topic(s).

## Method

String[]addNoDuplicate(String[] array, String target) add No Duplicate

```java title=Example.java
List<String> list = Arrays.asList(array);
if (!list.contains(target)) {
    list.add(target);
String[] result = list.toArray(newString[0]);
return result;
```

byte[]arrayDuplicate(byte[] in) array Duplicate

```java title=Example.java
byte[] out = newbyte[in.length];
arrayCopy(out, 0, in);
return out;
```

int[]deleteDuplicatedPages(int[] pages) Transforms (0,1,2,2,3) to (0,1,2,3)

```java title=Example.java
List<Integer> result = newArrayList<Integer>();
int lastInt = -1;
for (Integer currentInt : pages) {
    if (lastInt != currentInt) {
        result.add(currentInt);
    lastInt = currentInt;
int[] arrayResult = newint[result.size()];
for (int i = 0; i < result.size(); i++) {
    arrayResult[i] = result.get(i);
return arrayResult;
```

String[]duplicateArrayEntries(String[] inputArr, int numDuplicates) duplicate Array Entries

```java title=Example.java
List<String> list = newArrayList<String>();
for (String d : inputArr) {
    for (int i = 0; i < numDuplicates; i++) {
        list.add(d);
return list.toArray(newString[0]);
```

String[]eraseDuplicatedValue(String[] srcArr) Erase Duplicated method

```java title=Example.java
List tempVector = newArrayList();
int loopCount = 0;
for (loopCount = 0; loopCount < srcArr.length; loopCount++) {
    tempVector.add(srcArr[loopCount]);
Collections.sort(tempVector);
for (loopCount = 0; loopCount < srcArr.length; loopCount++) {
    srcArr[loopCount] = (String) (tempVector.get(loopCount));
...
```

booleanhasDuplicates(final T[] array) Determines whether a given array contains duplicate values.

```java title=Example.java
if (array == null) {
    thrownewIllegalArgumentException();
for (int i = 0; i < array.length - 1; i++) {
    final T x = array[i];
    for (int j = i + 1; j < array.length; j++) {
        final T y = array[j];
        if (x.equals(y)) {
...
```

booleanisDuplicated(String[] strArray) Check if there are duplicated values in a string array

```java title=Example.java
Set<String> strSet = newHashSet<String>();
for (int i = 0; i < strArray.length; i++) {
    strSet.add(strArray[i]);
return (strSet.size() < strArray.length) ? true : false;
```

double[]removeDuplicates(double[] array) remove Duplicates

```java title=Example.java
double[] result = null;
Map<Double, Object> values = newHashMap<Double, Object>(array.length);
for (double value : array)
    values.put(value, newObject());
    int i = 0;
    result = newdouble[values.size()];
    for (double value : values.keySet())
...
```

Object[]removeDuplicates(final Object[] array) Remove duplicate objects from an array

```java title=Example.java
if (isNull(array)) {
    return null;
try {
    List listNewPks = newArrayList();
    listNewPks.addAll(newLinkedHashSet(Arrays.asList(array)));
    return listNewPks.toArray();
} catch (Exception e) {
...
```

int[]removeDuplicates(int[] input) Remove duplicate elements from an int array

```java title=Example.java
if (input.length < 2) {
    return input;
Arrays.sort(input);
int j = 0;
int i = 1;
while (i < input.length) {
    if (input[i] == input[j]) {
...
```
