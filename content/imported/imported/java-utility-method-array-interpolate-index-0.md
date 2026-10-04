---
title: Java Utililty Methods Array Interpolate
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Interpolate are organized into topic(s).
section: Imported - java2s Archive
order: 50074
source: https://www.java2s.com/example/java-utility-method/array-interpolate-index-0.html
---
List of utility methods to do Array Interpolate

## Description

The list of methods to do Array Interpolate are organized into topic(s).

## Method

doubleinterpolate(double x, double xLeft, double yLeft, double xRight, double yRight, double[] weights) Interpolates the Y value for a given X and the surrounding x/y pairs.

```java title=Example.java
double result;
double[] w;
w = weights(x, xLeft, xRight);
weights[0] = w[0];
weights[1] = w[1];
result = yLeft * weights[0] + yRight * weights[1];
return result;
```

doubleinterpolate(double x, double[] begin, double[] end) interpolate

```java title=Example.java
return begin[1] + (x - begin[0]) / (end[0] - begin[0]) * (end[1] - begin[1]);
```

doubleinterpolate(double xa[], double ya[], double x) This function performs a polynomial interpolation using a set of given x and y values.

```java title=Example.java
if (xa.length != ya.length || xa.length == 0 || ya.length == 0) {
    System.out.println("** Invalid Parameter");
    returnDouble.NaN;
int n = xa.length;
double y = 0.0;
double dy = 0.0;
int i, m, ns = 1;
...
```

doubleinterpolate(double[] array, int[] translation, double index) interpolate

```java title=Example.java
int length = translation == null ? array.length : translation.length;
int floor = (int) index;
int[] intIndex = newint[] { floor % length, (floor + 1) % length };
if (translation != null)
    for (int i = 0; i < intIndex.length; i++)
        intIndex[i] = translation[intIndex[i]];
double[] value = newdouble[] { array[intIndex[0]], array[intIndex[1]] };
double percent = index - floor;
...
```

double[]interpolate(double[] end0, double[] end1, double[] mid) interpolate

```java title=Example.java
double dx = mid[0] - end0[0];
double dy = mid[1] - end0[1];
double d0 = Math.sqrt(dx * dx + dy * dy);
dx = mid[0] - end1[0];
dy = mid[1] - end1[1];
double d1 = Math.sqrt(dx * dx + dy * dy);
if (d0 < zeroMax || d1 < zeroMax) {
    returnnewdouble[] { (end0[0] + end1[0]) / 2, (end0[1] + end1[1]) / 2 };
...
```

doubleinterpolate(double[] points, double[] values, double interpolateAt) Estimates the function value at a specified point on x-axis using the Lagrange interpolation.

```java title=Example.java
if (points.length != values.length) {
    thrownewArithmeticException("The number of elements in both arrays does not match!");
} else {
    double value = 0;
    double tempValue = 0;
    for (int i = 0; i < points.length; i++) {
        tempValue = values[i];
        for (int j = 0; j < i; j++) {
...
```

double[]interpolate(double[] x, double D) interpolate

```java title=Example.java
double[] y = null;
if (x != null) {
    int ylen = (int) Math.floor(x.length * D + 0.5);
    y = newdouble[ylen];
    int xind;
    double xindDouble;
    for (int i = 0; i < ylen; i++) {
        xindDouble = i / D;
...
```

double[]interpolate(double[] X, double[] Y, double[] Z) Interpolate using a cubic spline.

```java title=Example.java
double[] interpolatedValues = newdouble[Z.length];
int n = X.length;
double[] tmpY = newdouble[n + 1];
double[] tmpX = newdouble[n + 1];
for (int i = 0; i < n; i++) {
    tmpY[i + 1] = Y[i];
    tmpX[i + 1] = X[i];
double[] y2 = newdouble[n + 1];
spline(tmpX, tmpY, n, 0., 0., y2);
double[] y = newdouble[1];
for (int i = 0; i < Z.length; i++) {
    splint(tmpX, tmpY, y2, n, Z[i], y);
    interpolatedValues[i] = y[0];
return interpolatedValues;
```

double[]interpolate(double[] x, int newLength) interpolate

```java title=Example.java
double[] y = null;
if (newLength > 0) {
    int N = x.length;
    if (N == 1) {
        y = newdouble[1];
        y[0] = x[0];
        return y;
    } elseif (newLength == 1) {
...
```

voidinterpolate(float out[], float in1[], float in2[], int in2_idx, float coef, int length) interpolate

```java title=Example.java
int i;
float invcoef;
invcoef = 1.0f - coef;
for (i = 0; i < length; i++) {
    out[i] = coef * in1[i] + invcoef * in2[i + in2_idx];
```
