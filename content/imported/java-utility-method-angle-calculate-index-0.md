---
title: Java Utililty Methods Angle Calculate
nav: Java Utililty Methods Angl...
description: The list of methods to do Angle Calculate are organized into topic(s).
section: Imported - java2s Archive
order: 50020
source: https://www.java2s.com/example/java-utility-method/angle-calculate-index-0.html
---
List of utility methods to do Angle Calculate

## Description

The list of methods to do Angle Calculate are organized into topic(s).

## Method

doubleangle(Point2D from, Point2D to) angle

```java title=Example.java
Point2D delta = subtract(from, to);
returnMath.atan2(delta.getY(), delta.getX());
```

doubleangle(Point2D.Double vec) Computes "angle" of a vector using the

```java title=Example.java
Math.atan
```

method.

```java title=Example.java
if (Double.isInfinite(vec.x)) {
    return vec.y > PI ? vec.y - 2 * PI : vec.y;
return atan2(vec.y, vec.x);
```

doubleangle2D(Point p1, Point p2) angle D

```java title=Example.java
double dtheta = Math.atan2(p2.y, p2.x) - Math.atan2(p1.y, p1.x);
while (dtheta > Math.PI) {
    dtheta -= 2.0 * Math.PI;
while (dtheta < -1.0 * Math.PI) {
    dtheta += 2.0 * Math.PI;
return dtheta;
...
```

doubleangleBetween(Point2D.Double vec1, Point2D.Double vec2) Computes angle between two vectors, as comptued by the dot product formula

```java title=Example.java
returnMath.acos(dotProduct(vec1, vec2) / (magnitude(vec1) * magnitude(vec2)));
```

doubleangleOf(Point2D a, Point2D b) Calculates the radian angle from point a to point b .

```java title=Example.java
double x = b.getX() - a.getX();
double y = b.getY() - a.getY();
returnMath.atan2(y, x);
```

doubleanglePI(Point2D top, Point2D corner1, Point2D corner2) Calculate the value of the angle [0,PI).

```java title=Example.java
double x1 = corner1.getX() - top.getX();
double x2 = corner2.getX() - top.getX();
double y1 = corner1.getY() - top.getY();
double y2 = corner2.getY() - top.getY();
returnMath.acos((x1 * x2 + y1 * y2) / Math.sqrt((x1 * x1 + y1 * y1) * (x2 * x2 + y2 * y2)));
```

PointangleToPoint(Rectangle r, double angle) angle To Point

```java title=Example.java
double si = Math.sin(angle);
double co = Math.cos(angle);
double e = 1.0E-4D;
int x = 0;
int y = 0;
if (Math.abs(si) > e) {
    x = (int) ((1.0D + co / Math.abs(si)) / 2.0D * (double) r.width);
    x = range(0, r.width, x);
...
```

doublecalculateAngle(double dx, double dy) calculate Angle

```java title=Example.java
double alpha;
if (Math.abs(dx) > Math.abs(dy)) {
    double tg = dy / dx;
    alpha = Math.atan(tg);
    if (dx < 0) {
        alpha += Math.PI;
} else {
...
```

floatcalculateAngle(float x, float y, float x1, float y1) From x,y -> x1,y1

```java title=Example.java
double angle = Math.atan2(y - y1, x - x1);
return (float) angle + 1.5f;
```

doublecalculateAngle(int a1, int b1, int a2, int b2) Calculates the angle between two points in 2D space

```java title=Example.java
double distance_between_a1_a2 = calculateDifference(a1, a2);
double distance_between_b1_b2 = calculateDifference(b1, b2);
returnMath.atan(distance_between_b1_b2 / distance_between_a1_a2);
```
