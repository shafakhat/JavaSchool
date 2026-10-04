---
title: Java Utililty Methods Array Scale
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Scale are organized into topic(s).
section: Imported - java2s Archive
order: 50100
source: https://www.java2s.com/example/java-utility-method/array-scale-index-0.html
---
List of utility methods to do Array Scale

## Description

The list of methods to do Array Scale are organized into topic(s).

## Method

Double[]arrayScale(final Double[] first, final double scale) Scales the elements of the arrays with a contstant.

```java title=Example.java
finalDouble[] toret = newDouble[first.length];
for (int i = 0; i < first.length; i++) {
    toret[i] = first[i] * scale;
return toret;
```

byte[]expandToLength16(byte scaledValue[], final boolean isNegative) Converts BigInteger's byte representation containing a scaled magnitude to a fixed size 16 byte array and set the sign in the most significant byte's most significant bit.

```java title=Example.java
if (scaledValue.length == 16) {
    return scaledValue;
byte replacement[] = newbyte[16];
if (isNegative) {
    java.util.Arrays.fill(replacement, (byte) -1);
for (int ii = 15; 15 - ii < scaledValue.length; ii--) {
...
```

double[]minMaxScale(final double[] x) min Max Scale

```java title=Example.java
DoubleSummaryStatistics s = Arrays.stream(x).summaryStatistics();
return s.getMax() == 1 && s.getMin() == 0 ? x
        : Arrays.stream(x).map(d -> (d - s.getMin()) / (s.getMax() - s.getMin())).toArray();
```

double[][]scale(double[][] as) scale

```java title=Example.java
finalint VALUES = as[0].length;
double[][] result = newdouble[as.length][VALUES];
for (int v = 0; v < VALUES; v++) {
    double max = as[as.length - 1][v];
    for (int i = 0; i < as.length; i++) {
        result[i][v] = as[i][v] / max;
System.out.println(Arrays.deepToString(result));
return result;
```

double[]scale(final double[] a, double scale) scale

```java title=Example.java
returnArrays.stream(a).parallel().map(x -> x * scale).toArray();
```

doublescaleMAD(double[] data) Scale MAD in order to use it as a consistent estimator for the estimation of the standard deviation

```java title=Example.java
finaldouble constant = 1.4826;
return constant * computeMAD(data);
```

int[]scalePoints(double[] points, int height) scale Points

```java title=Example.java
double maxValue = -1.0;
for (int i = 0; i < points.length; i++) {
    if (points[i] > maxValue && points[i] != Double.POSITIVE_INFINITY) {
        maxValue = points[i];
return scalePoints(points, height, maxValue);
```
