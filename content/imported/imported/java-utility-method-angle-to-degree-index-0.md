---
title: Java Utililty Methods Angle to Degree
nav: Java Utililty Methods Angl...
description: The list of methods to do Angle to Degree are organized into topic(s).
section: Imported - java2s Archive
order: 50024
source: https://www.java2s.com/example/java-utility-method/angle-to-degree-index-0.html
---
List of utility methods to do Angle to Degree

## Description

The list of methods to do Angle to Degree are organized into topic(s).

## Method

floattoDegree(double angle) to Degree

```java title=Example.java
return (float) Math.toDegrees(angle);
```

doubletoDegrees(final double angle) Returns angle converted into degrees.

```java title=Example.java
return angle * 180 / Math.PI;
```

floattoDegrees(float angle) to Degrees

```java title=Example.java
return (float) 180 / (float) Math.PI * angle;
```

doubletoDegrees(int val) Convert an angle in map units to degrees.

```java title=Example.java
return (double) val * (360.0 / (1 << 24));
```

doubletoDegrees(Short angrad) To degrees.

```java title=Example.java
returnMath.toDegrees(angrad.doubleValue());
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
