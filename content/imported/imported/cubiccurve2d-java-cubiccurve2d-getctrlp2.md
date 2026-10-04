---
title: Java Tutorial - Java CubicCurve2D.getCtrlP2()
nav: Java Tutorial - Java Cubic...
description: In the following code shows how to use CubicCurve2D.getCtrlP2() method.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/Java_CubicCurve2D_getCtrlP2_.htm
---
Next »CubicCurve2D (4199/9945)« Previous

### Syntax

CubicCurve2D.getCtrlP2() has the following syntax.

```java title=Example.java
publicabstract Point2D getCtrlP2()
```

### Example

In the following code shows how to use CubicCurve2D.getCtrlP2() method.

```java title=Example.java
/*www.java2s.com*/import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.CubicCurve2D;

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

    System.out.println(cubcurve.getCtrlP2());
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt.geom »

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
