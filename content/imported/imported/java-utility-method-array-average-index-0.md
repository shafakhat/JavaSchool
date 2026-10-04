---
title: Java Utililty Methods Array Average
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Average are organized into topic(s).
section: Imported - java2s Archive
order: 50031
source: https://www.java2s.com/example/java-utility-method/array-average-index-0.html
---
List of utility methods to do Array Average

## Description

The list of methods to do Array Average are organized into topic(s).

## Method

Doubleaverage(Double sum, Double size) average

```java title=Example.java
if (Math.abs(size) < 0.0001)
    return 0.0;
return sum / size;
```

doubleaverage(double values[]) average

```java title=Example.java
int s = values.length;
if (s == 0)
    returnDouble.MIN_VALUE;
double avg = 0.0;
for (int i = 0; i < s; i++)
    avg += values[i];
return avg / s;
```

doubleaverage(double x, double y) Average two numbers

```java title=Example.java
return (x + y) / 2;
```

doubleaverage(double x1, double x2) average

```java title=Example.java
return (x1 + x2) / 2;
```

doubleaverage(double... args) average

```java title=Example.java
double total = 0D;
for (double value : args) {
    total += value;
return total / args.length;
```

doubleaverage(double... vals) If you think your values will overflow this operation, then roll your own

```java title=Example.java
if (vals == null || vals.length == 0) {
    return 0;
return sum(vals) / vals.length;
```

doubleaverage(double[] a) average

```java title=Example.java
return sum(a) / a.length;
```

doubleaverage(double[] a) average

```java title=Example.java
return sum(a) / a.length;
```

Doubleaverage(Double[] arr) average

```java title=Example.java
return sum(arr) / arr.length;
```

doubleaverage(double[] array) Returns the average value of an array.

```java title=Example.java
return array.length == 0 ? 0 : sum(array) / array.length;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
