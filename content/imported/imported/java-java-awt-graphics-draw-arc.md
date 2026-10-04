---
title: Java AWT Graphics draw arc
nav: Java AWT Graphics draw arc
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20119
source: http://www.java2s.com/ref/java/java-awt-graphics-draw-arc.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics draw arc

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    // start at 0 and sweep 360 degrees
    g.setColor(Color.RED);
    g.setColor(Color.BLACK);
    g.drawArc(15, 35, 80, 80, 0, 360);

    // start at 0 and sweep -270 degrees
    g.setColor(Color.RED);
    g.setColor(Color.BLACK);
    g.drawArc(15, 55, 80, 80, 0, -270);

    // start at 0 and sweep 360 degrees
    g.fillArc(15, 120, 80, 40, 0, 360);
  }

  publicstaticvoid main(String[] args) {
    // create frame for MainJFrame frame = newJFrame("Drawing Arcs");
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

- Java AWT GradientPaint
- Java AWT GradientPaint create
- Java AWT Graphics double buffer
- Java AWT Graphics draw line
- Java AWT Graphics draw lines with random location
