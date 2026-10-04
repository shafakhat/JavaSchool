---
title: Java Swing Tutorial - Java CubicCurve2D.getFlatness()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use CubicCurve2D.getFlatness() method.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/0300__CubicCurve2D.getFlatness_.htm
---
## Syntax

CubicCurve2D.getFlatness() has the following syntax.

```java title=Example.java
publicdouble getFlatness()
```

## Example

In the following code shows how to use CubicCurve2D.getFlatness() method.

```java title=Example.java
import java.awt.Frame;
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
    System.out.println(cubcurve.getFlatness());
  }
}
```

The code above generates the following result.
