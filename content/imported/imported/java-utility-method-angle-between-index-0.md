---
title: Java Utililty Methods Angle Between
nav: Java Utililty Methods Angl...
description: The list of methods to do Angle Between are organized into topic(s).
section: Imported - java2s Archive
order: 50019
source: https://www.java2s.com/example/java-utility-method/angle-between-index-0.html
---
List of utility methods to do Angle Between

## Description

The list of methods to do Angle Between are organized into topic(s).

## Method

doubleangle2DBetween(double[] coord1, double[] coord2) Calculates the angle between two coordinates in degrees.

```java title=Example.java
if (coord1.length != coord2.length && coord1.length != 2)
    thrownewIllegalArgumentException("Number of dimensions is not valid for the provided coordinates");
double xDiff = coord2[0] - coord1[0];
double yDiff = coord2[1] - coord1[1];
double angle = Math.toDegrees(Math.atan2(yDiff, xDiff)) - 180;
return angle;
```

doubleangle_between(double x1, double y1, double z1, double x2, double y2, double z2) Calculate the angle between two vectors in three dimensions.

```java title=Example.java
double magnitude1 = StrictMath.sqrt((x1 * x1) + (y1 * y1) + (z1 * z1));
double magnitude2 = StrictMath.sqrt((x2 * x2) + (y2 * y2) + (z2 * z2));
double dotProduct = ((x1 * x2) + (y1 * y2) + (z1 * z2));
return (StrictMath.acos(dotProduct / (magnitude1 * magnitude2)));
```

doubleangleBetween(double[] v1, double[] v2) Determine the angle of rotation between two vectors.

```java title=Example.java
double m1 = mag(v1);
double m2 = mag(v2);
double ang = dot(v1, v2) / (m1 * m2);
ang = Math.acos(ang);
return ang;
```

doubleangleBetween(final double ax, final double ay, final double bx, final double by) Return the angle in radians between the 2d vectors defined by the parameters.

```java title=Example.java
return normaliseAngle(Math.atan2(ay, ax) - Math.atan2(by, bx));
```

doubleangleBetween2Lines(double l1x1, double l1y1, double l1x2, double l1y2, double l2x1, double l2y1, double l2x2, double l2y2) angle Between Lines

```java title=Example.java
double angle1 = Math.atan2(l1y1 - l1y2, l1x1 - l1x2);
double angle2 = Math.atan2(l2y1 - l2y2, l2x1 - l2x2);
return angle1 - angle2;
```

doubleangleBetween2LinesVectorAlgebra(double x11, double y11, double x12, double y12, double x21, double y21, double x22, double y22) angle Between Lines Vector Algebra

```java title=Example.java
double[] u = { x12 - x11, y12 - y11 };
double[] v = { x22 - x21, y22 - y21 };
double cosa = Math.abs(u[0] * v[0] + u[1] * v[1])
        / Math.sqrt((u[0] * u[0] + u[1] * u[1]) * (v[0] * v[0] + v[1] * v[1]));
returnMath.acos(cosa);
```

doubleAngleBetweenDegrees(double longitudeFirstBody, double latitudeFirstBody, double longitudeSecondBody, double latitudeSecondBody) Angle Between Degrees

```java title=Example.java
double[] vectorFirst = latLonToVector(longitudeFirstBody, latitudeFirstBody);
double[] vectorSecond = latLonToVector(longitudeSecondBody, latitudeSecondBody);
double dotproduct = vectorDotProduct(vectorFirst[0], vectorFirst[1], vectorFirst[2], vectorSecond[0],
        vectorSecond[1], vectorSecond[2]);
double absoluteFirst = vectorAbsoluteValue(vectorFirst[0], vectorFirst[1], vectorFirst[2]);
double absoluteSecond = vectorAbsoluteValue(vectorSecond[0], vectorSecond[1], vectorSecond[2]);
double angleResult = Math.acos(dotproduct / (absoluteFirst * absoluteSecond));
return angleResult;
...
```

doubleangleBetweenPoints(double ax, double ay, double bx, double by) angle Between Points

```java title=Example.java
double angle = 0;
if (bx - ax == 0) {
    if (by > ay)
        angle = -90;
    else
        angle = 90;
} else
    angle = Math.atan((by - ay) / (bx - ax)) * 180.0 / Math.PI;
...
```

doubleAngleBetweenVectors(double X1, double Y1, double Z1, double X2, double Y2, double Z2) Angle Between Vectors

```java title=Example.java
double dotproduct = vectorDotProduct(X1, Y1, Z1, X2, Y2, Z2);
double absoluteFirst = vectorAbsoluteValue(X1, Y1, Z1);
double absoluteSecond = vectorAbsoluteValue(X2, Y2, Z2);
double angleResult = Math.acos(dotproduct / (absoluteFirst * absoluteSecond));
return angleResult;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
