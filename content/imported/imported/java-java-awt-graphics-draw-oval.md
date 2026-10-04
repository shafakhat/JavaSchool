---
title: Java AWT Graphics draw oval
nav: Java AWT Graphics draw oval
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20120
source: http://www.java2s.com/ref/java/java-awt-graphics-draw-oval.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics draw oval

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    this.setBackground(Color.WHITE);

    g.setColor(Color.MAGENTA);
    g.drawOval(15, 10, 90, 55);
    g.fillOval(20, 10, 90, 55);
  }

  publicstaticvoid main(String[] args) {
    // create frame for MainJFrame frame = newJFrame("Drawing ovals");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    Main Main = new Main();
    Main.setBackground(Color.WHITE);
    frame.add(Main);
    frame.setSize(400, 210);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT Graphics draw arc
- Java AWT Graphics draw line
- Java AWT Graphics draw lines with random location
- Java AWT Graphics draw Pie
- Java AWT Graphics draw Polygon
