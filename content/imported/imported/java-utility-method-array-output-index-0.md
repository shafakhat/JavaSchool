---
title: Java Utililty Methods Array Output
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Output are organized into topic(s).
section: Imported - java2s Archive
order: 50090
source: https://www.java2s.com/example/java-utility-method/array-output-index-0.html
---
List of utility methods to do Array Output

## Description

The list of methods to do Array Output are organized into topic(s).

## Method

voidprintArray(char[] array) print Array

```java title=Example.java
StringBuilder buf = newStringBuilder();
for (int i = 0; i < array.length; ++i) {
    if (i == 0) {
        buf.append("[");
        buf.append("'").append(array[i]).append("'");
    } else {
        buf.append(",");
        buf.append("'").append(array[i]).append("'");
...
```

voidprintArray(double[] array) print Array

```java title=Example.java
System.out.print("Double Array: [");
for (int i = 0; i < array.length; i++) {
    System.out.print(array[i]);
    if (i != array.length - 1) {
        System.out.print(", ");
System.out.println("]");
...
```

voidprintArray(double[] array, String msgBefore, String msgAfter) print Array

```java title=Example.java
System.out.print(msgBefore);
System.out.print(arrayToString(array));
System.out.print(msgAfter);
```

StringprintArray(double[][] in) print Array

```java title=Example.java
if (in == null)
    return"null";
String out = "";
for (int i = 0; i < in.length; i++) {
    for (int j = 0; j < in[0].length; j++) {
        out += in[i][j] + " ";
    out += "\n";
...
```

StringprintArray(double[][] in) print Array

```java title=Example.java
if (in == null)
    return"null";
String out = "";
for (int i = 0; i < in.length; i++) {
    for (int j = 0; j < in[0].length; j++) {
        out += in[i][j] + " ";
    out += "\n";
...
```

voidprintarray(final int[] a) printarray

```java title=Example.java
StringBuilder s = newStringBuilder();
for (int i : a) {
    s.append(i);
    s.append(", ");
if (s.length() >= 1) {
    s.deleteCharAt(s.length() - 1);
s.append("\n");
System.err.print(s.toString());
```

voidprintArray(final Object[] array, int indent) utility method, prints out an array using the toString() method of the members.

```java title=Example.java
System.out.println(toString(array, indent, false, true));
```

voidprintArray(float[] arr) Prints out the array to standard output.

```java title=Example.java
if (arr == null) {
    System.out.println("Null array.");
    return;
for (int i = 0; i < arr.length - 1; i++) {
    System.out.print(arr[i] + " ");
System.out.print(arr[arr.length - 1]);
...
```

StringprintArray(int arr[]) print Array

```java title=Example.java
String ret = "[ ";
for (int i = 0; i < arr.length; i++) {
    ret += arr[i] + ", ";
return ret.substring(0, ret.length() - 2) + " ]";
```

voidprintArray(int[] arr) print Array

```java title=Example.java
printArray(arr, "\t");
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
