---
title: Java AWT Graphics2D draw cubic curve
nav: Java AWT Graphics2D draw c...
description: @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
section: Imported
order: 20135
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-cubic-curve.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw cubic curve

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.CubicCurve2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();

  @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    //CubicCurve2D
    CubicCurve2D cubicCurve = new CubicCurve2D.Float(
            50, 75,            // start pt (x1,y1)
            50+30, 75-100,     // control pt1
            50+60, 75+100,     // control pt2
            50+90, 75          // end pt (x2,y2)
    );

    g2d.draw(cubicCurve);
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

- Java AWT Graphics2D class
- Java AWT Graphics2D clear rectangle
- Java AWT Graphics2D draw arc with Arc2D
- Java AWT Graphics2D draw dashed line
- Java AWT Graphics2D draw ellipse with Ellipse2D
