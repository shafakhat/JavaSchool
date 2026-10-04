---
title: Java AWT Color class
nav: Java AWT Color class
description: newColor(255, 100, 100); // light red int newRed = (0xff000000 | (0xc0 << 16) | (0x00 << 8) | 0x00);
section: Imported
order: 20069
source: http://www.java2s.com/ref/java/java-awt-color-class.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

The AWT color system can specify any color you want.

Three commonly used constructors are shown here:

```java title=Example.java
Color(int red, int green, int blue)
Color(int rgbValue)
Color(float red, float green, float blue)
```

For example:

```java title=Example.java
newColor(255, 100, 100); // light red int newRed = (0xff000000 | (0xc0 << 16) | (0x00 << 8) | 0x00);
Color darkRed = newColor(newRed);
```

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

class DrawPanel extendsJPanel {
   publicvoid paintComponent(Graphics g) {
      Color c1 = newColor(255, 100, 100);
      Color c2 = newColor(100, 255, 100);
      Color c3 = newColor(100, 100, 255);

      g.setColor(c1);//fromwww.java2s.com
      g.drawLine(0, 0, 100, 100);
      g.drawLine(0, 100, 100, 0);

      g.setColor(c2);
      g.drawLine(40, 25, 250, 180);
      g.drawLine(75, 90, 400, 400);

      g.setColor(c3);
      g.drawLine(20, 150, 400, 40);
      g.drawLine(5, 290, 80, 19);

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

- Java AWT CardLayout class
- Java AWT CardLayout move to next component
- Java AWT CardLayout control by JComboBox
- Java AWT Color create from hexadecimal integer value
- Java AWT Color create random color
