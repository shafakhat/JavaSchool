---
title: Java Utililty Methods Array Append
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Append are organized into topic(s).
section: Imported - java2s Archive
order: 50030
source: https://www.java2s.com/example/java-utility-method/array-append-index-0.html
---
List of utility methods to do Array Append

## Description

The list of methods to do Array Append are organized into topic(s).

## Method

intaddToArray(final int[] array, int index, final String csvString, final String delim) add To Array

```java title=Example.java
finalStringTokenizer tokenizer = newStringTokenizer(csvString, delim);
while (tokenizer.hasMoreTokens()) {
    array[index++] = Integer.parseInt(tokenizer.nextToken());
return index;
```

int[]addToArray(int[] a, int value) add To Array

```java title=Example.java
if (a == null || a.length == 0) {
    returnnewint[] { value };
int[] array = Arrays.copyOf(a, a.length + 1);
array[a.length] = value;
return array;
```

String[]addToArray(String[] items, String str) Adds a string to a string array.

```java title=Example.java
List<String> itemList;
if (items == null) {
    itemList = newArrayList<String>();
} else {
    itemList = newArrayList<String>(Arrays.asList(items));
if (str != null) {
    itemList.add(str);
...
```

byte[]appendArray(final byte[] buffer1, final byte[] buffer2) Appends the second array to the first array.

```java title=Example.java
finalbyte[] newBuffer = newbyte[buffer1.length + buffer2.length];
int pos = 0;
System.arraycopy(buffer1, 0, newBuffer, pos, buffer1.length);
pos += buffer1.length;
System.arraycopy(buffer2, 0, newBuffer, pos, buffer2.length);
return newBuffer;
```

int[][]appendArray(int[][] array, int[] staple) append Array

```java title=Example.java
int[][] output = newint[array.length + 1][];
System.arraycopy(array, 0, output, 0, array.length);
output[array.length] = staple;
return output;
```

Object[]appendArray(Object[] arr, Object obj) Append an Object at end of array

```java title=Example.java
Object[] newArr = newObject[arr.length + 1];
System.arraycopy(arr, 0, newArr, 0, arr.length);
newArr[arr.length] = obj;
return newArr;
```

Object[]appendArray(Object[] array1, Object[] array2) Appends array2 to the end of array1 and returns the result

```java title=Example.java
Object[] result = newObject[array1.length + array2.length];
System.arraycopy(array1, 0, result, 0, array1.length);
System.arraycopy(array2, 0, result, array1.length, array2.length);
return result;
```

String[]appendArray(String[] A, String... B) Appends String(s) B to array A.

```java title=Example.java
return concatArrays(A, B);
```

voidappendArray(StringBuilder bld, Object[] array, String sep) Appends an array to a string builder using the specified separator string.

```java title=Example.java
String curSep = "";
for (Object obj : array) {
    bld.append(curSep);
    bld.append(obj);
    curSep = sep;
```

StringBuilderappendArray(StringBuilder sb, int[] arr) append Array

```java title=Example.java
for (int i : arr) {
    sb.append(i);
    sb.append(System.getProperty("line.separator"));
return sb;
```
