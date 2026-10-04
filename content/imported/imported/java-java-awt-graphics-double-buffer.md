---
title: Java AWT Graphics double buffer
nav: Java AWT Graphics double b...
description: g.drawString("Press mouse button to double buffer", 10, h / 2);
section: Imported
order: 20117
source: http://www.java2s.com/ref/java/java-awt-graphics-double-buffer.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics double buffer

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

import javax.swing.JFrame;
import javax.swing.JPanel;

class Demo extendsJPanel {
   int gap = 3;//www.java2s.comint mx, my;
   boolean flicker = true;
   Image buffer = null;
   int w, h;

   public Demo() {
      Dimension d = getSize();
      w = d.width;
      h = d.height;
      buffer = createImage(w, h);
      addMouseMotionListener(newMouseMotionAdapter() {
         publicvoid mouseDragged(MouseEvent me) {
            mx = me.getX();
            my = me.getY();
            flicker = false;
            repaint();
         }

         publicvoid mouseMoved(MouseEvent me) {
            mx = me.getX();
            my = me.getY();
            flicker = true;
            repaint();
         }
      });
   }

   publicvoid paint(Graphics g) {
      Graphics screengc = null;

      if (!flicker) {
         screengc = g;
         g = buffer.getGraphics();
      }

      g.setColor(Color.blue);
      g.fillRect(0, 0, w, h);

      g.setColor(Color.red);
      for (int i = 0; i < w; i += gap)
         g.drawLine(i, 0, w - i, h);
      for (int i = 0; i < h; i += gap)
         g.drawLine(0, i, w, h - i);

      g.setColor(Color.black);
      g.drawString("Press mouse button to double buffer", 10, h / 2);

      g.setColor(Color.yellow);
      g.fillOval(mx - gap, my - gap, gap * 2 + 1, gap * 2 + 1);

      if (!flicker) {
         screengc.drawImage(buffer, 0, 0, null);
      }
   }

   publicvoid update(Graphics g) {
      paint(g);
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

- Java AWT FontMetrics get from JTextField
- Java AWT GradientPaint
- Java AWT GradientPaint create
- Java AWT Graphics draw arc
- Java AWT Graphics draw line
