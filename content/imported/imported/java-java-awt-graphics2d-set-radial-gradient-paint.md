---
title: Java AWT Graphics2D set radial gradient paint
nav: Java AWT Graphics2D set ra...
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20148
source: http://www.java2s.com/ref/java/java-awt-graphics2d-set-radial-gradient-paint.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D set radial gradient paint

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RadialGradientPaint;
import java.awt.RenderingHints;
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

    //Ellipse2D
    Ellipse2D ellipse = new Ellipse2D.Float(50, 50, 100, 70);

    float[] dists = { .3f, 1.0f};
    Color[] colors = {Color.RED, Color.BLACK};
    RadialGradientPaint gradient1 = newRadialGradientPaint(50, 50, 100, dists, colors);
    g2d.setPaint(gradient1);
    g2d.fill(ellipse);

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

- Java AWT Graphics2D set linear gradient paint
- Java AWT Graphics2D set paint to red color
- Java AWT Graphics2D set paint to TexturePaint
- Java AWT Graphics2D set stroke to BasicStroke
- Java AWT Graphics2D transform reset
