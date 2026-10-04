---
title: Java Utililty Methods Angle Difference
nav: Java Utililty Methods Angl...
description: The list of methods to do Angle Difference are organized into topic(s).
section: Imported - java2s Archive
order: 50021
source: https://www.java2s.com/example/java-utility-method/angle-difference-index-0.html
---
List of utility methods to do Angle Difference

## Description

The list of methods to do Angle Difference are organized into topic(s).

## Method

doubleangleDif(double a1, double a2) Compute the difference between two angles.

```java title=Example.java
doubleval = a1 - a2;
if (val > Math.PI) {
    val -= 2. * Math.PI;
if (val < -Math.PI) {
    val += 2. * Math.PI;
returnval;
...
```

floatangleDif(float a, float b) angle Dif

```java title=Example.java
if (b > a)
    return b - a > PI ? (float) (a + 2 * PI - b) : b - a;
return a - b > PI ? (float) (b + 2 * PI - a) : a - b;
```

floatangleDif(float a1, float a2) Compute the difference between two angles.

```java title=Example.java
doubleval = a1 - a2;
if (val > Math.PI) {
    val -= 2. * Math.PI;
if (val < -Math.PI) {
    val += 2. * Math.PI;
return (float) val;
...
```

doubleangleDiff(double a, double b) given two angels in radians, returns a difference in radians closest to zero such that a + angleDiff(a, b) represents b.

```java title=Example.java
return angleDiff(a, b, Math.PI * 2);
```

doubleangleDiff(double alpha, double beta) angle Diff

```java title=Example.java
double angleDiff = alpha - beta;
return ((((angleDiff) % (2 * Math.PI)) + (3 * Math.PI)) % (2 * Math.PI)) - Math.PI;
```

doubleangleDiff(double angle1, double angle2, boolean normalized) angle Diff

```java title=Example.java
if (!normalized) {
    angle1 = normalizeAngle(angle1);
    angle2 = normalizeAngle(angle2);
returnMath.min(Math.abs(angle1 - angle2),
        Math.min(Math.abs(angle1 - angle2 + TWO_PI), Math.abs(angle1 - angle2 - TWO_PI)));
```

doubleangleDiff(final double a1, final double a2) Get the difference of angles (radians) as given from angle(x,z), from a1 to a2, i.e.

```java title=Example.java
if (Double.isNaN(a1) || Double.isNaN(a1))
    returnDouble.NaN;
finaldouble diff = a2 - a1;
if (diff < -Math.PI)
    return diff + 2.0 * Math.PI;
elseif (diff > Math.PI)
    return diff - 2.0 * Math.PI;
else
...
```

floatangleDiff(float a, float b) Returns the smallest signed difference between the two given angles, from a to b.

```java title=Example.java
return reduceAngle(b - a);
```

intangleDiff(int ang1, int ang2) angle Diff

```java title=Example.java
int delta = ang2 - ang1;
delta %= ANGLE_2PI;
if (delta < 0)
    delta += ANGLE_2PI;
if (delta > ANGLE_PI)
    delta -= ANGLE_2PI;
return delta;
```

doubleangleDiff(int angle1, int angle2) angle Diff

```java title=Example.java
double diff = Math.abs(angle1 - angle2);
if (diff <= 180) {
    return diff;
} else {
    return 360 - diff;
```
