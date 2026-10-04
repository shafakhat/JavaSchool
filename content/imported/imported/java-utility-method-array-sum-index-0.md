---
title: Java Utililty Methods Array Sum
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Sum are organized into topic(s).
section: Imported - java2s Archive
order: 50113
source: https://www.java2s.com/example/java-utility-method/array-sum-index-0.html
---
List of utility methods to do Array Sum

## Description

The list of methods to do Array Sum are organized into topic(s).

## Method

voidarrayAdd(int[] sumFreq, int[] freq) array Add

```java title=Example.java
for (int i = 0; i < freq.length; i++) {
    sumFreq[i] += freq[i];
```

floatArrayCeilSum(float[] a) Array Ceil Sum

```java title=Example.java
float sum = 0.0f;
for (float aa : a) {
    sum += Math.ceil(aa);
return sum;
```

DoublearraySum(double[] a) Sum up array

```java title=Example.java
if (a == null)
    return 0.0;
if (a.length == 0)
    return 0.0;
double ret = 0.0;
for (int i = 0; i < a.length; i++) {
    ret += a[i];
return ret;
```

doublearraySum(double[] arr) array Sum

```java title=Example.java
double sum = 0;
for (double num : arr) {
    sum += num;
return sum;
```

doublearraySum(final double input[]) Calculates the sum of all array elements

```java title=Example.java
double sum = 0;
for (double v : input)
    sum = sum + v;
return sum;
```

floatArraySum(float[] a) Array Sum

```java title=Example.java
float sum = 0.0f;
for (float aa : a) {
    sum += aa;
return sum;
```

intarraySum(int[] intArray, short flag) Returns the sum of the values of all integer elements in an integer array

```java title=Example.java
int r = 0;
for (int i : intArray) {
    if (flag == 0 && i < 0) {
        thrownewIllegalArgumentException("all integers in array must be positive");
    } elseif (flag == 1 && i > 0) {
        thrownewIllegalArgumentException("all integers in array must be negative");
    r += i;
...
```

intgetSum(int[] array) get Sum

```java title=Example.java
int sum = 0;
for (intval : array)
    sum += val;
return sum;
```

intgetSum(int[] array) get Sum

```java title=Example.java
int ges = 0;
for (int value : array)
    ges += value;
return ges;
```

intsum( int[] a) sum

```java title=Example.java
if (a == null)
    thrownewException("Array is null.");
else {
    int sum = 0;
    for (int i = 0; i < a.length; i++)
        sum += a[i];
    return sum;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
