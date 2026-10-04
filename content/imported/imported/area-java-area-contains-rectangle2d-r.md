---
title: Java Tutorial - Java Area.contains(Rectangle2D r)
nav: Java Tutorial - Java Area....
description: In the following code shows how to use Area.contains(Rectangle2D r) method.
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Area/Java_Area_contains_Rectangle2D_r_.htm
---
Next »Area (4176/9945)« Previous

### Syntax

Area.contains(Rectangle2D r) has the following syntax.

```java title=Example.java
publicboolean contains(Rectangle2D r)
```

### Example

In the following code shows how to use Area.contains(Rectangle2D r) method.

```java title=Example.java
//fromwww.java2s.comimport java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.geom.Area;
import java.awt.geom.Ellipse2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extends JPanel {

  publicvoid paint(Graphics g) {
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

    System.out.println(a1.contains(new Rectangle(50,50,5,5)));
  }

  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200,200);
    frame.setVisible(true);
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt.geom »

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
