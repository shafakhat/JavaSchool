---
title: Java Utililty Methods Array Remove
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Remove are organized into topic(s).
section: Imported - java2s Archive
order: 50095
source: https://www.java2s.com/example/java-utility-method/array-remove-index-0.html
---
List of utility methods to do Array Remove

## Description

The list of methods to do Array Remove are organized into topic(s).

## Method

boolean[]remove(boolean[] array, boolean value) remove

```java title=Example.java
List<Boolean> list = newArrayList<Boolean>();
for (int i = 0; i < array.length; i++) {
    if (value != array[i]) {
        list.add(newBoolean(array[i]));
return toArray(list.toArray(newBoolean[list.size()]));
```

int[]remove(int[] a, int[] b) remove

```java title=Example.java
Arrays.sort(a);
Arrays.sort(b);
int[] rest = null;
int k = 0;
if (a.length > 0 && b.length > 0) {
    rest = Arrays.copyOf(b, b.length);
    for (int j = 0; j < b.length; j++) {
        for (int i = 0; i < a.length; i++) {
...
```

String[]remove(String[] initial, String... toExclude) remove

```java title=Example.java
List<String> result = newArrayList<String>();
result.addAll(Arrays.asList(initial));
result.removeAll(Arrays.asList(toExclude));
return result.toArray(newString[result.size()]);
```

String[]remove(String[] target, String[] needRemoved) remove

```java title=Example.java
if (target == null) {
    thrownewRuntimeException("target array is null!");
if (isEmpty(needRemoved)) {
    return target;
String[] result = target;
for (String needRemove : needRemoved) {
...
```

T[]remove(T[] a, int i) remove

```java title=Example.java
T[] tmp = Arrays.copyOf(a, a.length - 1);
System.arraycopy(a, i + 1, tmp, i, tmp.length - i);
return tmp;
```

E[]removeAll(E[] array, Object... toRemove) remove All

```java title=Example.java
final E[] removed = Arrays.copyOf(array, array.length - count(array, toRemove));
int index = 0;
for (E element : array) {
    if (!contains(toRemove, element)) {
        removed[index++] = element;
return removed;
...
```

MapremoveAll(T[] array, Collection toRemove) Remove the specified elements from the array in-place, replacing them with null .

```java title=Example.java
Map<T, Integer> removed = newHashMap<>();
for (int i = 0; i < array.length; i++) {
    T element = array[i];
    if (toRemove.contains(element)) {
        array[i] = null;
        removed.put(element, i);
return removed;
```

T[]removeAll(T[] items, T item) Remove any occurrence of a given value from an array.

```java title=Example.java
int count = 0;
for (int i = 0; i != items.length; ++i) {
    T ith = items[i];
    if (ith == item || (item != null && item.equals(ith))) {
        count++;
if (count == 0) {
...
```

StringRemoveArgs(String[] args, int startIndex) Remove Args

```java title=Example.java
List<String> list = removeFirstTwoArgs(args, startIndex);
String convertedString = convertToString(list);
return convertedString;
```

T[]removeAt(T[] array, int index) Removes the element at the index from the array and returns a new array.

```java title=Example.java
System.arraycopy(array, index + 1, array, index, array.length - index - 1);
returnArrays.copyOf(array, array.length - 1);
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
