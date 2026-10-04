---
title: Java Utililty Methods Array Delete
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Delete are organized into topic(s).
section: Imported - java2s Archive
order: 50052
source: https://www.java2s.com/example/java-utility-method/array-delete-index-0.html
---
List of utility methods to do Array Delete

## Description

The list of methods to do Array Delete are organized into topic(s).

## Method

byte[]arrayDelete(byte[] array, int length) array Delete

```java title=Example.java
byte[] newArray = newbyte[array.length - length];
System.arraycopy(array, length, newArray, 0, array.length - length);
return newArray;
```

int[]arrayDelete(final int[] arr, final int ind) array Delete

```java title=Example.java
int[] narr = newint[arr.length - 1];
int offs = 0;
for (int i = 0; i < arr.length; i++) {
    if (i == ind) {
        offs = 1;
        continue;
    narr[i - offs] = arr[i];
...
```
