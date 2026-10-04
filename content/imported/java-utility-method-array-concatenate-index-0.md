---
title: Java Utililty Methods Array Concatenate
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Concatenate are organized into topic(s).
section: Imported - java2s Archive
order: 50041
source: https://www.java2s.com/example/java-utility-method/array-concatenate-index-0.html
---
List of utility methods to do Array Concatenate

## Description

The list of methods to do Array Concatenate are organized into topic(s).

## Method

String[][]arraycat(String[][] array1, String[][] array2) Concatenates two String[][] arrays.

```java title=Example.java
String[][] Result = newString[array1.length + array2.length][];
int i = 0;
for (int j = 0; j < array1.length; j++)
    Result[i++] = array1[j];
for (int j = 0; j < array2.length; j++)
    Result[i++] = array2[j];
returnResult;
```

byte[]arrayConcat(byte[] a, byte[] b) array Concat

```java title=Example.java
int lenA = a.length;
int lenB = b.length;
byte[] out = newbyte[lenA + lenB];
System.arraycopy(a, 0, out, 0, lenA);
System.arraycopy(b, 0, out, lenA, lenB);
return out;
```

byte[]arrayConcat(final byte[] firstArray, final byte[] secondArray) array Concat

```java title=Example.java
finalint aLen = firstArray.length;
finalint bLen = secondArray.length;
finalbyte[] combinedArray = newbyte[aLen + bLen];
System.arraycopy(firstArray, 0, combinedArray, 0, aLen);
System.arraycopy(secondArray, 0, combinedArray, aLen, bLen);
return combinedArray;
```

String[]arrayConcat(String[] first, String second) Returns a new array adding the second array at the end of first array.

```java title=Example.java
if (second == null)
    return first;
if (first == null)
    returnnewString[] { second };
int length = first.length;
if (first.length == 0) {
    returnnewString[] { second };
String[] result = newString[length + 1];
System.arraycopy(first, 0, result, 0, length);
result[length] = second;
return result;
```

T[]arrayConcat(T[] a, T[] b) array Concat

```java title=Example.java
if (a == null)
    thrownewIllegalArgumentException("'a' can't be null");
if (b == null)
    thrownewIllegalArgumentException("'b' can't be null");
T[] rn = Arrays.copyOf(a, a.length + b.length);
System.arraycopy(b, 0, rn, a.length, b.length);
T[] r = rn;
return r;
...
```

T[]arrayConcat(T[] first, T[] second) Concatenate two arrays of type T and produce a new of the same type.

```java title=Example.java
T[] combinedArray = Arrays.copyOf(first, first.length + second.length);
System.arraycopy(second, 0, combinedArray, first.length, second.length);
return combinedArray;
```

T[]arrayConcat(T[] first, T[] second) Concatenate two arrays.

```java title=Example.java
T[] result = Arrays.copyOf(first, first.length + second.length);
System.arraycopy(second, 0, result, first.length, second.length);
return result;
```

String[]arrayConcatenate(final String[] f, final String[] s) array Concatenate

```java title=Example.java
finalint fLen = (f == null ? 0 : f.length);
finalint sLen = (s == null ? 0 : s.length);
finalint len = fLen + sLen;
finalString[] ret = newString[len];
if (fLen > 0) {
    System.arraycopy(f, 0, ret, 0, fLen);
    if (sLen > 0) {
        System.arraycopy(s, 0, ret, fLen, sLen);
...
```

String[]arrayConcatenate(String[] first, String[] second) array Concatenate

```java title=Example.java
String[] ret = newString[first.length + second.length];
System.arraycopy(first, 0, ret, 0, first.length);
System.arraycopy(second, 0, ret, first.length, second.length);
return ret;
```

int[]arrayConcatInt(final int[] original, final int[] appender) Concatenates two integer arrays

```java title=Example.java
finalint[] result = Arrays.copyOf(original, original.length + appender.length);
System.arraycopy(appender, 0, result, original.length, appender.length);
return result;
```
