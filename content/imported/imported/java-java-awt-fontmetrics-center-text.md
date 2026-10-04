---
title: Java AWT FontMetrics center text
nav: Java AWT FontMetrics cente...
description: drawCenteredString("This is centered.", d.width, d.height, g);
section: Imported
order: 20101
source: http://www.java2s.com/ref/java/java-awt-fontmetrics-center-text.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT FontMetrics center text

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

class Demo extendsJPanel {
   finalFont f = newFont("SansSerif", Font.BOLD, 18);

   publicvoid paint(Graphics g) {
     Dimension d = this.getSize();

     g.setColor(Color.white);//www.java2s.com
     g.fillRect(0, 0, d.width,d.height);
     g.setColor(Color.black);
     g.setFont(f);
     drawCenteredString("This is centered.", d.width, d.height, g);
     g.drawRect(0, 0, d.width-1, d.height-1);
   }

   publicvoid drawCenteredString(String s, int w, int h,
                                  Graphics g) {
     FontMetrics fm = g.getFontMetrics();
     int x = (w - fm.stringWidth(s)) / 2;
     int y = (fm.getAscent() + (h - (fm.getAscent()
              + fm.getDescent()))/2);
     g.drawString(s, x, y);
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      Demo panel = new Demo();

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

- Java AWT Font derive font from swing component
- Java AWT FontMetrics from Graphics
- Java AWT FontMetrics multiple line text alignment
- Java AWT FontMetrics get font height and width
- Java AWT FontMetrics get from JTextField
