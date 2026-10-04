---
title: Java Tutorial - Java Ellipse2D.contains(double x, double y)
nav: Java Tutorial - Java Ellip...
description: Ellipse2D.contains(double x, double y) has the following syntax.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Ellipse2D/Java_Ellipse2D_contains_double_x_double_y_.htm
---
Next »Ellipse2D (4213/9945)« Previous

### Syntax

Ellipse2D.contains(double x, double y) has the following syntax.

```java title=Example.java
publicboolean contains(double x,  double y)
```

### Example

In the following code shows how to use Ellipse2D.contains(double x, double y) method.

```java title=Example.java
/*fromwww.java2s.com*/import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;

publicclass Main {

  publicstaticvoid main(String args[]) {
    Ellipse2D.Double e = new Ellipse2D.Double(1.0,2.0,2.0,2.0);

    e.contains(20.0,20.0);
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt.geom »

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
