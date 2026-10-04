---
title: Java Utililty Methods Array Flatten
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Flatten are organized into topic(s).
section: Imported - java2s Archive
order: 50067
source: https://www.java2s.com/example/java-utility-method/array-flatten-index-0.html
---
List of utility methods to do Array Flatten

## Description

The list of methods to do Array Flatten are organized into topic(s).

## Method

byte[]flatten(byte[][] first) flatten

```java title=Example.java
byte[] result = null;
for (byte[] curr : first) {
    result = concat(result, curr);
return result;
```

ArrayListflatten(E[][] a) flatten

```java title=Example.java
ArrayList<E> res = newArrayList<E>();
for (int i = 0; i < a.length; i++) {
    for (int j = 0; j < a[i].length; j++) {
        res.add(a[i][j]);
return res;
```

Stringflatten(final Object[] array) Flattens the elements of the provided array into a single string, separating elements by a space character.

```java title=Example.java
return flatten(array, SEPARATOR);
```

float[]flatten(float[][] mat) flatten

```java title=Example.java
float[] result = newfloat[mat.length * mat[0].length];
for (int i = 0; i < mat.length; ++i) {
    System.arraycopy(mat[i], 0, result, i * mat[0].length, mat[i].length);
return result;
```

Object[]flatten(Object[] array) Transform a multidimensional array into a one-dimensional list.

```java title=Example.java
finalList<Object> list = newArrayList<Object>();
if (array != null) {
    for (Object o : array) {
        if (o instanceofObject[]) {
            for (Object oR : flatten((Object[]) o)) {
                list.add(oR);
        } else {
...
```

Object[]flatten(Object[] array) flatten

```java title=Example.java
ArrayList result = newArrayList();
for (int i = 0; i < array.length; i++) {
    if (Object[].class.isAssignableFrom(array[i].getClass())) {
        appendArrayToList((Object[]) array[i], result);
    } else {
        result.add(array[i]);
return result.toArray();
```

Stringflatten(Object[] lines, String sep) Flattens the array into a single, long string.

```java title=Example.java
StringBuilder result;
int i;
result = newStringBuilder();
for (i = 0; i < lines.length; i++) {
    if (i > 0)
        result.append(sep);
    result.append(lines[i].toString());
return result.toString();
```

Stringflatten(String s[]) Shorthand for #flatten(String[],String) invoked with a

```java title=Example.java
" "
```

separator.

```java title=Example.java
return flatten(s, " ");
```

Stringflatten(String[] strings, String separator) Flattens an array of strings (with separator)

```java title=Example.java
StringBuilder sb = newStringBuilder();
boolean any = false;
for (String s : strings) {
    if (any) {
        sb.append(separator);
    any = true;
    sb.append(s);
...
```

StringflattenArguments(String[] arguments) This method flattens an array of arguments to a string.

```java title=Example.java
StringBuffer buf = newStringBuffer();
for (int i = 0; i < arguments.length; i++) {
    if (i > 0)
        buf.append(' ');
    boolean whitespace = false;
    char[] chars = arguments[i].toCharArray();
    for (int j = 0; !whitespace && j < chars.length; j++) {
        if (Character.isWhitespace(chars[j])) {
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
