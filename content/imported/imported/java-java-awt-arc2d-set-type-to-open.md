---
title: Java AWT Arc2D set type to open
nav: Java AWT Arc2D set type to...
description: @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
section: Imported
order: 20048
source: http://www.java2s.com/ref/java/java-awt-arc2d-set-type-to-open.html
---
- java.awt.geom
- java.awt.geom Arc2D Area CubicCurve2D Ellipse2D GeneralPath Line2D Path2D Point2D QuadCurve2D Rectangle2D RoundRectangle2D

## Description

Java AWT Arc2D set type to open

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.Arc2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();
  @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.BLACK);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    // 3 thickness
    g2d.setStroke(newBasicStroke(3));

    // Arc with open type
    Arc2D arc = new Arc2D.Float(50, // x coordinate
            50,                     // y coordinate
            100,                    // bounds width
            100,                    // bounds height
            45,                     // start angle in degrees
            270,                    // degrees plus start angle
            Arc2D.OPEN              // Open type arc
    );
    g2d.draw(arc);
  }

  publicstaticvoid main(String[] args) {
    // create frame for MainJFrame frame = newJFrame("java2s.com");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    Main Main = new Main();
    frame.add(Main);
    frame.setSize(300, 210);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT TextLayout layout multiple lines of text
- Java AWT Arc2D class
- Java AWT Arc2D set type to CHORD
- Java AWT Arc2D set type to PIE
- Java AWT Area subtract
