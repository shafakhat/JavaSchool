---
title: Java Swing Tutorial - Java CubicCurve2D.getCtrlY2()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use CubicCurve2D.getCtrlY2() method.
section: Imported - java2s Archive
order: 1259
source: https://web.archive.org/web/20150325033943/http://www.java2s.com/Tutorials/Java/java.awt.geom/CubicCurve2D/0280__CubicCurve2D.getCtrlY2_.htm
---
## Syntax

CubicCurve2D.getCtrlY2() has the following syntax.

```java title=Example.java
public abstract double getCtrlY2()
```

## Example

In the following code shows how to use CubicCurve2D.getCtrlY2() method.

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.CubicCurve2D;
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
    System.out.println(cubcurve.getCtrlY2());
  }
}
java title=Example.java
```
