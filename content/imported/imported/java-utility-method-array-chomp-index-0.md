---
title: Java Utililty Methods Array Chomp
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Chomp are organized into topic(s).
section: Imported - java2s Archive
order: 50035
source: https://www.java2s.com/example/java-utility-method/array-chomp-index-0.html
---
List of utility methods to do Array Chomp

## Description

The list of methods to do Array Chomp are organized into topic(s).

## Method

Stringchomp(char[] charArray) Given a character array, this method constructs a new string without trailing carriage return or newline characters.

```java title=Example.java
int length = charArray.length;
int endIndex = charArray.length - 1;
for (int i = endIndex; i > -1; i--) {
    if (charArray[i] == '\r' || charArray[i] == '\n') {
        length--;
    } else {
        break;
returnnewString(charArray, 0, length);
```

char[]chompArray(char[] array, int start, int end) chomp Array

```java title=Example.java
char[] newArray = newchar[end - start];
for (int i = 0, j = start; j < end; i++, j++) {
    newArray[i] = array[j];
return newArray;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
