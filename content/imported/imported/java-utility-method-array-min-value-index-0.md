---
title: Java Utililty Methods Array Min Value
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Min Value are organized into topic(s).
section: Imported - java2s Archive
order: 50083
source: https://www.java2s.com/example/java-utility-method/array-min-value-index-0.html
---
List of utility methods to do Array Min Value

## Description

The list of methods to do Array Min Value are organized into topic(s).

## Method

intargmin(double... vs) argmin

```java title=Example.java
double min = vs[0];
int minI = 0;
for (int i = 1; i < vs.length; i++) {
    double v = vs[i];
    if (v < min) {
        min = v;
        minI = i;
return minI;
```

intargmin(final double[] vec) Returns the index of the smallest element in a vector.

```java title=Example.java
assert vec != null;
double min = vec[0];
int argmin = 0;
for (int i = 1; i < vec.length; i++) {
    finaldouble tmp = vec[i];
    if (tmp < min) {
        min = tmp;
        argmin = i;
...
```

intargmin(int[] a) argmin

```java title=Example.java
int re = Integer.MAX_VALUE;
int arg = -1;
for (int i = 0; i < a.length; i++) {
    if (a[i] < re) {
        re = a[i];
        arg = i;
return arg;
```

intargMin(int[] a) arg Min

```java title=Example.java
int v = Integer.MAX_VALUE;
int ind = -1;
for (int i = 0; i < a.length; i++) {
    if (a[i] < v) {
        v = a[i];
        ind = i;
return ind;
```

double[]arrayMin(double minVal, double[] vals) Applies a min value to all elements in an array

```java title=Example.java
double[] out = newdouble[vals.length];
for (int i = 0; i < vals.length; i++) {
    out[i] = Math.min(minVal, vals[i]);
return out;
```

doublearrayMin(double[] arr) A method to find min element in an array of doubles.

```java title=Example.java
double min = Double.POSITIVE_INFINITY;
for (double cur : arr)
    min = Math.min(min, cur);
return min;
```

doublearrayMin(double[] x) array Min

```java title=Example.java
if (x.length == 0) {
    thrownewIllegalArgumentException();
double result = x[0];
for (int i = 1; i < x.length; i++) {
    if (result > x[i]) {
        result = x[i];
return result;
```

doublearrayMin(final double[] array) array Min

```java title=Example.java
return array[minElementIndex(array)];
```

intarrayMin(int[] property) array Min

```java title=Example.java
int[] copy = property.clone();
int min = 0;
int numElements = copy.length;
Arrays.sort(copy);
if (numElements > 0)
    min = copy[0];
return min;
```

floatfindMin(float[] array) Finds minimal element in array

```java title=Example.java
float min = Float.MAX_VALUE;
for (int i = 0; i < array.length; i++) {
    if (array[i] < min) {
        min = array[i];
return min;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
