---
title: Java Utililty Methods Array Covariance
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Covariance are organized into topic(s).
section: Imported - java2s Archive
order: 50045
source: https://www.java2s.com/example/java-utility-method/array-covariance-index-0.html
---
List of utility methods to do Array Covariance

## Description

The list of methods to do Array Covariance are organized into topic(s).

## Method

doublecovariance(double[] a, double amean, double[] b, double bmean) Compute co-variance of the supplied array pair

```java title=Example.java
double t = 0;
for (int i = 0; i < a.length; i++) {
    t += (a[i] - amean) * (b[i] - bmean);
return t / a.length;
```

doublecovariance(double[] a, double[] b) Calculates the covariance between the two double arrays a and b.

```java title=Example.java
if (a.length != b.length) {
    System.err.println("Arrays are not of the same size!");
    returnDouble.NaN;
double sumA = 0.0;
double sumB = 0.0;
double m_A = 0.0;
double m_B = 0.0;
...
```

doublecovariance(double[] x, double[] y)

Returns the covariance between the two arrays of data.

See - [Mathworld](http://mathworld.wolfram.com/Covariance.html)

```java title=Example.java
double c = 0;
double meanX = mean(x);
double meanY = mean(y);
for (int t = 0; t < x.length; t++) {
    c += (x[t] - meanX) * (y[t] - meanY);
return c / x.length;
```

doublecovariance(double[] x, double[] y, int delay)

Returns the covariance between the two arrays of data, with a given lag between the first and second.

See - [Mathworld](http://mathworld.wolfram.com/Covariance.html)

```java title=Example.java
double meanX = 0, meanY = 0;
for (int n = 0; n < x.length - delay; n++) {
    meanX += x[n];
    meanY += y[n + delay];
meanX /= (double) (x.length - delay);
meanY /= (double) (x.length - delay);
double c = 0;
...
```

doublecovariance(final double[] xArray, final double[] yArray) Computes the covariance of the two input arrays.

```java title=Example.java
double result = 0d;
finalint length = xArray.length;
finaldouble xMean = mean(xArray);
finaldouble yMean = mean(yArray);
for (int i = 0; i < length; i++) {
    finaldouble xDev = xArray[i] - xMean;
    finaldouble yDev = yArray[i] - yMean;
    result += (xDev * yDev - result) / (i + 1);
...
```

double[][]covariance(final double[][] data) covariance

```java title=Example.java
finalint len = data.length;
finaldouble[] means = newdouble[len];
finaldouble[][] ret = newdouble[len][len];
for (int i = 0; i < len; i++) {
    means[i] = mean(data[i]);
    for (int j = 0; j <= i; j++) {
        finaldouble d = sum(multiply(shift(data[i], -means[i]), shift(data[j], -means[j]))) / (len);
        ret[i][j] = d;
...
```

doublecovariance(int[] v1, int[] v2) Computes the covariance.

```java title=Example.java
if (v1.length != v2.length)
    thrownewIllegalArgumentException(
            "Arrays must have the same length : " + v1.length + ", " + v2.length);
finaldouble m1 = mean(v1);
finaldouble m2 = mean(v2);
double ans = 0.0;
for (int i = 0; i < v1.length; i++)
    ans += (v1[i] - m1) * (v2[i] - m2);
...
```

doublecovariance(Number[] x, Number[] y) Computes the covariance between the two data vectors and returns it.

```java title=Example.java
double result;
int i;
double xbar;
double ybar;
if (x.length != y.length)
    thrownewIllegalArgumentException("Arrays differ in length: " + x.length + " != " + y.length);
if (x.length == 0)
    thrownewIllegalArgumentException("0-length arrays provided!");
...
```

doublecovarianceOfDoubleArrays(double[] x, double[] y) computes the covariance between two arrays

```java title=Example.java
double meanX = computeMean(x);
double meanY = computeMean(y);
double covariance = 0;
for (int i = 0; i < x.length; i++) {
    covariance += ((x[i] - meanX) * (y[i] - meanY)) / x.length;
return covariance / x.length;
```

doublecovarianceTwoColumns(double[][] data, int col1, int col2)

Returns the covariance between two columns of data in a multivariate array.

See - [Mathworld](http://mathworld.wolfram.com/Covariance.html)

```java title=Example.java
double mean1 = mean(data, col1);
double mean2 = mean(data, col2);
return covarianceTwoColumns(data, col1, col2, mean1, mean2);
```
