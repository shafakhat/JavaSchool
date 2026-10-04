---
title: Java Utililty Methods Array to ArrayList
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to ArrayList are organized into topic(s).
section: Imported - java2s Archive
order: 50116
source: https://www.java2s.com/example/java-utility-method/array-to-arraylist-index-0.html
---
List of utility methods to do Array to ArrayList

## Description

The list of methods to do Array to ArrayList are organized into topic(s).

## Method

ArrayListarrayToArrayList(Object aobj[]) array To Array List

```java title=Example.java
ArrayList<Object> arraylist = newArrayList<Object>();
if (aobj != null && aobj.length > 0) {
    for (int i = 0; i < aobj.length; i++)
        arraylist.add(aobj[i]);
return arraylist;
```

ArrayListarrayToArrayList(Object[] array) Convert array into list

```java title=Example.java
ArrayList list = newArrayList();
if (array != null)
    for (int i = 0; i < array.length; i++)
        list.add(array[i]);
return list;
```

ArrayListarrayToArrayList(Object[] myArray) This method converts an array into an ArrayList.

```java title=Example.java
int i = 0;
ArrayList out = newArrayList();
for (i = 0; i < myArray.length; i++) {
    Object extract = myArray[i];
    out.add(extract);
return (out);
```

ArrayListarrayToArraylist(String[] array) array To Arraylist

```java title=Example.java
returnnewArrayList<String>(Arrays.asList(array));
```

ArrayListarrayToArrayList(T[] array) Converts a Java array to an ArrayList .

```java title=Example.java
if (array == null)
    thrownewIllegalArgumentException("Parameter 'array' cannot be null!");
ArrayList<T> arrayList = newArrayList<T>();
for (T element : array)
    arrayList.add(element);
return arrayList;
```

ArrayListarrayToArraylist(T[] array) array To Arraylist

```java title=Example.java
ArrayList<T> ret = newArrayList<T>();
for (T e : array) {
    ret.add(e);
return ret;
```

ArrayListasArrayList(Collection c) as Array List

```java title=Example.java
return (ArrayList) asTargetTypeCollection(c, ArrayList.class);
```

ArrayListasArrayList(T... elements) as Array List

```java title=Example.java
ArrayList<T> result = newArrayList<T>();
for (T elem : elements) {
    result.add(elem);
return result;
```

ArrayListasArrayList(T[] tArray) Converts the typed Array into a typed ArrayList

```java title=Example.java
ArrayList<T> tList = newArrayList<T>();
for (T t : tArray) {
    tList.add(t);
return tList;
```

ListasArrayList(T[] values) Arrays.asList cannot be reliably used for SQL parameters on MyBatis < 3.3.0

```java title=Example.java
ArrayList<T> result = newArrayList<T>();
Collections.addAll(result, values);
return result;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
