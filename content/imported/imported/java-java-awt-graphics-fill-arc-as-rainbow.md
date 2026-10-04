---
title: Java AWT Graphics fill arc as rainbow
nav: Java AWT Graphics fill arc...
description: // Drawing a rainbow using arcs and an array of colors.import java.awt.Color;
section: Imported
order: 20127
source: http://www.java2s.com/ref/java/java-awt-graphics-fill-arc-as-rainbow.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics fill arc as rainbow

```java title=Example.java
// Drawing a rainbow using arcs and an array of colors.import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

class DrawRainbow extendsJPanel {
   // define indigo and violetprivatefinalstaticColor VIOLET = newColor(128, 0, 128);
   privatefinalstaticColor INDIGO = newColor(75, 0, 130);

   // colors to use in the rainbow, starting from the innermost// The two white entries result in an empty arc in the centerprivateColor[] colors = { Color.WHITE, Color.WHITE, VIOLET, INDIGO, Color.BLUE, Color.GREEN, Color.YELLOW,
         Color.ORANGE, Color.RED };

   // constructorpublic DrawRainbow() {
      setBackground(Color.WHITE); // set the background to white
   } // end DrawRainbow constructor// draws a rainbow using concentric arcspublicvoid paintComponent(Graphics g) {
      super.paintComponent(g);

      int radius = 20; // radius of an arc// draw the rainbow near the bottom-centerint centerX = getWidth() / 2;
      int centerY = getHeight() - 10;

      // draws filled arcs starting with the outermostfor (int counter = colors.length; counter > 0; counter--) {
         // set the color for the current arc
         g.setColor(colors[counter - 1]);

         // fill the arc from 0 to 180 degrees
         g.fillArc(centerX - counter * radius, centerY - counter * radius, counter * radius * 2, counter * radius * 2,
               0, 180);/*www.java2s.com*/
      }
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      DrawRainbow panel = new DrawRainbow();
      JFrame application = newJFrame();

      application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      application.add(panel);
      application.setSize(400, 250);
      application.setVisible(true);
   }
}
```

PreviousNext

## Related

- Java AWT Graphics draw round rectangle
- Java AWT Graphics draw smiley face
- Java AWT Graphics draw with mouse
- Java AWT Graphics fill rectangle
- Java AWT Graphics fill whole window
