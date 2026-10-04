---
title: Java Utililty Methods Array Deep to String
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Deep to String are organized into topic(s).
section: Imported - java2s Archive
order: 50051
source: https://www.java2s.com/example/java-utility-method/array-deep-to-string-index-0.html
---
List of utility methods to do Array Deep to String

## Description

The list of methods to do Array Deep to String are organized into topic(s).

## Method

StringdeepToString(double[][] array) deep To String

```java title=Example.java
StringBuilder sb = newStringBuilder();
sb.append("[");
for (double[] arr : array) {
    sb.append("[");
    for (double a : arr) {
        sb.append(String.format("%10.3g, ", a));
    sb.append("], ");
...
```

StringdeepToString(int[] values) Print the contents of an int[].

```java title=Example.java
StringBuilder b = newStringBuilder();
b.append("[");
for (int i = 0; i < values.length; i++) {
    b.append(values[i]);
    b.append(", ");
b.delete(b.length() - 2, b.length() - 1);
b.append("]");
...
```

StringdeepToString(Object[] array) Simple method to walk an array and call

```java title=Example.java
toString()
```

on each of the entries.

```java title=Example.java
StringBuffer buffer = newStringBuffer();
for (int i = 0; i < array.length; i++) {
    buffer.append(array[i].toString());
    if (i < array.length - 1) {
        buffer.append(',');
return buffer.toString();
...
```
