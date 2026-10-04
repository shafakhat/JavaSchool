---
title: Java Utililty Methods Angle from Point
nav: Java Utililty Methods Angl...
description: The list of methods to do Angle from Point are organized into topic(s).
section: Imported - java2s Archive
order: 50022
source: https://www.java2s.com/example/java-utility-method/angle-from-point-index-0.html
---
List of utility methods to do Angle from Point

## Description

The list of methods to do Angle from Point are organized into topic(s).

## Method

doublegetAngle(double originX, double originY, double x, double y) The getAngle method returns the angle between (x, y) and (originX, originY).

```java title=Example.java
double adj = x - originX;
double opp = y - originY;
double rad = 0.0;
if (adj == 0) {
    if (opp == 0) {
        return 0.0;
    } else {
        rad = Math.PI / 2;
...
```

doublegetAngle(Point2D center, Point2D point) get Angle

```java title=Example.java
returnMath.atan2(-(point.getY() - center.getY()), point.getX() - center.getX());
```

doublegetAngle(Point2D origin, Point2D target) get Angle

```java title=Example.java
double angle = Math.toDegrees(Math.atan2((origin.getY() - target.getY()), (target.getX() - origin.getX())));
if (angle < 0) {
    angle += 360;
return angle;
```

doublegetAngle(Point2D p1, Point2D p2) get Angle

```java title=Example.java
if (p1.equals(p2)) {
    thrownewIllegalArgumentException();
double a = -Math.atan2(p2.getY() - p1.getY(), p2.getX() - p1.getX());
a = a * 180.0 / Math.PI;
a -= 90;
if (a >= 360.0) {
    a -= 360.0;
...
```

doublegetAngle(Point2D startPosition, Point2D endPosition) get Angle

```java title=Example.java
double deltaX = endPosition.getX() - startPosition.getX();
double deltaY = endPosition.getY() - startPosition.getY();
returnMath.atan2(deltaY, deltaX);
```

doublegetAngle(Point2D.Double vertPt, Point2D.Double edgePt) get Angle

```java title=Example.java
double dx = Math.abs(edgePt.x - vertPt.x), dy = Math.abs(edgePt.y - vertPt.y);
if (dx == 0.0D) {
    if (edgePt.y > vertPt.y)
        returnMath.PI / 2.0D;
    elsereturn 3 * Math.PI / 2.0D;
} elseif (dy == 0.0D) {
    if (edgePt.x > vertPt.x)
...
```

doublegetAngleForPoint(Arc2D arc, int x, int y) get Angle For Point

```java title=Example.java
double px = x - arc.getCenterX();
double py = arc.getCenterY() - y;
double d = Math.sqrt(px * px + py * py);
double a1 = Math.toDegrees(Math.acos(px / d));
double a2 = Math.toDegrees(Math.asin(py / d));
if (a2 < 0) {
    if (a1 > 90)
        return 360 - a1;
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
