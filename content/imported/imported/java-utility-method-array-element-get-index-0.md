---
title: Java Utililty Methods Array Element Get
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Element Get are organized into topic(s).
section: Imported - java2s Archive
order: 50061
source: https://www.java2s.com/example/java-utility-method/array-element-get-index-0.html
---
List of utility methods to do Array Element Get

## Description

The list of methods to do Array Element Get are organized into topic(s).

## Method

TarrayElement(T[] array, int index) Gets the element at an index in the array, but returns null if the index is outside of the array bounds.

```java title=Example.java
if (index < 0 || index >= array.length)
    return null;
elsereturn array[index];
```

Tget(int index, final T[]... arrays) get

```java title=Example.java
int shift = index;
for (T[] tab : arrays) {
    if (shift < tab.length) {
        return tab[shift];
    } else {
        shift -= tab.length;
return null;
```

Objectget(Object[] array, int index) get

```java title=Example.java
return getArrayLength(array) > index ? array[index] : null;
```

Tget(T[] array, int index) get

```java title=Example.java
return isRange(array, index) ? array[index] : null;
```

Tget(T[] array, int index)

Returns the value at the given index in the arrayor null if the index is out of bounds.

```java title=Example.java
return index >= 0 && index < array.length ? array[index] : null;
```

Tget(T[] array, int index) get

```java title=Example.java
if (array.length < index + 1) {
    return null;
return array[index];
```

ArrayListgetAllMatches(String[] target, String[] pattern) Input: array of strings, and a target array Output: the array of all the appearance

```java title=Example.java
ArrayList<Integer> result = newArrayList<Integer>();
int start = 0;
while (start < target.length) {
    String[] subArray = newString[target.length - start];
    for (int iter = 0; iter < subArray.length; iter++) {
        subArray[iter] = target[iter + start];
    int index = getFirst(subArray, pattern);
...
```

MapgetArgPairsSeparatedByChar(String[] args, String separator) get Arg Pairs Separated By Char

```java title=Example.java
Map<String, String> argPairs = newHashMap<String, String>();
if (args != null) {
    for (String argPair : args) {
        String[] pair = argPair.split("=");
        if (pair.length > 1) {
            argPairs.put(pair[0], pair[1]);
return argPairs;
```

String[]getArgs(final String[] args, final String[] defaultValue, final String... flags) Retrieve multi argument after the given flag and until the next "-*".

```java title=Example.java
if (flags == null || flags.length == 0)
    return null;
if (args == null || args.length == 0)
    return defaultValue;
finalList<String> r = newArrayList<String>();
int i = 0;
outer: for (; i < args.length; i++)
    for (finalString flag : flags)
...
```

MapgetArgs(String[] args, String... singleArgs) Get CLI arguments.

```java title=Example.java
Map<String, String[]> params = newHashMap<String, String[]>();
for (int i = 0; i < args.length; i++) {
    String inArg = args[i];
    if (!inArg.startsWith("--")) {
        thrownewException("Wrong argument syntax: " + inArg);
    } else {
        inArg = inArg.substring(2);
    for (int j = 0; j < singleArgs.length; j++) {
        if (singleArgs[j].equals(inArg)) {
            params.put(inArg, newString[] {});
    if (inArg.contains("=")) {
        String[] keyset = inArg.split("=", 2);
        if (keyset[1].startsWith("{") && keyset[1].endsWith("}")) {
            params.put(keyset[0], newString[] { keyset[1].substring(1, keyset[1].length() - 1) });
        } else {
            params.put(keyset[0], keyset[1].split(","));
return params;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
