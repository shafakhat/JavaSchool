---
title: Java Utililty Methods Array to Delimited String
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to Delimited String are organized into topic(s).
section: Imported - java2s Archive
order: 50119
source: https://www.java2s.com/example/java-utility-method/array-to-delimited-string-index-0.html
---
List of utility methods to do Array to Delimited String

## Description

The list of methods to do Array to Delimited String are organized into topic(s).

## Method

StringarrayAsCommaSeperatedList(String... items) array As Comma Seperated List

```java title=Example.java
String result = items[0];
for (int i = 1; i < items.length; i++) {
    result += "," + items[i];
return result;
```

StringarrayAsString(final int[] _intArray) Utility method (debug/test): Trivial helper function for quick trace output.

```java title=Example.java
String strArray = "";
for (int i = 0; i < _intArray.length; i++)
    strArray += _intArray[i] + " ";
return strArray;
```

StringarrayToCommaDelimitedString(Object[] arr) Convenience method to return a String array as a CSV String.

```java title=Example.java
return arrayToDelimitedString(arr, ",");
```

StringarrayToCommaDelimitedString(Object[] arr) array To Comma Delimited String

```java title=Example.java
return arrayToDelimitedString(arr, ",");
```

StringarrayToCommaDelimitedString(Object[] strings) Turns this string array in one comma-delimited string.

```java title=Example.java
if (strings == null) {
    return"";
StringBuilder builder = newStringBuilder();
for (int i = 0; i < strings.length; i++) {
    if (i > 0) {
        builder.append(",");
    builder.append(String.valueOf(strings[i]));
return builder.toString();
```

StringarrayToCommaSeparatedString(int[] array) array To Comma Separated String

```java title=Example.java
if (array == null) {
    return null;
StringBuffer result = newStringBuffer();
for (int i = 0; i < array.length; i++) {
    result.append(array[i] + (i == array.length - 1 ? "" : ", "));
return result.toString();
...
```

StringarrayToCommaString(int[] array) array To Comma String

```java title=Example.java
StringBuffer sb = newStringBuffer();
for (int i = array.length - 1; i >= 0; i--) {
    if (array[i] == 0) {
        continue;
    sb.append(array[i]);
    sb.append(i == 0 ? "" : ",");
return sb.toString();
```

StringarrayToCommaString(int[] array) array To Comma String

```java title=Example.java
StringBuffer sb = newStringBuffer();
for (int i = array.length - 1; i >= 0; i--) {
    if (array[i] == 0) {
        continue;
    sb.append(array[i]);
    sb.append(i == 0 ? "" : ",");
return sb.toString();
```

StringarrayToDelimitedString(Object[] arr, String delim) array To Delimited String

```java title=Example.java
if (arr == null || arr.length == 0) {
    return"";
StringBuffer sb = newStringBuffer();
for (int i = 0; i < arr.length; i++) {
    if (i > 0) {
        sb.append(delim);
    sb.append('\'');
    sb.append(arr[i]);
    sb.append('\'');
return sb.toString();
```

StringarrayToDelimitedString(Object[] arr, String delim) Convenience method to return a String array as a delimited (e.g.

```java title=Example.java
if (arr == null)
    return"null";
else {
    StringBuffer sb = newStringBuffer();
    for (int i = 0; i < arr.length; i++) {
        if (i > 0)
            sb.append(delim);
        sb.append(arr[i]);
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
