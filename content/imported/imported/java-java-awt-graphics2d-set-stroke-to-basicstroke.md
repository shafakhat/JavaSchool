---
title: Java AWT Graphics2D set stroke to BasicStroke
nav: Java AWT Graphics2D set st...
description: @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
section: Imported
order: 20151
source: http://www.java2s.com/ref/java/java-awt-graphics2d-set-stroke-to-basicstroke.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D set stroke to BasicStroke

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Arc2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g; // cast g to Graphics2D// draw 2D pie-shaped arc in white
    g2d.setPaint(Color.WHITE);
    g2d.setStroke(newBasicStroke(6.0f));
    g2d.draw(new Arc2D.Double(240, 30, 75, 100, 0, 270, Arc2D.PIE));
  }

  publicstaticvoid main(String[] args) {
    JFrame frame = newJFrame("Drawing 2D shapes");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Main Main = new Main();
    frame.add(Main);
    frame.setSize(425, 200);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT Graphics2D set paint to red color
- Java AWT Graphics2D set paint to TexturePaint
- Java AWT Graphics2D set radial gradient paint
- Java AWT Graphics2D transform reset
- Java AWT Graphics2D transform rotate
