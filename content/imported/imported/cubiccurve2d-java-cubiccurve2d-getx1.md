---
title: Java Tutorial - Java CubicCurve2D.getX1()
nav: Java Tutorial - Java Cubic...
description: In the following code shows how to use CubicCurve2D.getX1() method.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/Java_CubicCurve2D_getX1_.htm
---
Next »CubicCurve2D (4207/9945)« Previous

### Syntax

CubicCurve2D.getX1() has the following syntax.

```java title=Example.java
publicabstractdouble getX1()
```

### Example

In the following code shows how to use CubicCurve2D.getX1() method.

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.CubicCurve2D;
/*www.java2s.com*/publicclass Main extends Frame {
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

    System.out.println(cubcurve.getX1());
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt.geom »

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
