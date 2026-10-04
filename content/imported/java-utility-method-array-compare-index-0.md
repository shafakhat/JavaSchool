---
title: Java Utililty Methods Array Compare
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Compare are organized into topic(s).
section: Imported - java2s Archive
order: 50040
source: https://www.java2s.com/example/java-utility-method/array-compare-index-0.html
---
List of utility methods to do Array Compare

## Description

The list of methods to do Array Compare are organized into topic(s).

## Method

booleanareEqual(byte[] a, byte[] b)

Returns true if the two designated byte arrays are (a) non-null, (b) of the same length, and (c) contain the same values.

```java title=Example.java
if (a == null || b == null) {
    return false;
int aLength = a.length;
if (aLength != b.length) {
    return false;
for (int i = 0; i < aLength; i++) {
...
```

booleanareEqual(byte[] a, byte[] b) Compares two byte arrays for equality.

```java title=Example.java
int aLength = a.length;
if (aLength != b.length) {
    return false;
for (int i = 0; i < aLength; i++) {
    if (a[i] != b[i]) {
        return false;
return true;
```

booleanareEqual(byte[] a, byte[] b) Compares two byte arrays for equality.

```java title=Example.java
int aLength = a.length;
if (aLength != b.length)
    return false;
for (int i = 0; i < aLength; i++)
    if (a[i] != b[i])
        return false;
return true;
```

booleanareEqual(byte[] a, byte[] b) are Equal

```java title=Example.java
int aLength = a.length;
if (aLength != b.length)
    return false;
for (int i = 0; i < aLength; i++)
    if (a[i] != b[i])
        return false;
return true;
```

booleanareEqual(byte[] array1, byte[] array2) Determine if the two passed arrays have exactly the same values.

```java title=Example.java
boolean equality;
if (array1.length == array2.length) {
    equality = true;
    for (int loop = 0; equality && loop < array1.length; loop++) {
        if (array1[loop] != array2[loop]) {
            equality = false;
} else {
    equality = false;
return equality;
```

booleanAreEqual(double[] vector1, double[] vector2) Use this method to check that two vectors have are the same, i.e.

```java title=Example.java
try {
    CheckArrays(vector1, vector2);
} catch (IllegalArgumentException ex) {
    return false;
for (int i = 0; i < vector2.length; i++) {
    if (vector1[i] != vector2[i])
        return false;
...
```

booleanareEqual(final byte[] a, final byte[] b) Checks the specified arrays for equality in constant time.

```java title=Example.java
if (a.length != b.length) {
    return false;
int result = 0;
for (int i = 0; i < a.length; i++) {
    result |= a[i] ^ b[i];
return result == 0;
...
```

booleanareEqualBytes(byte[] b1, byte[] b2) are Equal Bytes

```java title=Example.java
if (b1.length != b2.length) {
    return false;
for (int i = 0; i < b1.length; i++) {
    if (b1[i] != b2[i]) {
        return false;
return true;
```

booleanareEqualPropPaths(String[] pp1, String[] pp2) Tests whether two property paths are equal, i.e.

```java title=Example.java
if (pp1 == pp2)
    return true;
if (pp1 == null || pp2 == null || pp1.length != pp2.length)
    return false;
for (int i = pp1.length - 1; i > -1; i--)
    if (pp1[i] == null || !pp1[i].equals(pp2[i]))
        return false;
return true;
...
```

booleanareEquals(byte[] g1, byte[] g2) are Equals

```java title=Example.java
if ((g1 == null && g2 == null) || (g1 == null && g2.length == 0) || (g2 == null && g1.length == 0))
    return true;
boolean b = true;
for (int i = 0; i < g1.length; i++)
    b = b && g1[i] == g2[i];
return b;
```
