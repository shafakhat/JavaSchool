---
title: Java Utililty Methods Array Deep Equal
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Deep Equal are organized into topic(s).
section: Imported - java2s Archive
order: 50049
source: https://www.java2s.com/example/java-utility-method/array-deep-equal-index-0.html
---
List of utility methods to do Array Deep Equal

## Description

The list of methods to do Array Deep Equal are organized into topic(s).

## Method

booleandeepEquals(boolean[] array1, boolean[] array2) Compares the two boolean arrays deeply

```java title=Example.java
if (array1.length != array2.length)
    return false;
for (int i = 0; i < array1.length; i++) {
    if (!(array1[i] == array2[i]))
        return false;
return true;
```

booleandeepEquals(Object[] a1, Object[] a2) Returns true if the two specified arrays are deeply equal to one another.

```java title=Example.java
if (a1 == a2)
    return true;
if (a1 == null || a2 == null)
    return false;
int length = a1.length;
if (a2.length != length)
    return false;
for (int i = 0; i < length; i++) {
...
```

booleandeepEquals(Object[] a1, Object[] a2) Copied from

```java title=Example.java
Arrays.deepEquals
```

.

```java title=Example.java
if (a1 == a2) {
    return true;
if (a1 == null || a2 == null) {
    return false;
int length = a1.length;
if (a2.length != length) {
...
```

booleandeepEquals(Object[] a1, Object[] a2) deep Equals

```java title=Example.java
if (a1 == a2)
    return true;
if (a1 == null || a2 == null)
    return false;
int len = a1.length;
if (len != a2.length)
    return false;
for (int i = 0; i < len; i++) {
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
