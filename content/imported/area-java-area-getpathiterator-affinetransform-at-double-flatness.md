---
title: Java Tutorial - Java Area .getPathIterator (AffineTransform at, double flatness)
nav: Java Tutorial - Java Area ...
description: Area.getPathIterator(AffineTransform at, double flatness) has the following syntax.
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20140830012843/http://www.java2s.com/Tutorials/Java/java.awt.geom/Area/Java_Area_getPathIterator_AffineTransform_at_double_flatness_.htm
---
### Syntax

Area.getPathIterator(AffineTransform at, double flatness) has the following syntax.

```java title=Example.java
public PathIterator getPathIterator(AffineTransform at,    double flatness)
```

### Example

In the following code shows how to use Area.getPathIterator(AffineTransform at, double flatness) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.awt.geom.Area;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    Ellipse2D e1 = new Ellipse2D.Double (20.0, 20.0, 80.0, 70.0);
    Ellipse2D e2 = new Ellipse2D.Double (20.0, 70.0, 40.0, 40.0);
    Area a1 = new Area (e1);
    Area a2 = new Area (e2);
    a1.subtract (a2);
    g2.setColor (Color.orange);
    g2.fill (a1);
    g2.setColor (Color.black);
    g2.drawString ("subtract", 20, 140);
    System.out.println(a1.getPathIterator(new AffineTransform(),0.5).getWindingRule());
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200,200);
    frame.setVisible(true);
  }
}
```

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
