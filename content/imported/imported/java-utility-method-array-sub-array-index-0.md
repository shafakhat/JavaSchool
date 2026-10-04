---
title: Java Utililty Methods Array Sub Array
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Sub Array are organized into topic(s).
section: Imported - java2s Archive
order: 50111
source: https://www.java2s.com/example/java-utility-method/array-sub-array-index-0.html
---
List of utility methods to do Array Sub Array

## Description

The list of methods to do Array Sub Array are organized into topic(s).

## Method

String[]sub(String[] a, String[] b) subtract b from a

```java title=Example.java
TreeSet<String> s = newTreeSet<>(Arrays.asList(a));
s.removeAll(Arrays.asList(b));
if (s.size() != a.length) {
    return s.toArray(newString[s.size()]);
} else {
    return a;
```

Listsub(T[] source, int first, int last) sub

```java title=Example.java
if (first < 0 || last < 0 || first >= source.length || last >= source.length)
    thrownewArrayIndexOutOfBoundsException();
List<T> result = newArrayList<T>();
for (int i = first; i <= last; i++)
    result.add(source[i]);
return result;
```

boolean[]subarray(boolean[] array, int fromIndex, int length) Building on the arraycopy function in System, this function returns a "subarray" of a larger array.

```java title=Example.java
boolean[] tempArray = newboolean[length];
try {
    System.arraycopy(array, fromIndex, tempArray, 0, tempArray.length);
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
    System.out.println("Array of length:" + array.length);
    System.out.println("From index with length:" + fromIndex + "," + length);
    System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
...
```

byte[]subArray(byte[] a, int beginIndex, int endIndex) Returns the new array that is the sub-array of the specified array .

```java title=Example.java
if (a == null || a.length == 0 || beginIndex < 0 || endIndex > a.length || beginIndex > endIndex) {
    returnnewbyte[0];
} else {
    byte[] b = newbyte[endIndex - beginIndex];
    System.arraycopy(a, beginIndex, b, 0, b.length);
    return b;
```

byte[]subArray(byte[] array, int beginIndex, int endIndex) Extract a sub array of bytes out of the byte array.

```java title=Example.java
int length = endIndex - beginIndex;
byte[] subarray = newbyte[length];
System.arraycopy(array, beginIndex, subarray, 0, length);
return subarray;
```

byte[]subarray(byte[] array, int offset, int length) NOTE: subarray method implemented for arrays of type byte Extracts a sub array from an array of a primitive type.

```java title=Example.java
validateOffsetLength(array, array.length, offset, length);
byte[] sub = newbyte[length];
for (int i = 0; i < length; i++)
    sub[i] = array[offset + i];
return sub;
```

byte[]subarray(byte[] array, int startIndexInclusive, int endIndexExclusive)

Produces a new byte array containing the elements between the start and end indices.

The start index is inclusive, the end index exclusive. if (array == null) { return null; if (startIndexInclusive < 0) { startIndexInclusive = 0; if (endIndexExclusive > array.length) { endIndexExclusive = array.length; ...

byte[]subarray(byte[] array, int startIndexInclusive, int endIndexExclusive) subarray

```java title=Example.java
if (array == null) {
    return null;
if (startIndexInclusive < 0) {
    startIndexInclusive = 0;
if (endIndexExclusive > array.length) {
    endIndexExclusive = array.length;
...
```

byte[]subArray(byte[] b, int offset, int length) Return a subarray of the byte array in parameter.

```java title=Example.java
byte[] sub = newbyte[length];
for (int i = offset; i < offset + length; i++)
    sub[i - offset] = b[i];
return sub;
```

byte[]subarray(byte[] b, int ofs, int len) subarray

```java title=Example.java
byte[] out = newbyte[len];
System.arraycopy(b, ofs, out, 0, len);
return out;
```
