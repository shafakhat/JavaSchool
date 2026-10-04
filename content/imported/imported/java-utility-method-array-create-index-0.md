---
title: Java Utililty Methods Array Create
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Create are organized into topic(s).
section: Imported - java2s Archive
order: 50046
source: https://www.java2s.com/example/java-utility-method/array-create-index-0.html
---
List of utility methods to do Array Create

## Description

The list of methods to do Array Create are organized into topic(s).

## Method

CharSequencearray(CharSequence... args) array

```java title=Example.java
StringBuilder array = newStringBuilder();
array.append('[');
if (args.length > 0) {
    array.append(args[0]);
    for (int i = 1; i < args.length; i++) {
        array.append(", ").append(args[i]);
array.append(']');
return array.toString();
```

T[]array(final T... array) Creates an array from the given objects.

```java title=Example.java
return array;
```

T[]array(final T... elements) Shortcut to create an array of objects.

```java title=Example.java
return elements;
```

byte[]array(int... rest) array

```java title=Example.java
int len = rest.length;
byte bs[] = newbyte[len];
for (int i = 0; i < len; ++i) {
    bs[i] = (byte) rest[i];
return bs;
```

byte[]array(int... values) Helper fonction for building bytes array.

```java title=Example.java
byte[] array = newbyte[values.length];
for (int i = 0; i < array.length; i++) {
    array[i] = (byte) values[i];
return array;
```

Stringarray(int[] array, int index) array

```java title=Example.java
if ((array == null) || (index >= array.length) || (index < 0)) {
    return EMPTY;
return (array[index] != 0) ? CHECKED : EMPTY;
```

T[]array(Object... objects) array

```java title=Example.java
return as(objects);
```

Object[]array(Object... val) array

```java title=Example.java
returnval;
```

String[]array(String str) array

```java title=Example.java
returnnewString[] { str };
```

String[]array(String... strings) Returns an array of strings from the supplied var-args.

```java title=Example.java
if (strings == null)
    returnnewString[0];
String[] ret = newString[strings.length];
for (int i = 0; i < strings.length; ret[i] = strings[i], i++)
    ;
return ret;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
