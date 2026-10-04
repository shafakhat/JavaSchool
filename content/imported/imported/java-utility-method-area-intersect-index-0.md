---
title: Java Utililty Methods Area Intersect
nav: Java Utililty Methods Area...
description: The list of methods to do Area Intersect are organized into topic(s).
section: Imported - java2s Archive
order: 50025
source: https://www.java2s.com/example/java-utility-method/area-intersect-index-0.html
---
List of utility methods to do Area Intersect

## Description

The list of methods to do Area Intersect are organized into topic(s).

## Method

booleanintersection(Area a1, Area a2) Check whether the two provided areas intersect one another.

```java title=Example.java
Area copy = newArea(a1);
copy.intersect(a2);
return !copy.isEmpty();
```

booleanintersects(Area a, Area b) intersects

```java title=Example.java
Area a2 = (Area) a.clone();
a2.intersect(b);
return !a2.isEmpty();
```

booleanintersects(Area lhs, Area rhs) intersects

```java title=Example.java
if (lhs == null || lhs.isEmpty() || rhs == null || rhs.isEmpty()) {
    return false;
if (!lhs.getBounds().intersects(rhs.getBounds())) {
    return false;
Area newArea = newArea(lhs);
newArea.intersect(rhs);
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
