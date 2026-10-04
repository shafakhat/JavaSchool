---
title: Java AWT Graphics2D draw round rectangle with RoundRectangle2D
nav: Java AWT Graphics2D draw r...
description: Java AWT Graphics2D draw round rectangle with RoundRectangle2D
section: Imported
order: 20136
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-round-rectangle-with-roundrectangle2d.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw round rectangle with RoundRectangle2D

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
  @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    // Blue line
    g2d.setPaint(Color.BLUE);
    //RoundRectangle2D
    RoundRectangle2D roundRect = new RoundRectangle2D.Float(50, 50, 100, 70, 20, 20);
    g2d.draw(roundRect);

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

- Java AWT Graphics2D draw path
- Java AWT Graphics2D draw quad curve
- Java AWT Graphics2D draw rectangle with Rectangle2D
- Java AWT Graphics2D draw shadow
- Java AWT Graphics2D draw String
