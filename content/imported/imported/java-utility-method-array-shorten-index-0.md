---
title: Java Utililty Methods Array Shorten
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Shorten are organized into topic(s).
section: Imported - java2s Archive
order: 50103
source: https://www.java2s.com/example/java-utility-method/array-shorten-index-0.html
---
List of utility methods to do Array Shorten

## Description

The list of methods to do Array Shorten are organized into topic(s).

## Method

short[]toShortArray(byte[] data) to Short Array

```java title=Example.java
if ((data == null) || (data.length % 2 != 0)) {
    return null;
short[] shts = newshort[data.length / 2];
for (int i = 0; i < shts.length; i++) {
    shts[i] = toShort(newbyte[] { data[(i * 2)], data[(i * 2) + 1] });
return shts;
...
```

short[][]toShortArray(double[][] array) to Short Array

```java title=Example.java
int nr = array.length;
int nc = array[0].length;
short[][] ret = newshort[nr][nc];
for (int i = 0; i < nr; i++) {
    for (int j = 0; j < nc; j++) {
        ret[i][j] = (short) array[i][j];
return ret;
```

short[]toShortArray(final byte[] array) to Short Array

```java title=Example.java
return toShortArray(array, 0, array.length);
```

byte[]toShortArray(long value, int length) Converts a long value to a short array. The long value could be positive or negative.

```java title=Example.java
byte[] ret = newbyte[length];
toArray(value, ret, 0, length);
return ret;
```

short[]toShortArray(Number[] array) Turns the Number array into one consisting of primitive shorts.

```java title=Example.java
short[] result;
int i;
result = newshort[array.length];
for (i = 0; i < array.length; i++)
    result[i] = array[i].shortValue();
return result;
```

short[]toShortArray(Object[] array) to Short Array

```java title=Example.java
if (array == null)
    return null;
short[] ret = newshort[array.length];
for (int i = 0; i < array.length; i++)
    ret[i] = parseShort(array[i]);
return ret;
```

short[]toShortArray(String str, String separator) Converts a string of numbers to a short array

```java title=Example.java
String[] fields = str.split(separator);
short[] tmp = newshort[fields.length];
for (int i = 0; i < tmp.length; i++)
    tmp[i] = Short.parseShort(fields[i]);
return tmp;
```

short[]toShortArray(String[] anArray) to Short Array

```java title=Example.java
short[] output = newshort[anArray.length];
for (int index = 0; index < anArray.length; index++)
    output[index] = Short.parseShort(anArray[index]);
return output;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
