---
title: Java Utililty Methods Array Range Copy
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Range Copy are organized into topic(s).
section: Imported - java2s Archive
order: 50093
source: https://www.java2s.com/example/java-utility-method/array-range-copy-index-0.html
---
List of utility methods to do Array Range Copy

## Description

The list of methods to do Array Range Copy are organized into topic(s).

## Method

boolean[]copyOf(boolean[] array, int length) Returns a copy of the given array of size 1 greater than the argument.

```java title=Example.java
boolean[] anew = newboolean[length];
for (int i = 0; i < length; i++) {
    if (i < array.length) {
        anew[i] = array[i];
        continue;
    anew[i] = false;
return anew;
```

byte[]copyOf(byte[] arr, int newLength) Returns a copy of the given array of the given length.

```java title=Example.java
return copyOf(arr, 0, newLength, 0);
```

byte[]copyOf(byte[] b) Creates a copy of the given byte array.

```java title=Example.java
if (b == null) {
    return null;
return copyOf(b, 0, b.length);
```

byte[]copyOf(byte[] b, int off, int len) copy Of

```java title=Example.java
if (off == 0 && len == b.length)
    return b;
byte[] br = newbyte[len];
System.arraycopy(b, off, br, 0, len);
return br;
```

byte[]copyOf(byte[] b, int off, int len) Creates a copy of a section of the given byte array.

```java title=Example.java
if (b == null) {
    thrownewNullPointerException();
if (off < 0 || len < 0 || off > b.length - len) {
    thrownewArrayIndexOutOfBoundsException();
byte[] copy = newbyte[len];
System.arraycopy(b, off, copy, 0, len);
...
```

byte[]copyOf(byte[] bytes) copy Of

```java title=Example.java
return copyOfRange(bytes, 0, bytes.length);
```

byte[]copyOf(byte[] bytes, int startIndex, int length) Returns a new byte array of 'length' size containing the contents of the provided 'bytes' array beginning at startIndex to (startIndex+length-1)

```java title=Example.java
byte[] newByteArray = newbyte[length];
for (int i = 0; i < length; i++) {
    newByteArray[i] = bytes[i + startIndex];
return newByteArray;
```

byte[]copyOf(byte[] original, int newLength) Replacement for Java6 Arrays#copyOf(byte[],int) .

```java title=Example.java
byte[] result = newbyte[newLength];
System.arraycopy(original, 0, result, 0, Math.min(newLength, original.length));
return result;
```

byte[]copyOf(byte[] original, int newLength) Copies the specified array, truncating or padding with zeros (if necessary) so the copy has the specified length.

```java title=Example.java
byte[] copy = newbyte[newLength];
System.arraycopy(original, 0, copy, 0, Math.min(original.length, newLength));
return copy;
```

byte[]copyOf(byte[] original, int newLength) copy Of

```java title=Example.java
if (newLength < 0) {
    thrownewIllegalArgumentException();
byte[] buf = newbyte[newLength];
int lastIndex = Math.min(original.length, newLength);
System.arraycopy(original, 0, buf, 0, lastIndex);
return buf;
```
