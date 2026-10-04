---
title: Java Swing Tutorial - Java CubicCurve2D.contains(double x, double y)
nav: Java Swing Tutorial - Java...
description: CubicCurve2D.contains(double x, double y) has the following syntax.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/0080__CubicCurve2D.contains_double_x_double_y_.htm
---
## Syntax

CubicCurve2D.contains(double x, double y) has the following syntax.

```java title=Example.java
publicboolean contains(double x,  double y)
```

## Example

In the following code shows how to use CubicCurve2D.contains(double x, double y) method.

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.CubicCurve2D;
import java.awt.geom.Point2D;
publicclass Main extends Frame {
  publicstaticvoid main(String[] args) {
    new Main().setVisible(true);
  }
  public Main () {
    setSize(400, 550);
  }
  publicvoid paint(Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    CubicCurve2D cubcurve = new CubicCurve2D.Float(30, 400, 150, 400, 200, 500, 350, 450);
    g2d.draw(cubcurve);
    System.out.println(cubcurve.contains(0.2F, 0.3F));
  }
}
```

The code above generates the following result.
