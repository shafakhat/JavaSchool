---
title: Java Utililty Methods Array to Collection
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to Collection are organized into topic(s).
section: Imported - java2s Archive
order: 50117
source: https://www.java2s.com/example/java-utility-method/array-to-collection-index-0.html
---
List of utility methods to do Array to Collection

## Description

The list of methods to do Array to Collection are organized into topic(s).

## Method

CollectionarrayToCollection(Collection collection, T[] elements) array To Collection

```java title=Example.java
for (T element : elements) {
    collection.add(element);
return collection;
```

CarrayToCollection(E[] array, C collection) Constructs a new java.util.Collection that will contain the given array elements.

```java title=Example.java
collection.clear();
for (E e : array) {
    collection.add(e);
return collection;
```

ListarrayToCollection(Object[] objs) array To Collection

```java title=Example.java
returnnewArrayList(Arrays.asList(objs));
```

ListarrayToCollection(String[] values) array To Collection

```java title=Example.java
List<String> list = newArrayList<String>(values.length);
Collections.addAll(list, values);
return list;
```
