---
title: Java Utililty Methods Angle Reduce
nav: Java Utililty Methods Angl...
description: The list of methods to do Angle Reduce are organized into topic(s).
section: Imported - java2s Archive
order: 50023
source: https://www.java2s.com/example/java-utility-method/angle-reduce-index-0.html
---
List of utility methods to do Angle Reduce

## Description

The list of methods to do Angle Reduce are organized into topic(s).

## Method

doublereduceAngle(double theta) reduce Angle

```java title=Example.java
theta %= TWOPI;
if (Math.abs(theta) > PI) {
    theta = theta - TWOPI;
if (Math.abs(theta) > HALF_PI) {
    theta = PI - theta;
return theta;
...
```

doublereduceAngle(double theta) reduce Angle

```java title=Example.java
theta %= TWO_PI;
if (Math.abs(theta) > PI) {
    theta = theta - TWO_PI;
if (Math.abs(theta) > HALF_PI) {
    theta = PI - theta;
return theta;
...
```

floatreduceAngle(float angle) Reduces the given angle to its equivalent angle between -pi and pi.

```java title=Example.java
return loop(angle, -PI, PI);
```

floatreduceAngle(float theta) Reduces the given angle into the -PI/4 ...

```java title=Example.java
theta %= TWO_PI;
if (abs(theta) > PI) {
    theta = theta - TWO_PI;
if (abs(theta) > HALF_PI) {
    theta = PI - theta;
return theta;
...
```
