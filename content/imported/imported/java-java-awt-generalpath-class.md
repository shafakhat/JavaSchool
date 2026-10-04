---
title: Java AWT GeneralPath class
nav: Java AWT GeneralPath class
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20106
source: http://www.java2s.com/ref/java/java-awt-generalpath-class.html
---
- java.awt.geom
- java.awt.geom Arc2D Area CubicCurve2D Ellipse2D GeneralPath Line2D Path2D Point2D QuadCurve2D Rectangle2D RoundRectangle2D

## Description

Java AWT GeneralPath class

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.GeneralPath;
import java.security.SecureRandom;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
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

- Java AWT Area subtract
- Java AWT CubicCurve2D create
- Java AWT Ellipse2D class
- Java AWT Line2D class
- Java AWT Line2D create from Point2D
