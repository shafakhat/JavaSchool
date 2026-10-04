---
title: Java Utililty Methods Array Replace
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Replace are organized into topic(s).
section: Imported - java2s Archive
order: 50096
source: https://www.java2s.com/example/java-utility-method/array-replace-index-0.html
---
List of utility methods to do Array Replace

## Description

The list of methods to do Array Replace are organized into topic(s).

## Method

StringarrayReplace(String haystack, String[] search, String[] replacements) array Replace

```java title=Example.java
String toReturn = haystack;
for (int i = 0; i < search.length; i++) {
    toReturn = toReturn.replace(search[i], replacements[i]);
return toReturn;
```

char[]replace(char[] array, char[] toBeReplaced, char[] replacementChars) replace

```java title=Example.java
int max = array.length;
int replacedLength = toBeReplaced.length;
int replacementLength = replacementChars.length;
int[] starts = newint[5];
int occurrenceCount = 0;
if (!equals(toBeReplaced, replacementChars)) {
    next: for (int i = 0; i < max; i++) {
        int j = 0;
...
```

char[][]replace(char[][] arrays, char character, char[][] replacements) replace

```java title=Example.java
List<char[]> list = newArrayList<char[]>();
for (char[] array : arrays) {
    String string = String.valueOf(array);
    if (string.indexOf(character) >= 0) {
        for (char[] replacement : replacements) {
            list.add(string.replaceAll(String.valueOf(character), String.valueOf(replacement))
                    .toCharArray());
    } else {
        list.add(array);
return list.toArray(newchar[list.size()][]);
```

char[][]replace(char[][] arrays, char character, char[][] replacements) replace

```java title=Example.java
List<char[]> list = newArrayList<char[]>();
for (char[] array : arrays) {
    String string = String.valueOf(array);
    if (string.indexOf(character) >= 0) {
        for (char[] replacement : replacements) {
            list.add(string.replaceAll(String.valueOf(character), String.valueOf(replacement))
                    .toCharArray());
    } else {
        list.add(array);
return list.toArray(newchar[list.size()][]);
```

Object[]replaceAll(final Object[] objs, final String str) Returns stripped value from the specified array of stuff

```java title=Example.java
if (isEmpty(objs, false)) {
    return null;
List<Object> list = newArrayList<Object>(Arrays.asList(trimArray(objs)));
list.removeAll(Collections.singletonList(str));
return list.toArray(newObject[list.size()]);
```

String[]replaceAll(final String[] args, final String from, final String to) replace All

```java title=Example.java
returnArrays.stream(args).map(arg -> from.equals(arg) ? to : arg).toArray(String[]::new);
```

StringreplaceAll(String src, String[] replace, String[] by) Replaces all Strings in replace by the corresponding String in by, that is the ith String in replace is replaced by the ith String in by, in order.

```java title=Example.java
for (int i = 0; i < replace.length; i++) {
    src = src.replace(replace[i], by[i]);
return src;
```

StringreplaceChars(String s, char[] from, char[] to) replace Chars

```java title=Example.java
StringBuilder sb = newStringBuilder();
for (int i = 0; i < s.length(); i++) {
    char ch = s.charAt(i);
    int index = Arrays.binarySearch(from, ch);
    if (index >= 0) {
        sb.append(to[index]);
    } else {
        sb.append(ch);
...
```

StringreplaceIgnoreCase(final String s, final String[] sub, final String[] with) replace Ignore Case

```java title=Example.java
if (sub.length != with.length || sub.length == 0) {
    return s;
int start = 0;
finalStringBuilder buf = newStringBuilder(s.length());
while (true) {
    finalint[] res = indexOfIgnoreCase(s, sub, start);
    if (res == null) {
...
```

String[]replaceInArray(String[] thisArray, String findThis, String replaceWithThis) replace In Array

```java title=Example.java
String[] outputArray = newString[thisArray.length];
for (int i = 0; i < thisArray.length; i++) {
    outputArray[i] = thisArray[i].replaceAll(findThis, replaceWithThis);
return outputArray;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
