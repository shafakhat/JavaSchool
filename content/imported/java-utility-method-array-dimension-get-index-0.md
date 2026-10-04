---
title: Java Utililty Methods Array Dimension Get
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Dimension Get are organized into topic(s).
section: Imported - java2s Archive
order: 50055
source: https://www.java2s.com/example/java-utility-method/array-dimension-get-index-0.html
---
List of utility methods to do Array Dimension Get

## Description

The list of methods to do Array Dimension Get are organized into topic(s).

## Method

intarrayDim(Class c) array Dim

```java title=Example.java
if (c.isArray() && !c.getComponentType().isArray())
    return 1;
elsereturn 1 + arrayDim(c.getComponentType());
```

intarrayDimension(String clsName) Computes the dimension of the array class specified by name.

```java title=Example.java
int arrayDim = 0;
if (clsName.startsWith("[")) {
    for (int i = 0; i < clsName.length(); i++) {
        if (clsName.charAt(i) != '[') {
            break;
        arrayDim = i + 1;
return arrayDim;
```

intarrayDimensions(Class arrayClass) Get the dimension of an array

```java title=Example.java
verifyIsArray(arrayClass);
return arrayClass.getName().lastIndexOf("[") + 1;
```

intarrayDimensions(Class c) Return the number of array dimensions represented by the given class.

```java title=Example.java
Class<?> rest = c;
int result = 0;
while (rest.isArray()) {
    rest = rest.getComponentType();
    result++;
return result;
```

int[]arraysDims(String[] arr) arrays Dims

```java title=Example.java
if (arr.length > 1) {
    int[] idx = newint[arr.length - 1];
    for (int i = 1; i < arr.length; i++) {
        idx[i - 1] = Integer.parseInt(arr[i]);
    return idx;
return null;
...
```
