---
title: Java Utililty Methods Angle
nav: Java Utililty Methods Angle
description: doubleangle(double aX, double aY, double bX, double bY) angle
section: Imported - java2s Archive
order: 50018
source: https://www.java2s.com/example/java-utility-method/angle-index-0.html
---
List of utility methods to do Angle

## Description

The list of methods to do Angle are organized into topic(s).

## Method

doubleangle(double a, double b) angle

```java title=Example.java
double result = Math.abs(a - b) % (Math.PI * 2.0);
return result > Math.PI ? Math.PI * 2.0 - result : result;
```

doubleangle(double aX, double aY, double bX, double bY) angle

```java title=Example.java
double deltaX = bX - aX;
double deltaY = bY - aY;
if (deltaX == 0) {
    return 90;
if (deltaY == 0) {
    return 0;
double tang = deltaY / deltaX;
double tangRad = Math.atan(tang);
double tangGrau = tangRad * 36 / 2 * Math.PI;
return tangGrau;
```

doubleangle(double px, double py, double qx, double qy) angle

```java title=Example.java
double deltaX = px - qx;
double deltaY = py - qy;
double angleInDegrees = Math.atan2(deltaY, deltaX) * 180 / Math.PI;
return angleInDegrees;
```

doubleangle(double x1, double y1, double x2, double y2) Calculates angle formed by line from (x1,y1) to (x2,y2)

```java title=Example.java
double dely = y2 - y1;
double delx = x2 - x1;
if ((delx == 0.0) && (dely == 0.0)) {
    return 0;
returnMath.atan(dely / delx);
```

doubleangle(double x1, double y1, double x2, double y2) angle

```java title=Example.java
returnMath.atan2(y2 - y1, x2 - x1);
```

doubleangle(double x1, double y1, double x2, double y2) Returns the clockwise angle in radians to the y axis of the line from x1, y1 to x2, y2

```java title=Example.java
double xdiff = x1 - x2;
double ydiff = y1 - y2;
double angle;
if (xdiff == 0.0d && ydiff == 0.0d) {
    angle = -1.0d;
} else {
    if (xdiff <= 0.0d) {
        if (xdiff == 0.0d) {
...
```

doubleangle(double[] vec1, double[] vec2) angle

```java title=Example.java
double small, undefined, magv1, magv2, temp;
small = 0.00000001;
undefined = 999999.1;
magv1 = mag(vec1);
magv2 = mag(vec2);
if (magv1 * magv2 > small * small) {
    temp = dot(vec1, vec2) / (magv1 * magv2);
    if (Math.abs(temp) > 1.0) {
...
```

doubleangle(float x, float y, float x1, float y1) angle

```java title=Example.java
returnMath.atan((y1 - y) / (x1 - x)) + (x1 < x ? Math.PI : 0);
```

floatangle(float x1, float y1, float x2, float y2) Angle between 2 points.

```java title=Example.java
return (float) Math.toDegrees(Math.atan2(x2 - x1, y2 - y1));
```

doubleangle2degree(double angle) angledegree

```java title=Example.java
double w = -(angle * 180d / Math.PI);
if (w < 0) {
    w += 360;
return w;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
