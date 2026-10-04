---
title: Java Utililty Methods Array Index Of
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Index Of are organized into topic(s).
section: Imported - java2s Archive
order: 50073
source: https://www.java2s.com/example/java-utility-method/array-index-of-index-0.html
---
List of utility methods to do Array Index Of

## Description

The list of methods to do Array Index Of are organized into topic(s).

## Method

intarrayIndex(T[] arr, T item) array Index

```java title=Example.java
if (arr == null) {
    return -1;
for (int i = 0; i < arr.length; i++) {
    if (arr[i].equals(item)) {
        return i;
return -1;
```

voidarrayIndexCheck(char[] text, int startPos, int endPos) array Index Check

```java title=Example.java
if (text == null || startPos < 0 || startPos > endPos) {
    thrownewArrayIndexOutOfBoundsException("text.length: " + (text == null ? 0 : text.length)
            + ", startPos: " + startPos + ", endPos: " + endPos);
```

StringarrayIndexClean(String indx) array Index Clean

```java title=Example.java
if (indx.length() >= 2 && indx.charAt(0) == '\"' && indx.charAt(indx.length() - 1) == '\"')
    return indx.substring(1, indx.length() - 1);
elsereturn"#" + indx + "#";
```

intarrayIndexFor(final String raw) DOCUMENT ME!

```java title=Example.java
if (raw.isEmpty()) {
    return -1;
if (raw.charAt(0) == '0') {
    return (raw.length() == 1) ? 0 : -1;
try {
    returnInteger.parseInt(raw);
...
```

intArrayIndexOf(byte[] data, byte[] dest) Array Index Of

```java title=Example.java
return ArrayIndexOf(data, dest, 0);
```

intarrayIndexOf(int needle, int[] haystack) Sequentially search through an array, return the index of first needle element in haystack or -1, if not found.

```java title=Example.java
for (int i = 0; i < haystack.length; i++) {
    if (haystack[i] == needle) {
        return i;
return -1;
```

intarrayIndexOf(int value, int[] arr) array Index Of

```java title=Example.java
for (int i = 0; i < arr.length; i++) {
    if (arr[i] == value)
        return i;
return -1;
```

intarrayIndexOf(Object[] array, Object element) array Index Of

```java title=Example.java
for (int i = 0; i < array.length; i++) {
    if (element.equals(array[i])) {
        return i;
return -1;
```

longarrayIndexOffset(int index, long baseOffset, long indexScale) array Index Offset

```java title=Example.java
if (index < 0)
    thrownewIndexOutOfBoundsException("index " + index);
return baseOffset + (long) index * indexScale;
```

intindexOf(byte[] array, byte[] target, int fromIndex) Returns the index (start position) of the first occurrence of the specified target within array starting at fromIndex , or -1 if there is no such occurrence.

```java title=Example.java
if (array == null || target == null) {
    return -1;
if (fromIndex < 0 || (fromIndex > (array.length - target.length))) {
    return -1;
if (target.length == 0) {
    return fromIndex;
...
```
