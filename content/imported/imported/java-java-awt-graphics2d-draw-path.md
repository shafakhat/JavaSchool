---
title: Java AWT Graphics2D draw path
nav: Java AWT Graphics2D draw p...
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20133
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-path.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw path

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.Path2D;
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

    //Path2D (IceCream shape)Path2D path = newPath2D.Float();
    path.moveTo(50, 150);
    path.quadTo(100, 50, 150, 150);
    path.lineTo(50, 150);
    path.lineTo(100, 150 + 125);
    path.lineTo(150, 150);
    path.closePath();

    g2d.draw(path);
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

- Java AWT Graphics2D draw image
- Java AWT Graphics2D draw line
- Java AWT Graphics2D draw line with Line2D
- Java AWT Graphics2D draw quad curve
- Java AWT Graphics2D draw rectangle with Rectangle2D
