---
title: Java Utililty Methods Array Move
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Move are organized into topic(s).
section: Imported - java2s Archive
order: 50085
source: https://www.java2s.com/example/java-utility-method/array-move-index-0.html
---
List of utility methods to do Array Move

## Description

The list of methods to do Array Move are organized into topic(s).

## Method

voidArrayMove(byte b[], int srcOff, int dstOff, int Len) Array Move

```java title=Example.java
int i, j, k;
if (null == b || 0 == b.length || Len <= 0) {
    return;
if (srcOff > dstOff) {
    if (b.length < srcOff + Len) {
        Len = b.length - srcOff;
    k = srcOff + Len;
    for (i = srcOff, j = dstOff; i < k; i++, j++) {
        b[j] = b[i];
} elseif (srcOff < dstOff) {
    if (b.length < dstOff + Len) {
        Len = b.length - dstOff;
    k = dstOff + Len - 1;
    for (i = srcOff + Len - 1, j = k; i >= srcOff; i--, j--) {
        b[j] = b[i];
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
