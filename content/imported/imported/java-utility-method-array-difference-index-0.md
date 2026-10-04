---
title: Java Utililty Methods Array Difference
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Difference are organized into topic(s).
section: Imported - java2s Archive
order: 50053
source: https://www.java2s.com/example/java-utility-method/array-difference-index-0.html
---
List of utility methods to do Array Difference

## Description

The list of methods to do Array Difference are organized into topic(s).

## Method

float[]difference(float[] v1, float[] v2) difference

```java title=Example.java
if (v1.length != v2.length) {
    thrownewIllegalArgumentException("Arrays lengths are different");
float[] out = newfloat[v1.length];
for (int i = 0; i < out.length; i++) {
    out[i] = v1[i] - v2[i];
return out;
...
```

intdifference2D(char[][] first, char[][] second) difference D

```java title=Example.java
int result = 0;
for (int i = 0; i < first.length; i++) {
    for (int j = 0; j < first[0].length; j++) {
        if (first[i][j] != second[i][j]) {
            result++;
return result;
```

intdifference5D(char[][][][][] first, char[][][][][] second) difference D

```java title=Example.java
int result = 0;
for (int i1 = 0; i1 < first.length; i1++) {
    for (int i2 = 0; i2 < first.length; i2++) {
        for (int i3 = 0; i3 < first.length; i3++) {
            for (int i4 = 0; i4 < first.length; i4++) {
                for (int i5 = 0; i5 < first.length; i5++) {
                    if (first[i1][i2][i3][i4][i5] != second[i1][i2][i3][i4][i5]) {
                        result++;
...
```

float[]differenceFunction(float[] data, int windowLength) difference Function

```java title=Example.java
float[] diffFunction = newfloat[data.length];
float sum;
for (int t = 0; t < data.length; t++) {
    sum = 0;
    for (int j = 0; j < Math.min(j + windowLength, data.length - t); j++) {
        sum += Math.pow(data[j] - data[j + t], 2);
    diffFunction[t] = sum;
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
