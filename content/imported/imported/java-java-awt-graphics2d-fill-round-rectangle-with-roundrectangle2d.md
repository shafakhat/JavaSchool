---
title: Java AWT Graphics2D fill round rectangle with RoundRectangle2D
nav: Java AWT Graphics2D fill r...
description: Java AWT Graphics2D fill round rectangle with RoundRectangle2D
section: Imported
order: 20144
source: http://www.java2s.com/ref/java/java-awt-graphics2d-fill-round-rectangle-with-roundrectangle2d.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D fill round rectangle with RoundRectangle2D

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.RoundRectangle2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();
  @Override/*fromwww.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    RoundRectangle2D roundRect = new RoundRectangle2D.Float(50, 50, 100, 70, 20, 20);
    g2d.setPaint(Color.BLACK);
    g2d.draw(roundRect);
    g2d.setPaint(Color.GREEN);
    g2d.fill(roundRect);

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

- Java AWT Graphics2D draw with mouse
- Java AWT Graphics2D fill area
- Java AWT Graphics2D fill rectangle with Rectangle2D
- Java AWT Graphics2D fill Shape
- Java AWT Graphics2D get font metrics
