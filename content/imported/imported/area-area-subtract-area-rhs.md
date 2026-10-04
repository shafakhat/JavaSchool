---
title: Java Swing Tutorial - Java Area.subtract(Area rhs)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Area.subtract(Area rhs) method.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Area/0500__Area.subtract_Area_rhs_.htm
---
```java title=Example.java
Back to Area  ↑
```

## Syntax

Area.subtract(Area rhs) has the following syntax.

```java title=Example.java
publicvoid subtract(Area rhs)
```

## Example

In the following code shows how to use Area.subtract(Area rhs) method.

```java title=Example.java
/*fromwww.java2s.com*/import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
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

- Back to Area ↑
