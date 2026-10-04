---
title: Java Utililty Methods Array Split
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Split are organized into topic(s).
section: Imported - java2s Archive
order: 50108
source: https://www.java2s.com/example/java-utility-method/array-split-index-0.html
---
List of utility methods to do Array Split

## Description

The list of methods to do Array Split are organized into topic(s).

## Method

byte[][]split(byte[] array, int index, int len, byte value) split

```java title=Example.java
int maxIndex = index + len;
int start = index;
int end = 0;
byte[][] result = newbyte[10][];
int resultIndex = 0;
int limit = maxIndex - 1;
for (int i = index; i < maxIndex; i++) {
    if (array[i] == value) {
...
```

Listsplit(byte[] pattern, byte[] src) split

```java title=Example.java
List<byte[]> list = newArrayList<>();
int startPos = 0;
for (int i = startPos; i < src.length;) {
    int match = firstMatch(pattern, src, i);
    if (match < 0) {
        list.add(Arrays.copyOfRange(src, startPos, src.length));
        break;
    } else {
...
```

byte[][]split(byte[] source, int c) split

```java title=Example.java
if (source == null || source.length == 0) {
    returnnewbyte[][] {};
List<byte[]> bytes = newArrayList<byte[]>();
int offset = 0;
for (int i = 0; i <= source.length; i++) {
    if (i == source.length) {
        bytes.add(Arrays.copyOfRange(source, offset, i));
...
```

C[]split(Collection collection, C[] array, int pageSize) split

```java title=Example.java
try {
    int size = (int) Math.ceil((collection.size() / (double) pageSize));
    Object[] toReturn = newObject[size];
    int index = 0;
    C currentCollection = (C) array.getClass().getComponentType().newInstance();
    int count = 0;
    for (T obj : collection) {
        currentCollection.add(obj);
...
```

int[][]split(final int[] array) Splits array into two smaller arrays.

```java title=Example.java
finalint[] part1 = Arrays.copyOfRange(array, 0, array.length / 2);
finalint[] part2 = Arrays.copyOfRange(array, array.length / 2, array.length);
return twoDimensionalArray(part1, part2);
```

byte[][]split(int splitBefore, byte[] source) split

```java title=Example.java
if (source.length <= splitBefore)
    thrownewRuntimeException("cannot split the bypassed array (array too small: " + source.length + "<="
            + splitBefore + ")");
byte[][] result = newbyte[2][];
result[0] = Arrays.copyOfRange(source, 0, splitBefore);
result[1] = Arrays.copyOfRange(source, splitBefore, source.length);
return result;
```

intsplit(String string, String delim, String[] a) split

```java title=Example.java
if (a.length == 0) {
    thrownewIllegalArgumentException();
int idx = 0;
for (String s : split(string, delim)) {
    a[idx++] = s;
return idx;
...
```

ListsplitAndPad(byte[] byteArray, int blocksize) Splits the given array into blocks of given size and adds padding to the last one, if necessary.

```java title=Example.java
List<byte[]> blocks = newArrayList<byte[]>();
int numBlocks = (int) Math.ceil(byteArray.length / (double) blocksize);
for (int i = 0; i < numBlocks; i++) {
    byte[] block = newbyte[blocksize];
    Arrays.fill(block, (byte) 0x00);
    if (i + 1 == numBlocks) {
        int remainingBytes = byteArray.length - (i * blocksize);
        System.arraycopy(byteArray, i * blocksize, block, 0, remainingBytes);
...
```

byte[][]splitArray(byte[] src, int size) Splits an array into more chunks with the specified maximum size for each array chunk.

```java title=Example.java
int index = 0;
ArrayList<byte[]> split = newArrayList<byte[]>();
while (index < src.length) {
    if (index + size <= src.length) {
        split.add(Arrays.copyOfRange(src, index, index + size));
        index += size;
    } else {
        split.add(Arrays.copyOfRange(src, index, src.length));
...
```

ListsplitArray(int[] array, int limit) split Array

```java title=Example.java
List<int[]> list = newArrayList<>();
if (array.length <= limit) {
    list.add(array);
    return list;
int count = getSplitCount(array.length, limit);
int copied = 0;
for (int i = 0; i < count; i++) {
...
```
