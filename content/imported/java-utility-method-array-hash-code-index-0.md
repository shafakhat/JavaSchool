---
title: Java Utililty Methods Array Hash Code
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Hash Code are organized into topic(s).
section: Imported - java2s Archive
order: 50071
source: https://www.java2s.com/example/java-utility-method/array-hash-code-index-0.html
---
List of utility methods to do Array Hash Code

## Description

The list of methods to do Array Hash Code are organized into topic(s).

## Method

intarrayHashCode(Object array[]) Calling hashCode on an array does not go into the items in the array, as would be done for a List.

```java title=Example.java
int result = 0;
if (array != null) {
    for (int i = 0; i < array.length; i++) {
        Object obj = array[i];
        result += obj.hashCode();
return result;
...
```

intarrayHashCode(Object[] arr) array Hash Code

```java title=Example.java
int hash = 0;
if (arr != null) {
    hash ^= arr.getClass().hashCode();
    for (int i = 0; i < arr.length; ++i) {
        hash ^= arr[i] == null ? 0 : arr[i].hashCode();
return hash;
...
```

intarrayHashCode(Object[] arr) Compute hash code of array.

```java title=Example.java
int c = 0;
int len = arr.length;
for (int i = 0; i < len; i++) {
    Object o = arr[i];
    int v = o == null ? 1 : o.hashCode();
    c += (v ^ i);
return c;
...
```

intarrayHashCode(Object[] objects) array Hash Code

```java title=Example.java
int hc = 0;
if (objects != null) {
    for (int i = 0; i < objects.length; i++) {
        hc += (objects[i] != null ? (objects[i].hashCode() * 31) : 0);
return hc;
```

intbyteArrayHashCode(final byte[] array) Obtain the hashcode of a byte array.

```java title=Example.java
returnArrays.hashCode(array);
```

intcalculateHash(byte[] data) calculate Hash

```java title=Example.java
returnArrays.hashCode(data);
```

intdeepHash(Object[] t) deep Hash

```java title=Example.java
returnArrays.deepHashCode(t);
```

intdeepHashCode(double[][] matrix) Computes hashCode of a given matrix

```java title=Example.java
int retVal = 0;
for (int i = 0; i < matrix.length; i++) {
    retVal += Arrays.hashCode(matrix[i]);
return retVal;
```

inthashCode(byte[] bytes) This function calculates a hash code for the specified byte array.

```java title=Example.java
int hash = Arrays.hashCode(bytes);
return hash;
```

inthashCode(byte[] obj) hash Code

```java title=Example.java
if (obj == null)
    return 0;
returnArrays.hashCode(obj);
```
