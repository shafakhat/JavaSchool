---
title: Java Utililty Methods Array to Iterable
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to Iterable are organized into topic(s).
section: Imported - java2s Archive
order: 50121
source: https://www.java2s.com/example/java-utility-method/array-to-iterable-index-0.html
---
List of utility methods to do Array to Iterable

## Description

The list of methods to do Array to Iterable are organized into topic(s).

## Method

IterabletoIterable(final boolean[] values) Converts an array of

```java title=Example.java
boolean
```

values into an

```java title=Example.java
Iterable
```

of

```java title=Example.java
Boolean
```

objects.

```java title=Example.java
returnnewIterable<Boolean>() {
    @OverridepublicIterator<Boolean> iterator() {
        returnnewIterator<Boolean>() {
            privateint pos = 0;
            @Overridepublicboolean hasNext() {
                return pos < values.length;
...
```

IterabletoIterable(final T[] arr) to Iterable

```java title=Example.java
returnnewIterable<T>() {
    @OverridepublicIterator<T> iterator() {
        returnnewIterator<T>() {
            int index = 0;
            @Overridepublicboolean hasNext() {
                return index < arr.length;
...
```

IterabletoIterable(final T[] array) to Iterable

```java title=Example.java
returnnewIterable<T>() {
    @OverridepublicIterator<T> iterator() {
        returnnewIterator<T>() {
            privateint i;
            @Overridepublicboolean hasNext() {
                return i < array.length;
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
