---
title: Java Utililty Methods Array Dump
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Dump are organized into topic(s).
section: Imported - java2s Archive
order: 50059
source: https://www.java2s.com/example/java-utility-method/array-dump-index-0.html
---
List of utility methods to do Array Dump

## Description

The list of methods to do Array Dump are organized into topic(s).

## Method

voiddump(double[][] a) dump

```java title=Example.java
for (int i = 0; i < a.length; i++)
    dump(a[i]);
System.out.println();
```

StringBuilderdump(final StringBuilder buffer, final byte[] data, final int offset, final int length) dump

```java title=Example.java
for (int i = 0; i < length; i++) {
    if (i % 16 == 0)
        buffer.append("\n");
    buffer.append(String.format("%02x "));
return buffer;
```

voiddump(String name, byte[] in) dump

```java title=Example.java
int x = 0, bar_length = ((64 - name.length()) / 2);
String bar_left, bar = "";
for (int y = 0; y < bar_length; ++y)
    bar += "-";
bar_left = bar;
if (bar_length % 64 != 0)
    bar_left += "-";
System.out.print("+" + bar_left + name + bar + "+\n|");
...
```

voiddump(String t, String[] arr) dump

```java title=Example.java
System.out.println("--------" + t + "-------------");
for (int i = 0; i < arr.length; i++) {
    System.out.println("#" + i + "='" + arr[i] + "'");
```

voiddump(T[] from, T[] to) Replaces all the data in to with from without making modifications to the array being dumped.

```java title=Example.java
if (from.length != to.length)
    thrownewIllegalArgumentException("Arrays must be equal in size!");
for (int i = 0; i < from.length; i++)
    to[i] = from[i];
```

Stringdump_octets(byte[] oct) dumoctets

```java title=Example.java
StringBuilder sb = newStringBuilder();
dump_octets(oct, 0, oct.length, sb);
return sb.toString();
```

voiddump_strarr(String[] arr, String doc) dumstrarr

```java title=Example.java
System.out.println(doc);
for (int i = 0; i < arr.length; i++) {
    System.out.println("(" + i + ") " + arr[i]);
```

voiddumpArray(final float[] array, final int maxElemsPerLine) Dumps the contents of the given array to stdout.

```java title=Example.java
if (array == null) {
    System.out.println((String) null);
    return;
int line = 0;
System.out.print("[ ");
for (int i = 0; i < array.length; i++) {
    if ((i > 0) && ((i % maxElemsPerLine) == 0)) {
...
```

StringdumpArray(String msg, float[][] A, int x1, int x2, int y1, int y2) dump Array

```java title=Example.java
String s = "dumpArray: " + msg + "\n";
for (int x = x1; x <= x2; x++)
    s += "\t*" + x + "*";
for (int y = y2; y >= y1; y--) {
    s += "\n*" + y + "*";
    for (int x = x1; x <= x2; x++)
        s += "\t" + (x < A.length && y < A[x].length ? A[x][y] : Float.NaN);
return s;
```

voiddumpArray(String msg, Object[] refs) dump Array

```java title=Example.java
System.out.println("DUMPING array: " + msg);
if (refs == null) {
    System.out.println("null");
    return;
for (int i = 0; i < refs.length; i++)
    System.out.println(refs[i].toString());
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
