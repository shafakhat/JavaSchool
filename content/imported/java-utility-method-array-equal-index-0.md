---
title: Java Utililty Methods Array Equal
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Equal are organized into topic(s).
section: Imported - java2s Archive
order: 50063
source: https://www.java2s.com/example/java-utility-method/array-equal-index-0.html
---
List of utility methods to do Array Equal

## Description

The list of methods to do Array Equal are organized into topic(s).

## Method

booleanallEqual(int[] arr) Returns true if all values in the array are equal.

```java title=Example.java
for (int i = 0; i < arr.length; i++) {
    if (arr[0] != arr[i])
        return false;
return true;
```

booleanallEqual(int[] values) Checks if elements in the given array are all equal.

```java title=Example.java
if (values.length == 0) {
    return true;
int value = values[0];
for (int i = 1; i < values.length; i++) {
    if (values[i] != value) {
        return false;
return true;
```

booleanallEquals(double[][] sims) all Equals

```java title=Example.java
double prev = 0;
for (int i = 0; i < sims.length; i++) {
    for (int j = 0; j < sims[0].length; j++) {
        if (!(i == 0 && j == 0))
            if (sims[i][j] != prev)
                return false;
        prev = sims[i][j];
return true;
```

booleanallEquals(final String value, final String... strings) Return true if all strings are the same.

```java title=Example.java
for (finalString s : strings) {
    if (s == null && value != null || s != null && value != null && !s.equals(value)) {
        return false;
return true;
```

booleanallEquals(int needle, byte... bytes) all Equals

```java title=Example.java
int i = 0;
while (i < bytes.length && bytes[i] == needle)
    i++;
return i == bytes.length;
```

booleanallEquals(int y, int y2, int y3) all Equals

```java title=Example.java
if ((y == y2) && (y2 == y3)) {
    return true;
return false;
```

booleanareEqualArrays(Object[] a1, Object[] a2) are Equal Arrays

```java title=Example.java
returnArrays.equals(a1, a2);
```

booleanarrayEq(byte[] a, byte[] b) array Eq

```java title=Example.java
if (a.length != b.length) {
    return false;
for (int i = 0; i < a.length; i++) {
    if (a[i] != b[i])
        return false;
return true;
...
```

booleanarrayEqual(char[] a, char[] b, int aStart, int bStart, int length) array Equal

```java title=Example.java
for (int i = 0; i < length; i++) {
    if (a[aStart + i] != b[bStart + i]) {
        return false;
return true;
```

booleanarrayEquals(byte[] data, byte[] expected) array Equals

```java title=Example.java
if (data.length != expected.length)
    return false;
for (int i = 0; i < data.length; i++) {
    if (data[i] != expected[i])
        return false;
return true;
```
