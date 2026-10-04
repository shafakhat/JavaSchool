---
title: Java AWT Graphics draw Pie
nav: Java AWT Graphics draw Pie
description: Ellipse2D.Float pie = new Ellipse2D.Float(xInset, yInset, width, height);
section: Imported
order: 20125
source: http://www.java2s.com/ref/java/java-awt-graphics-draw-pie.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics draw Pie

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Arc2D;
import java.awt.geom.Ellipse2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

class PiePanel extendsJPanel {
  private PieSlice[] slice;
  privateint current = 0;
  privatefloat totalSize = 0;
  privateColor background;

  public PiePanel(int sliceCount) {
    slice = new PieSlice[sliceCount];
    background = getBackground();/*fromwww.java2s.com*/
  }

  publicvoid addSlice(Color sColor, float sSize) {
    if (current <= slice.length) {
      slice[current] = new PieSlice(sColor, sSize);
      totalSize += sSize;
      current++;
    }
  }

  publicvoid paintComponent(Graphics comp) {
    super.paintComponent(comp);
    Graphics2D comp2D = (Graphics2D) comp;
    int width = getSize().width - 10;
    int height = getSize().height - 15;
    int xInset = 5;
    int yInset = 5;
    if (width < 5) {
      xInset = width;
    }
    if (height < 5) {
      yInset = height;
    }
    comp2D.setColor(background);
    comp2D.fillRect(0, 0, getSize().width, getSize().height);
    comp2D.setColor(Color.lightGray);
    Ellipse2D.Float pie = new Ellipse2D.Float(xInset, yInset, width, height);
    comp2D.fill(pie);
    float start = 0;
    for (int i = 0; i < slice.length; i++) {
      float extent = slice[i].size * 360F / totalSize;
      comp2D.setColor(slice[i].color);
      Arc2D.Float drawSlice = new Arc2D.Float(xInset, yInset, width, height, start, extent, Arc2D.Float.PIE);
      start += extent;
      comp2D.fill(drawSlice);
    }
  }
}

class PieSlice {
  Color color = Color.lightGray;
  float size = 0;

  PieSlice(Color pColor, float pSize) {
    color = pColor;
    size = pSize;
  }
}

publicclass Main extendsJFrame {
  Color uneasyBeingGreen = newColor(0xCC, 0xCC, 0x99);
  Color zuzusPetals = newColor(0xCC, 0x66, 0xFF);
  Color zootSuit = newColor(0x66, 0x66, 0x99);
  Color sweetHomeAvocado = newColor(0x66, 0x99, 0x66);
  Color shrinkingViolet = newColor(0x66, 0x66, 0x99);
  Color miamiNice = newColor(0x33, 0xFF, 0xFF);
  Color inBetweenGreen = newColor(0x00, 0x99, 0x66);
  Color norwegianBlue = newColor(0x33, 0xCC, 0xCC);
  Color purpleRain = newColor(0x66, 0x33, 0x99);
  Color freckle = newColor(0x99, 0x66, 0x33);

  public Main() {
    super("Pie Graph");
    setSize(320, 290);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setVisible(true);

    PiePanel pie = new PiePanel(10);
    pie.addSlice(uneasyBeingGreen, 1350);
    pie.addSlice(zuzusPetals, 1221);
    pie.addSlice(zootSuit, 316);
    pie.addSlice(sweetHomeAvocado, 251);
    pie.addSlice(shrinkingViolet, 201);
    pie.addSlice(miamiNice, 193);
    pie.addSlice(inBetweenGreen, 173);
    pie.addSlice(norwegianBlue, 164);
    pie.addSlice(purpleRain, 143);
    pie.addSlice(freckle, 127);
    add(pie);
  }
  publicstaticvoid main(String[] arguments) {
    Main pf = new Main();
  }
}
```

PreviousNext

## Related

- Java AWT Graphics draw line
- Java AWT Graphics draw lines with random location
- Java AWT Graphics draw oval
- Java AWT Graphics draw Polygon
- Java AWT Graphics draw rectangle
