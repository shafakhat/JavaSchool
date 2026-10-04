---
title: Java Utililty Methods Array Flip
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Flip are organized into topic(s).
section: Imported - java2s Archive
order: 50068
source: https://www.java2s.com/example/java-utility-method/array-flip-index-0.html
---
List of utility methods to do Array Flip

## Description

The list of methods to do Array Flip are organized into topic(s).

## Method

String[][]flip(String[][] data) flip

```java title=Example.java
String[][] flipped = newString[data[0].length][data.length];
for (int i = 0; i < data.length; i++) {
    for (int j = 0; j < data[i].length; j++) {
        flipped[j][i] = data[i][j];
return flipped;
```

T[]flip(T[] array) flip

```java title=Example.java
T[] tmp = array.clone();
for (int i = 0; i < array.length; i++) {
    tmp[i] = array[array.length - i];
return tmp;
```

byte[]flipAllBits(byte[] bytes) flip All Bits

```java title=Example.java
return flipAllBits(bytes, 0);
```

byte[]flipAllBitsInPlace(byte[] bytes) This flips the bits and returns the same byte[].

```java title=Example.java
return flipAllBitsInPlace(bytes, 0, bytes.length);
```

int[]flipChessboardVertically(int[] chessboard) flip Chessboard Vertically

```java title=Example.java
int len = chessboard.length;
int[] newChessboard = newint[len];
for (int i = 0; i < len; i++) {
    newChessboard[i] = chessboard[len - 1 - i];
return newChessboard;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
