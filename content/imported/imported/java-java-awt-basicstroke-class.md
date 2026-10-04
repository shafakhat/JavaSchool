---
title: Java AWT BasicStroke class
nav: Java AWT BasicStroke class
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20053
source: http://www.java2s.com/ref/java/java-awt-basicstroke-class.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT BasicStroke class

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g; // cast g to Graphics2D// draw 2D rectangle in red
    g2d.setPaint(Color.RED);
    g2d.setStroke(newBasicStroke(10.0f));
    g2d.draw(newRectangle2D.Double(80, 30, 65, 100));
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

- Android Base64 decode from base64 String
- Android TextView set text
- Java AWTEvent mask window event
- Java AWT BasicStroke create
- Java AWT BasicStroke create dashed line
