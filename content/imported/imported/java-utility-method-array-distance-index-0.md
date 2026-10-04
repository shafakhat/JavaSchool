---
title: Java Utililty Methods Array Distance
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Distance are organized into topic(s).
section: Imported - java2s Archive
order: 50056
source: https://www.java2s.com/example/java-utility-method/array-distance-index-0.html
---
List of utility methods to do Array Distance

## Description

The list of methods to do Array Distance are organized into topic(s).

## Method

DoublefindMaxDistance24(Double[] quad2, Double[] quad4) Finds the maximum separation between two points that are in quadrant2 and quadrant4.

```java title=Example.java
if (quad2.length == 0 || quad4.length == 0) {
    angleZero = Double.NaN;
    angleMax = Double.NaN;
    return UNDEFINED;
return findMaxDistance13(quad2, quad4);
```

DoublefindMaxDistanceAA(Double[] quadA) Finds the maximum separation between two points that are in the same quadrant.

```java title=Example.java
if (quadA.length == 0) {
    angleZero = Double.NaN;
    angleMax = Double.NaN;
    return UNDEFINED;
Double maxDistance = UNDEFINED;
angleZero = quadA[0].doubleValue();
angleMax = quadA[quadA.length - 1].doubleValue();
...
```
