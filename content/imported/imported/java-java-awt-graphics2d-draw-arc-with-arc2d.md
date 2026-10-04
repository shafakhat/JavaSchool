---
title: Java AWT Graphics2D draw arc with Arc2D
nav: Java AWT Graphics2D draw a...
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20131
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-arc-with-arc2d.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw arc with Arc2D

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
  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
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

- Java AWT Graphics create paint application
- Java AWT Graphics2D class
- Java AWT Graphics2D clear rectangle
- Java AWT Graphics2D draw cubic curve
- Java AWT Graphics2D draw dashed line
