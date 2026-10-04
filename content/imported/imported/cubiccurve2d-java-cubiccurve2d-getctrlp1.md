---
title: Java Tutorial - Java CubicCurve2D.getCtrlP1()
nav: Java Tutorial - Java Cubic...
description: In the following code shows how to use CubicCurve2D.getCtrlP1() method.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/Java_CubicCurve2D_getCtrlP1_.htm
---
Next »CubicCurve2D (4198/9945)« Previous

### Syntax

CubicCurve2D.getCtrlP1() has the following syntax.

```java title=Example.java
publicabstract Point2D getCtrlP1()
```

### Example

In the following code shows how to use CubicCurve2D.getCtrlP1() method.

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.CubicCurve2D;
//www.java2s.compublicclass Main extends Frame {
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

    System.out.println(cubcurve.getCtrlP1());
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt.geom »

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
