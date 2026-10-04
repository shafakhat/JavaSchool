---
title: Java Utililty Methods Array Max Value
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Max Value are organized into topic(s).
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/https://www.java2s.com/example/java-utility-method/array-max-value-index-0.html
---
List of utility methods to do Array Max Value

## Description

The list of methods to do Array Max Value are organized into topic(s).

## Method

intargmax(double[] array, boolean naturalNumbers) Returns the index of the maximal value in a double[]

```java title=Example.java
int best = -1;
double value = (naturalNumbers) ? 0D : Double.MIN_VALUE;
for (int i = 0; i < array.length; ++i) {
    if (array[i] > value) {
        value = array[i];
        best = i;
return best;
```

intargmax(double[] weights) argmax

```java title=Example.java
if (weights == null)
    return -1;
if (weights.length == 1)
    return 0;
double max = weights[0];
int maxI = 0;
for (int i = 1; i < weights.length; i++)
    if (weights[i] > max)
...
```

intargmax(final double[] vec) Returns the index of the greatest element in a vector.

```java title=Example.java
assert (vec != null);
double max = vec[0];
int argmax = 0;
for (int i = 1; i < vec.length; i++) {
    final double tmp = vec[i];
    if (tmp > max) {
        max = tmp;
        argmax = i;
...
```

intargmax(float[] args) argmax

```java title=Example.java
int result = 0;
for (int i = 1; i < args.length; i++) {
    if (Float.compare(args[result], args[i]) < 0)
        result = i;
return result;
```

intargMax(int[] a) arg Max

```java title=Example.java
int v = Integer.MIN_VALUE;
int ind = -1;
for (int i = 0; i < a.length; i++) {
    if (a[i] > v) {
        v = a[i];
        ind = i;
return ind;
```

intargmax(int[] a) argmax

```java title=Example.java
int re = Integer.MIN_VALUE;
int arg = -1;
for (int i = 0; i < a.length; i++) {
    if (a[i] > re) {
        re = a[i];
        arg = i;
return arg;
```

intargmax(int[] array) argmax

```java title=Example.java
return getArgmax(array);
```

intargmax(int[] array) Returns the index of the max value in the specified array

```java title=Example.java
int index = -1;
int max = Integer.MIN_VALUE;
for (int i = 0; i < array.length; i++) {
    if (array[i] > max) {
        max = array[i];
        index = i;
return index;
```

intargmax(int[] input) Returns the index of the largest element in an array.

```java title=Example.java
int i = input.length - 1;
int currentMaximum = input[i];
int currentArgmax = i;
while (i >= 0) {
    if (input[i] > currentMaximum) {
        currentMaximum = input[i];
        currentArgmax = i;
    i++;
return currentArgmax;
```

double[]arrayMax(double maxVal, double[] vals) Applies a max value to all elements in an array

```java title=Example.java
double[] out = new double[vals.length];
for (int i = 0; i < vals.length; i++) {
    out[i] = Math.max(maxVal, vals[i]);
return out;
```
