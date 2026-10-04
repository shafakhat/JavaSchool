---
title: Java AWT Graphics2D fill Shape
nav: Java AWT Graphics2D fill S...
description: @Override/*fromwww.java2s.com*/publicvoid paintComponent(Graphics g) {
section: Imported
order: 20142
source: http://www.java2s.com/ref/java/java-awt-graphics2d-fill-shape.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D fill Shape

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.GeneralPath;
import java.security.SecureRandom;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override/*fromwww.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g; // cast g to Graphics2Dint[] xPoints = { 55, 67, 109, 73, 83, 55, 27, 37, 1, 43 };
    int[] yPoints = { 0, 36, 36, 54, 96, 72, 96, 54, 36, 36 };

    GeneralPath star = newGeneralPath(); // create GeneralPath object// set the initial coordinate of the General Path
    star.moveTo(xPoints[0], yPoints[0]);

    // create the star--this does not draw the starfor (int count = 1; count < xPoints.length; count++)
      star.lineTo(xPoints[count], yPoints[count]);

    star.closePath(); // close the shape

    g2d.translate(150, 150); // translate the origin to (150, 150)// rotate around origin and draw stars in random colorsSecureRandom random = newSecureRandom();
    for (int count = 1; count <= 20; count++)
    {
       g2d.rotate(Math.PI / 10.0); // rotate coordinate system// set random drawing color
       g2d.setColor(newColor(random.nextInt(256),
          random.nextInt(256), random.nextInt(256)));

       g2d.fill(star); // draw filled star
    }
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

- Java AWT Graphics2D fill area
- Java AWT Graphics2D fill rectangle with Rectangle2D
- Java AWT Graphics2D fill round rectangle with RoundRectangle2D
- Java AWT Graphics2D get font metrics
- Java AWT Graphics2D measure String
