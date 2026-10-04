---
title: Java java.awt.geom.Ellipse2D
nav: Java java.awt.geom.Ellipse2D
description: The Ellipse2D class describes an ellipse that is defined by a framing rectangle. This class is only the abstract superclass for all objects which store a 2D ellipse. The
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Ellipse2D/Java_java_awt_geom_Ellipse2D.htm
---
Next »1164/7083« Previous

In this chapter you will learn:

- Get to know java.awt.geom.Ellipse2D
- JDK Version for java.awt.geom.Ellipse2D
- Constructors from java.awt.geom.Ellipse2D
- Methods from java.awt.geom.Ellipse2D

### Description

The Ellipse2D class describes an ellipse that is defined by a framing rectangle. This class is only the abstract superclass for all objects which store a 2D ellipse. The actual storage representation of the coordinates is left to the subclass.

### Since

```java title=Example.java
1.2
```

### Constructor

Constructor and Description
Ellipse2D() This is an abstract class that cannot be instantiated directly.

### Method

Modifier and Type  Method and Description
---  ---
boolean  contains(double x, double y) Tests if the specified coordinates are inside the boundary of the Shape , as described by the definition of insideness .
boolean  contains(double x, double y, double w, double h) Tests if the interior of the Shape entirely contains the specified rectangular area.
boolean  equals(Object obj) Determines whether or not the specified Object is equal to this Ellipse2D .
PathIterator  getPathIterator(AffineTransform at) Returns an iteration object that defines the boundary of this Ellipse2D .
int  hashCode() Returns the hashcode for this Ellipse2D .
boolean  intersects(double x, double y, double w, double h) Tests if the interior of the Shape intersects the interior of a specified rectangular area.

#### Next chapter...

What you will learn in the next chapter:

- Get to know Ellipse2D.Ellipse2D()
- Syntax for Ellipse2D() constructor from Ellipse2D
- Example - Ellipse2D.Ellipse2D()

Next »« PreviousHome » Java Tutorial » java.awt.geom » Ellipse2DJava java.awt.geom.Ellipse2DJava Ellipse2D() Constructor Java Ellipse2D.contains(double x, double y... Java Ellipse2D.contains(double x, double y... Java Ellipse2D.equals(Object obj) Java Ellipse2D .getPathIterator (AffineTran... Java Ellipse2D.hashCode() Java Ellipse2D.intersects(double x, doubl...
