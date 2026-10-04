---
title: Java AWT Graphics fill whole window
nav: Java AWT Graphics fill who...
description: Imported from java2s.com: Java AWT Graphics fill whole window
section: Imported
order: 20126
source: http://www.java2s.com/ref/java/java-awt-graphics-fill-whole-window.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics fill whole window

```java title=Example.java
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

class DrawPanel extendsJPanel {
   publicvoid paintComponent(Graphics g) {
      super.paintComponent(g);

      int width = getWidth();
      int height = getHeight();

      g.fillRect(0, 0, width, height);/*fromwww.java2s.com*/

   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      DrawPanel panel = new DrawPanel();

      JFrame application = newJFrame();

      application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      application.add(panel);
      application.setSize(250, 250);
      application.setVisible(true);
   }
}
```

PreviousNext

## Related

- Java AWT Graphics draw with mouse
- Java AWT Graphics fill arc as rainbow
- Java AWT Graphics fill rectangle
- Java AWT Graphics paint mode
- Java AWT Graphics set font
