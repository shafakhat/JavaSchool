---
title: Java Utililty Methods Array Contain
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Contain are organized into topic(s).
section: Imported - java2s Archive
order: 50042
source: https://www.java2s.com/example/java-utility-method/array-contain-index-0.html
---
List of utility methods to do Array Contain

## Description

The list of methods to do Array Contain are organized into topic(s).

## Method

booleanARRAY_Contains(int value, int[] array) returns true if the array contains the value, or false if it does not

```java title=Example.java
for (int x = 0; x < array.length; x++) {
    if (array[x] == value)
        return true;
return false;
```

booleanarrayContains(byte[] a, int offset, byte[] b) Returns true if an array's elements appear inside another array.

```java title=Example.java
if (a.length < offset + b.length)
    return false;
for (int i = 0; i < b.length; i++) {
    if (a[offset + i] != b[i])
        return false;
return true;
```

booleanarrayContains(char[] chars, char cToFind) array Contains

```java title=Example.java
for (char c : chars) {
    if (c == cToFind) {
        return true;
return false;
```

booleanarrayContains(char[] chars, char cToFind) array Contains

```java title=Example.java
for (char c : chars) {
    if (c == cToFind) {
        return true;
return false;
```

booleanarrayContains(final byte[] what, final byte[] b) array Contains

```java title=Example.java
boolean r = false;
for (int i = b.length - 1; i > what.length; i--) {
    int j = what.length;
    while (j > -1) {
        if (b[i] != what[j]) {
            r = false;
            continue;
        } else {
...
```

booleanarrayContains(final E[] arr, final E targetValue) Check if an array contains a value, very efficient

```java title=Example.java
for (final E s : arr) {
    if (s.equals(targetValue))
        return true;
return false;
```

booleanarrayContains(final int[] array, final int v) Determines if a value exists in an array.

```java title=Example.java
for (int i : array)
    if (i == v)
        return true;
return false;
```

booleanarrayContains(final Object[] a, final Object v) array Contains

```java title=Example.java
for (finalObject x : a) {
    if (v == null) {
        if (x == null)
            return true;
    } else {
        if (v.equals(x))
            return true;
return false;
```

booleanarrayContains(final String[] array, String needle) Returns true if the String array contains a string.

```java title=Example.java
needle = nn(needle);
for (finalString element : array) {
    if (needle.equalsIgnoreCase(element.trim())) {
        return true;
return false;
```

booleanarrayContains(final T[] array, final T v) array Contains

```java title=Example.java
for (final T e : array)
    if (e == v || v.equals(e))
        return true;
return false;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
