---
title: Java Utililty Methods Array to List
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to List are organized into topic(s).
section: Imported - java2s Archive
order: 50122
source: https://www.java2s.com/example/java-utility-method/array-to-list-index-0.html
---
List of utility methods to do Array to List

## Description

The list of methods to do Array to List are organized into topic(s).

## Method

StringarrayToCommaList(Object[] array) Format an array of Object as a list with commas, like "apples, oranges, and bananas"); XXX Should have a boolean for the final comma :-)

```java title=Example.java
StringBuffer sb = newStringBuffer();
for (int i = 0; i < array.length; i++) {
    if (i > 0 && i < array.length - 1) {
        sb.append(',');
    if (i > 0) {
        sb.append(' ');
    if (i == (array.length - 1)) {
        sb.append("and ");
    sb.append(array[i]);
return sb.toString();
```

StringarrayToCommaList(String[] array) Converts an array of strings into a comma seperated string.

```java title=Example.java
return arrayToList(array, ",");
```

ListarrayToList(final T... items) array To List

```java title=Example.java
returnArrays.asList(items);
```

StringarrayToList(int[] intArr, int cnt) array To List

```java title=Example.java
return arrayToList(intArr, 0, cnt);
```

ListarrayToList(Object[] objs) array To List

```java title=Example.java
if (objs == null)
    return null;
List ret = newArrayList(objs.length);
for (Object obj : objs) {
    ret.add(obj);
return ret;
```

ArrayListarrayToList(String... stringArray) Retrieves an array list containing the contents of the provided array.

```java title=Example.java
if (stringArray == null) {
    return null;
ArrayList<String> stringList = newArrayList<>(stringArray.length);
Collections.addAll(stringList, stringArray);
return stringList;
```

StringarrayToList(String[] array, String delim) Converts an array of strings into a delimeter seperated string.

```java title=Example.java
String result = "";
for (int i = 0; i < array.length; i++) {
    result += array[i] + ((i == (array.length - 1)) ? "" : delim);
return result;
```

ListarrayToList(String[] str) array To List

```java title=Example.java
List list = Arrays.asList(str);
return list;
```

ListarrayToList(T[] array) Puts varargs in a mutable list.

```java title=Example.java
List<T> list = newLinkedList<>();
Collections.addAll(list, array);
return list;
```

ListarrayToList(T[] t) array To List

```java title=Example.java
if (t == null || t.length == 0) {
    returnnewArrayList<T>(0);
List<T> list = newArrayList<T>(t.length);
Collections.addAll(list, t);
return list;
```
