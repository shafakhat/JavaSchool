---
title: Java Utililty Methods Array Null Element
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Null Element are organized into topic(s).
section: Imported - java2s Archive
order: 50088
source: https://www.java2s.com/example/java-utility-method/array-null-element-index-0.html
---
List of utility methods to do Array Null Element

## Description

The list of methods to do Array Null Element are organized into topic(s).

## Method

booleanisNull(final Object[] array) Checks if an array is null or empty or all its elements are null.

```java title=Example.java
if (array == null || array.length == 0) {
    return true;
for (int i = 0; i < array.length; i++) {
    if (array[i] != null) {
        return false;
return true;
```

booleanisNull(Object[] objects) is Null

```java title=Example.java
if (objects != null && objects.length > 0) {
    for (Object object : objects) {
        if (object instanceofString) {
            if ((String) object == null || "".equals((String) object)
                    || "NULL".equals(((String) object).toUpperCase())) {
                return true;
        } elseif (object instanceofInteger) {
...
```

booleanisNull(T array[]) Array is empty

```java title=Example.java
return array == null || array.length == 0;
```

booleanisNullArray(String[] array) is Null Array

```java title=Example.java
return (array == null || array.length == 0 || (array.length == 1 && "".equals(array[0])));
```
