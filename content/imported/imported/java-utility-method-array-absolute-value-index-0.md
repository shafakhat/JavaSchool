---
title: Java Utililty Methods Array Absolute Value
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Absolute Value are organized into topic(s).
section: Imported - java2s Archive
order: 50028
source: https://www.java2s.com/example/java-utility-method/array-absolute-value-index-0.html
---
List of utility methods to do Array Absolute Value

## Description

The list of methods to do Array Absolute Value are organized into topic(s).

## Method

intabs_sum(int[] data) Return sum of absVal of each index

```java title=Example.java
int sum = 0;
for (int i = 0; i < data.length; i++) {
    sum += Math.abs(data[i]);
return sum;
```

doubleabsAvg(double[] inputArray, int divisions, int cap) abs Avg

```java title=Example.java
double result = 0;
int count = inputArray.length;
if (count > cap) {
    double[][] parts = newdouble[count][];
    for (int i = 0; i < divisions; i++) {
        int start = (count * i) / divisions;
        int end = (count * (i + 1)) / divisions;
        int length = end - start;
...
```

Double[]absDiff(Double[] a, Double[] b) Compute the element-wise absolute difference between two arrays of the same length.

```java title=Example.java
Double[] result = newDouble[a.length];
for (int i = 0; i < a.length; i++) {
    result[i] = Math.abs(a[i] - b[i]);
;
return result;
```

doubleabsMax(double x, double y) Maximum of the absolute value of two numbers.

```java title=Example.java
if (x < 0.0D) {
    x = -x;
if (y < 0.0D) {
    y = -y;
return x > y ? x : y;
```

doubleabsMax(double[] arr) find absolute max value in array

```java title=Example.java
double max = Math.abs(arr[0]);
for (int i = 0; i < arr.length; i++) {
    doubleval = Math.abs(arr[i]);
    if (val > max) {
        max = val;
return max;
...
```

doubleabsMax(double[] data) Find the maximum of the absolute values of all elements in the array, ignoring elements that are NaN.

```java title=Example.java
double max = Double.NaN;
for (int i = 0; i < data.length; i++) {
    if (Double.isNaN(data[i]))
        continue;
    double abs = Math.abs(data[i]);
    if (Double.isNaN(max) || abs > max)
        max = abs;
return max;
```

doubleabsMax(double[] vector) abs Max

```java title=Example.java
double result = 0;
for (double d : vector) {
    if (d != Double.NEGATIVE_INFINITY && Math.abs(d) > Math.abs(result)) {
        result = d;
return result;
```

doubleabsMean(double[] arr) absMean

```java title=Example.java
double result = 0;
double len = arr.length;
for (int i = 0; i < arr.length; i++) {
    doubleval = Math.abs(arr[i]);
    result += val / len;
return result;
```

doubleabsMean(double[] x) abs Mean

```java title=Example.java
double m = 0.0;
for (int i = 0; i < x.length; i++)
    m += Math.abs(x[i]);
m /= x.length;
return m;
```

float[][]absolulteValue(float[][] image) Returns an image where all of the values have been absolute valued

```java title=Example.java
float[][] out_float_mat = newfloat[image.length][image[0].length];
for (int i = 0; i < image.length; i++) {
    for (int j = 0; j < image[0].length; j++) {
        out_float_mat[i][j] = Math.abs(image[i][j]);
return out_float_mat;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
