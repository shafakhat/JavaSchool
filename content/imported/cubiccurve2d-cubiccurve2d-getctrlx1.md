---
title: Java Swing Tutorial - Java CubicCurve2D.getCtrlX1()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use CubicCurve2D.getCtrlX1() method.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/0220__CubicCurve2D.getCtrlX1_.htm
---
```java title=Example.java
Back to CubicCurve2D  ↑
```

## Syntax

CubicCurve2D.getCtrlX1() has the following syntax.

```java title=Example.java
publicabstractdouble getCtrlX1()
```

## Example

In the following code shows how to use CubicCurve2D.getCtrlX1() method.

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
    System.out.println(cubcurve.getCtrlX1());
  }
}
```

The code above generates the following result.

- Back to CubicCurve2D ↑
