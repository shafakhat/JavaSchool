---
title: Java java.awt.geom.Area
nav: Java java.awt.geom.Area
description: An Area object stores and manipulates a resolution-independent description of an enclosed area of 2-dimensional space.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Area/Java_java_awt_geom_Area.htm
---
In this chapter you will learn:

- Get to know java.awt.geom.Area
- JDK Version for java.awt.geom.Area
- Constructors from java.awt.geom.Area
- Methods from java.awt.geom.Area

### Description

An Area object stores and manipulates a resolution-independent description of an enclosed area of 2-dimensional space.

Area objects can be transformed and can perform various Constructive Area Geometry (CAG) operations when combined with other Area objects.

The CAG operations include area addition , subtraction , intersection , and exclusive or . See the linked method documentation for examples of the various operations.

The Area class implements the Shape interface and provides full support for all of its hit-testing and path iteration facilities, but an Area is more specific than a generalized path in a number of ways: Only closed paths and sub-paths are stored.

### Since

```java title=Example.java
1.2
```

### Constructor

Constructor and Description
---
Area() Default constructor which creates an empty area.
Area(Shape s) The Area class creates an area geometry from the specified Shape object.

### Method

Modifier and Type  Method and Description
---  ---
void  add(Area rhs) Adds the shape of the specified Area to the shape of this Area .
Object  clone() Returns an exact copy of this Area object.
boolean  contains(double x, double y) Tests if the specified coordinates are inside the boundary of the Shape , as described by the definition of insideness .
boolean  contains(double x, double y, double w, double h) Tests if the interior of the Shape entirely contains the specified rectangular area.
boolean  contains(Point2D p) Tests if a specified Point2D is inside the boundary of the Shape , as described by the definition of insideness .
boolean  contains(Rectangle2D r) Tests if the interior of the Shape entirely contains the specified Rectangle2D .
Area  createTransformedArea(AffineTransform t) Creates a new Area object that contains the same geometry as this Area transformed by the specified AffineTransform .
boolean  equals(Area other) Tests whether the geometries of the two Area objects are equal.
void  exclusiveOr(Area rhs) Sets the shape of this Area to be the combined area of its current shape and the shape of the specified Area , minus their intersection.
Rectangle  getBounds() Returns a bounding Rectangle that completely encloses this Area .
Rectangle2D  getBounds2D() Returns a high precision bounding Rectangle2D that completely encloses this Area .
PathIterator  getPathIterator(AffineTransform at) Creates a PathIterator for the outline of this Area object.
PathIterator  getPathIterator(AffineTransform at, double flatness) Creates a PathIterator for the flattened outline of this Area object.
void  intersect(Area rhs) Sets the shape of this Area to the intersection of its current shape and the shape of the specified Area .
boolean  intersects(double x, double y, double w, double h) Tests if the interior of the Shape intersects the interior of a specified rectangular area.
boolean  intersects(Rectangle2D r) Tests if the interior of the Shape intersects the interior of a specified Rectangle2D .
boolean  isEmpty() Tests whether this Area object encloses any area.
boolean  isPolygonal() Tests whether this Area consists entirely of straight edged polygonal geometry.
boolean  isRectangular() Tests whether this Area is rectangular in shape.
boolean  isSingular() Tests whether this Area is comprised of a single closed subpath.
void  reset() Removes all of the geometry from this Area and restores it to an empty area.
void  subtract(Area rhs) Subtracts the shape of the specified Area from the shape of this Area .
void  transform(AffineTransform t) Transforms the geometry of this Area using the specified AffineTransform .

#### Next chapter...

What you will learn in the next chapter:

- Get to know Area.Area()
- Syntax for Area() constructor from Area
- Example - Area.Area()
