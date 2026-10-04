---
title: Java Utililty Methods Array From
nav: Java Utililty Methods Arra...
description: The list of methods to do Array From are organized into topic(s).
section: Imported - java2s Archive
order: 50069
source: https://www.java2s.com/example/java-utility-method/array-from-index-0.html
---
List of utility methods to do Array From

## Description

The list of methods to do Array From are organized into topic(s).

## Method

byte[]arrayFromArrayWithLength(final byte[] array, final int length) array From Array With Length

```java title=Example.java
finalbyte[] output = newbyte[length];
for (int j = 0; j < length; j++) {
    output[j] = array[(j % array.length)];
return output;
```

double[]arrayFromIndex(double[][] values, int index) array From Index

```java title=Example.java
double[] array = newdouble[values.length];
for (int i = 0; i < values.length; i++) {
    array[i] = values[i][index];
return array;
```

String[]arrayFromList(String aList) Function arrayFromList Given a comma seperated list, possibly within brackets this function will return all the comma seperated items as an array from strings

```java title=Example.java
String aS1 = aList.replaceAll("[\\s\"\'\\]\\[]+", "");
String[] aV = aS1.split(",");
return aV;
```

String[]arrayFromString(String fromString) array From String

```java title=Example.java
if (fromString == null) {
    return null;
return fromString.split(";");
```

String[]arrayFromString(String s) array From String

```java title=Example.java
if (s == null)
    returnnewString[] {};
if (!s.startsWith("[") || !s.endsWith("]"))
    thrownewIllegalArgumentException();
if (s.length() == 2)
    returnnewString[] {};
return s.substring(1, s.length() - 1).split(" *, *");
```

String[]arrayFromString(String str) array From String

```java title=Example.java
if ((str != null) && (str.length() > 0)) {
    return str.split("[ ,;]");
} else {
    return null;
```

Boolean[]toArray(boolean[] array) to Array

```java title=Example.java
Boolean[] newArray = newBoolean[array.length];
for (int i = 0; i < array.length; i++) {
    newArray[i] = Boolean.valueOf(array[i]);
return newArray;
```

boolean[]toArray(CharSequence input) Translates a

```java title=Example.java
String
```

of zero ('0') and one ('1') characters to an array of

```java title=Example.java
boolean
```

.

```java title=Example.java
int len = input.length();
boolean[] bools = newboolean[len];
for (int i = 0; i < len; i++) {
    bools[i] = (input.charAt(i) == '1');
return bools;
```

Class[]toArray(Class interfaceClass) to Array

```java title=Example.java
returnnewClass[] { interfaceClass };
```

double[]toArray(Double[] array) to Array

```java title=Example.java
if (array == null) {
    return null;
double[] data = newdouble[array.length];
for (int i = 0; i < array.length; i++) {
    doubleval = (array[i] == null) ? 0 : array[i].intValue();
    data[i] = val;
return data;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
