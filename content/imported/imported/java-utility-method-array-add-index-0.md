---
title: Java Utililty Methods Array Add
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Add are organized into topic(s).
section: Imported - java2s Archive
order: 50029
source: https://www.java2s.com/example/java-utility-method/array-add-index-0.html
---
List of utility methods to do Array Add

## Description

The list of methods to do Array Add are organized into topic(s).

## Method

double[]addArray(double[] array1, double[] array2) add Array

```java title=Example.java
if (array1.length != array2.length) {
    thrownewIllegalArgumentException("The dimensions have to be equal!");
double[] result = newdouble[array1.length];
assert array1.length == array2.length;
for (int i = 0; i < array1.length; i++) {
    result[i] = array1[i] + array2[i];
return result;
```

int[]addArray(int[] a, int p) Add element to the end of the array

```java title=Example.java
int[] b = newint[a.length + 1];
System.arraycopy(a, 0, b, 0, a.length);
b[a.length] = p;
return b;
```

int[]addArray(int[] a, int[] b) add Array

```java title=Example.java
int[] result = null;
if (a != null && b != null) {
    result = newint[a.length + b.length];
    System.arraycopy(a, 0, result, 0, a.length);
    System.arraycopy(b, 0, result, a.length, b.length);
} else {
    if (b != null)
        return b;
...
```

Object[]addArray(Object[] Old, Object[] New) add Array

```java title=Example.java
Object[] result = newObject[Old.length + New.length];
for (int zahl = 0; zahl < result.length; zahl++)
    if (zahl < Old.length)
        result[zahl] = Old[zahl];
    else
        result[zahl] = New[zahl - Old.length];
return result;
```

Object[][]addArray(Object[][] first, Object[][]... more) add Array

```java title=Example.java
int len = first.length;
for (int i = 0; i < more.length; i++) {
    Object[][] next = more[i];
    len += next.length;
Object[][] result = newObject[len][];
int count = 0;
for (int i = 0; i < first.length; i++) {
...
```

voidaddArray(StringBuffer RCode, String name, T[] array, boolean useEquals, boolean isString) add Array

```java title=Example.java
if (useEquals) {
    RCode.append(name).append("=").append("c(");
} else {
    RCode.append(name).append("<-").append("c(");
for (int i = 0; i < array.length; i++) {
    if (isString) {
        RCode.append("\"").append(array[i]).append("\"");
...
```

byte[]addArrayAll(byte[] array1, byte[] array2) add Array All

```java title=Example.java
if (array1 == null)
    return clone(array2);
if (array2 == null) {
    return clone(array1);
byte[] joinedArray = newbyte[array1.length + array2.length];
System.arraycopy(array1, 0, joinedArray, 0, array1.length);
System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);
...
```

byte[]addArrayElements(byte[] toArray, byte[] fromArray) adds the elements of the fromArray to the toArray.

```java title=Example.java
byte[] newToArray = newbyte[toArray.length + fromArray.length];
System.arraycopy(toArray, 0, newToArray, 0, toArray.length);
System.arraycopy(fromArray, 0, newToArray, toArray.length, fromArray.length);
return newToArray;
```

int[]addArrays(final int[] a, final int[] b) Adds two arrays together and returns a new array with the sum.

```java title=Example.java
int[] c = newint[a.length];
for (int i = 0; i < a.length; i++)
    c[i] = a[i] + b[i];
return c;
```

float[]addArrays(float[] arr1, float[] arr2, float[] arr3) add Arrays

```java title=Example.java
int l = arr1.length;
float[] res = newfloat[l];
for (int i = 0; i < l; i++) {
    res[i] = arr1[i] + arr2[i] + arr3[i];
return res;
```
