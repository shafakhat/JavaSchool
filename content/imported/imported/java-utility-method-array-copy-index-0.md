---
title: Java Utililty Methods Array Copy
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Copy are organized into topic(s).
section: Imported - java2s Archive
order: 50044
source: https://www.java2s.com/example/java-utility-method/array-copy-index-0.html
---
List of utility methods to do Array Copy

## Description

The list of methods to do Array Copy are organized into topic(s).

## Method

voidarrayBig2Small(int[] big, int bigWidth, int[][] small, int startRow, int startCol, int endRow, int endCol) array Big Small

```java title=Example.java
int j = 0;
for (int i = startRow; i <= endRow; i++, j++) {
    System.arraycopy(big, i * bigWidth + startCol, small[j], 0, endCol - startCol + 1);
```

voidarrayCopy(byte[] dest, int offset, byte[] in) array Copy

```java title=Example.java
System.arraycopy(in, 0, dest, offset, in.length);
```

voidarrayCopy(byte[] in, int inOff, int length, byte[] out, int outOff) array Copy

```java title=Example.java
for (int i = inOff; i < inOff + length; i++) {
    out[outOff + i - inOff] = in[i];
```

byte[]arrayCopy(byte[] source, byte[] dest) array Copy

```java title=Example.java
return arrayCopy(source, 0, dest, 0);
```

byte[]arrayCopy(byte[] source, byte[] dest) array Copy

```java title=Example.java
return arrayCopy(source, dest, 0);
```

byte[]arraycopy(byte[] src, int destLen, int len) arraycopy

```java title=Example.java
byte[] dest = newByte(destLen);
System.arraycopy(src, 0, dest, 0, len);
return dest;
```

voidarraycopy(byte[] src, int src_position, byte[] dst, int dst_position, int length) arraycopy

```java title=Example.java
if (src_position < 0)
    thrownewIllegalArgumentException("src_position was less than 0.  Actual value " + src_position);
if (src_position >= src.length)
    thrownewIllegalArgumentException(
            "src_position was greater than src array size.  Tried to write starting at position "
                    + src_position + " but the array length is " + src.length);
if (src_position + length > src.length)
    thrownewIllegalArgumentException(
...
```

byte[]arrayCopy(byte[] src, int srcOffset, byte[] target, int targetOffset, int length) array Copy

```java title=Example.java
System.arraycopy(src, srcOffset, target, targetOffset, length);
return target;
```

voidarrayCopy(byte[] src, int srcStart, byte[] dest, int destStart, int destBitOffset, int lengthInBits) array Copy

```java title=Example.java
int c = 0;
int nBytes = lengthInBits / 8;
int nRestBits = lengthInBits % 8;
for (int i = 0; i < nBytes; i++) {
    c |= ((src[srcStart + i] & 0xff) << destBitOffset);
    dest[destStart + i] |= (byte) (c & 0xff);
    c >>>= 8;
if (nRestBits > 0) {
    c |= ((src[srcStart + nBytes] & (0xff >> (8 - nRestBits))) << destBitOffset);
if ((nRestBits + destBitOffset) > 0) {
    dest[destStart + nBytes] |= c & 0xff;
```

voidarraycopy(char[] A1, int offset1, char[] A2, int offset2, int length) Copies the contents of

```java title=Example.java
A1
```

starting at offset

```java title=Example.java
offset1
```

into

```java title=Example.java
A2
```

starting at offset

```java title=Example.java
offset2
```

for

```java title=Example.java
length
```

elements.

```java title=Example.java
if (offset1 >= 0 && offset2 >= 0 && length >= 0 && length <= A1.length - offset1
        && length <= A2.length - offset2) {
    if (A1 != A2 || offset1 > offset2 || offset1 + length <= offset2) {
        for (int i = 0; i < length; ++i) {
            A2[offset2 + i] = A1[offset1 + i];
    } else {
        for (int i = length - 1; i >= 0; --i) {
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
