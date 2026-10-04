---
title: Java AWT Arc2D class
nav: Java AWT Arc2D class
description: @Override/*fromwww.java2s.com*/publicvoid paintComponent(Graphics g) {
section: Imported
order: 20046
source: http://www.java2s.com/ref/java/java-awt-arc2d-class.html
---
- java.awt.geom
- java.awt.geom Arc2D Area CubicCurve2D Ellipse2D GeneralPath Line2D Path2D Point2D QuadCurve2D Rectangle2D RoundRectangle2D

## Description

Java AWT Arc2D class

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Arc2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override/*fromwww.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g; // cast g to Graphics2D// draw 2D pie-shaped arc in white
    g2d.setPaint(Color.WHITE);
    g2d.setStroke(newBasicStroke(6.0f));
    g2d.draw(new Arc2D.Double(240, 30, 75, 100, 0, 270, Arc2D.PIE));
  }

  publicstaticvoid main(String[] args) {
    JFrame frame = newJFrame("Drawing 2D shapes");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Main Main = new Main();
    frame.add(Main);
    frame.setSize(425, 200);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT TextAttribute set text color
- Java AWT TextAttribute set under line
- Java AWT TextLayout layout multiple lines of text
- Java AWT Arc2D set type to CHORD
- Java AWT Arc2D set type to open
