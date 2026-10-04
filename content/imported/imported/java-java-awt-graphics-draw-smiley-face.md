---
title: Java AWT Graphics draw smiley face
nav: Java AWT Graphics draw smi...
description: Imported from java2s.com: Java AWT Graphics draw smiley face
section: Imported
order: 20122
source: http://www.java2s.com/ref/java/java-awt-graphics-draw-smiley-face.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics draw smiley face

```java title=Example.java
// Demonstrates filled shapes.import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    // draw the face
    g.setColor(Color.YELLOW);//www.java2s.com
    g.fillOval(10, 10, 200, 200);

    // draw the eyes
    g.setColor(Color.BLACK);
    g.fillOval(55, 65, 30, 30);
    g.fillOval(135, 65, 30, 30);

    // draw the mouth
    g.fillOval(50, 110, 120, 60);

    // "touch up" the mouth into a smile
    g.setColor(Color.YELLOW);
    g.fillRect(50, 110, 120, 30);
    g.fillOval(50, 120, 120, 40);
  }

  publicstaticvoid main(String[] args) {
    Main panel = new Main();
    JFrame application = newJFrame();

    application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    application.add(panel);
    application.setSize(230, 250);
    application.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT Graphics draw Polygon
- Java AWT Graphics draw rectangle
- Java AWT Graphics draw round rectangle
- Java AWT Graphics draw with mouse
- Java AWT Graphics fill arc as rainbow
