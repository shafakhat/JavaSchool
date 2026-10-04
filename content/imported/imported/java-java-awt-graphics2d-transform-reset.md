---
title: Java AWT Graphics2D transform reset
nav: Java AWT Graphics2D transf...
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20150
source: http://www.java2s.com/ref/java/java-awt-graphics2d-transform-reset.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D transform reset

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.Stroke;
import java.awt.geom.AffineTransform;
import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
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
    Stroke solidStroke = newBasicStroke(10, BasicStroke.CAP_ROUND,
            BasicStroke.JOIN_ROUND);
    g2d.setStroke(solidStroke);
    g2d.draw(newLine2D.Float(newPoint2D.Float(200, 10),
            newPoint2D.Double(10, 210)));

    AffineTransform origTransform = g2d.getTransform();

    g2d.translate(100, 100);

    // reset transform
    g2d.setTransform(origTransform);

    g2d.draw(newLine2D.Float(newPoint2D.Float(200, 10),
        newPoint2D.Double(10, 210)));

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

- Java AWT Graphics2D set paint to TexturePaint
- Java AWT Graphics2D set radial gradient paint
- Java AWT Graphics2D set stroke to BasicStroke
- Java AWT Graphics2D transform rotate
- Java AWT Graphics2D transform scale
