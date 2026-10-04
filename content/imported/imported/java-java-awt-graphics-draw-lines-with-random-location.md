---
title: Java AWT Graphics draw lines with random location
nav: Java AWT Graphics draw lin...
description: // Get the height and width of the component.int height = getHeight();
section: Imported
order: 20124
source: http://www.java2s.com/ref/java/java-awt-graphics-draw-lines-with-random-location.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics draw lines with random location

```java title=Example.java
import java.awt.Graphics;
import java.awt.Insets;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

class Demo extendsJPanel {

   publicvoid paint(Graphics g) {
      super.paintComponent(g);

      int x, y, x2, y2;

      // Get the height and width of the component.int height = getHeight();
      int width = getWidth();
      Random rand = newRandom();
      // Get the insets.Insets ins = getInsets();//www.java2s.com// Draw ten lines whose end points are randomly generated.for (int i = 0; i < 10; i++) {
         x = rand.nextInt(width - ins.left);
         y = rand.nextInt(height - ins.bottom);
         x2 = rand.nextInt(width - ins.left);
         y2 = rand.nextInt(height - ins.bottom);

         // Draw the line.
         g.drawLine(x, y, x2, y2);
      }
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

- Java AWT Graphics double buffer
- Java AWT Graphics draw arc
- Java AWT Graphics draw line
- Java AWT Graphics draw oval
- Java AWT Graphics draw Pie
