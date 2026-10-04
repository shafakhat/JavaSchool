---
title: Java CubicCurve2D.contains(double x, double y)
nav: Java CubicCurve2D.contains...
description: CubicCurve2D contains(double x, double y) tests if the specified coordinates are inside the boundary of the Shape , as described by the definition of insideness .
section: Imported - java2s Archive
order: 1271
source: https://web.archive.org/web/20140328011416/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/Java_CubicCurve2D_contains_double_x_double_y_.htm
---
In this chapter you will learn:

- Get to know CubicCurve2D.contains(double x, double y)
- Syntax for CubicCurve2D.contains(double x, double y)
- Parameter for CubicCurve2D.contains(double x, double y)
- Returns for CubicCurve2D.contains(double x, double y)
- Example - CubicCurve2D.contains(double x, double y)

### Description

CubicCurve2D contains(double x, double y) tests if the specified coordinates are inside the boundary of the Shape , as described by the definition of insideness .

### Syntax

CubicCurve2D.contains(double x, double y) has the following syntax.

```java title=Example.java
public boolean contains(double x,  double y)
```

### Parameters

CubicCurve2D.contains(double x, double y) has the following parameters.

- x - the specified X coordinate to be tested
- y - the specified Y coordinate to be tested

### Returns

CubicCurve2D.contains(double x, double y) method returns true if the specified coordinates are inside the Shape boundary; false otherwise.

### Example

In the following code shows how to use CubicCurve2D.contains(double x, double y) method.

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.CubicCurve2D;
import java.awt.geom.Point2D;
public class Main extends Frame {
  public static void main(String[] args) {
    new Main().setVisible(true);
  }
  public Main () {
    setSize(400, 550);
  }
  public void paint(Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    CubicCurve2D cubcurve = new CubicCurve2D.Float(30, 400, 150, 400, 200, 500, 350, 450);
    g2d.draw(cubcurve);
    System.out.println(cubcurve.contains(0.2F, 0.3F));
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- Get to know CubicCurve2D.contains(Point2D p)
- Syntax for CubicCurve2D.contains(Point2D p)
- Parameter for CubicCurve2D.contains(Point2D p)
- Returns for CubicCurve2D.contains(Point2D p)
- Example - CubicCurve2D.contains(Point2D p)
