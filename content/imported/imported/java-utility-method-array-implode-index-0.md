---
title: Java Utililty Methods Array Implode
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Implode are organized into topic(s).
section: Imported - java2s Archive
order: 50072
source: https://www.java2s.com/example/java-utility-method/array-implode-index-0.html
---
List of utility methods to do Array Implode

## Description

The list of methods to do Array Implode are organized into topic(s).

## Method

Stringimplode(double[] array, String separator) implode

```java title=Example.java
StringBuffer out = newStringBuffer();
boolean first = true;
for (double v : array) {
    if (first) {
        first = false;
    } else {
        out.append(separator);
    out.append(v);
return out.toString();
```

Stringimplode(final String[] array, final String delim) Implodes a string array into a String.

```java title=Example.java
return implode(array, delim, false);
```

Stringimplode(final String[] pStrArray) implode

```java title=Example.java
return implode(pStrArray, "\t");
```

Stringimplode(Object[] array, String separator) implode

```java title=Example.java
if (array == null)
    return null;
if (array.length == 0)
    return"";
StringBuffer result = newStringBuffer(array[0].toString());
for (int i = 1; i < array.length; i++) {
    if (separator != null)
        result.append(separator);
...
```

Stringimplode(Object[] ary, String delim) Glues together the array with delim inserted between elements.

```java title=Example.java
return implode(ary, delim, 0, ary.length);
```

Stringimplode(String delim, Object[] objects) This method merges an array of objects to a single string

```java title=Example.java
return implode(delim, Arrays.asList(objects));
```

Stringimplode(String delim, String[] args) implode

```java title=Example.java
StringBuffer sb = newStringBuffer();
for (int i = 0; i < args.length; i++) {
    if (i > 0) {
        sb.append(delim);
    sb.append(args[i]);
return sb.toString();
...
```

Stringimplode(String[] array, String separator) Returns the given array joined by a separator.

```java title=Example.java
if (array.length == 0) {
    return"";
StringBuilder buffer = newStringBuilder();
for (String str : array) {
    buffer.append(separator);
    buffer.append(str);
return buffer.substring(separator.length()).trim();
```

Stringimplode(String[] data, String glue) Converts a list of strings into a long string separated by glue.

```java title=Example.java
if (data == null || data.length == 0)
    return"";
StringBuilder sb = newStringBuilder();
int total = data.length;
for (int i = 0; i < total; i++) {
    String item = data[i];
    sb.append(item).append(glue);
String result = sb.toString();
if (result.endsWith(glue))
    result = result.substring(0, result.lastIndexOf(glue));
return result;
```

Stringimplode(String[] inputArray, String glueString) Method to join array elements of type string

```java title=Example.java
String output = EMPTY_STRING;
if (inputArray != null && inputArray.length > 0) {
    StringBuilder sb = newStringBuilder();
    sb.append(inputArray[0]);
    for (int i = 1; i < inputArray.length; i++) {
        sb.append(glueString);
        sb.append(inputArray[i]);
    output = sb.toString();
return output;
```
