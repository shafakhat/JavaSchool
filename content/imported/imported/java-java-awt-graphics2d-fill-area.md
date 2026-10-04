---
title: Java AWT Graphics2D fill area
nav: Java AWT Graphics2D fill a...
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20141
source: http://www.java2s.com/ref/java/java-awt-graphics2d-fill-area.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D fill area

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.Area;
import java.awt.geom.Ellipse2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();

  @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    Ellipse2D bigCircle = new Ellipse2D.Float(50, 50, 100, 75);
    Ellipse2D smallCircle = new Ellipse2D.Float(80, 75, 35, 25);
    Area donut = newArea(bigCircle);
    Area donutHole = newArea(smallCircle);
    donut.subtract(donutHole);

    g2d.fill(donut);
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

- Java AWT Graphics2D draw String right alignment
- Java AWT Graphics2D draw styled String
- Java AWT Graphics2D draw with mouse
- Java AWT Graphics2D fill rectangle with Rectangle2D
- Java AWT Graphics2D fill round rectangle with RoundRectangle2D
