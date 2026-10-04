---
title: Java AWT Color create random color
nav: Java AWT Color create rand...
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20065
source: http://www.java2s.com/ref/java/java-awt-color-create-random-color.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

Java AWT Color create random color

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();
  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.BLACK);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());

    for (int i=0; i<3000; i++) {
        int red = rnd.nextInt(256);
        int green = rnd.nextInt(256);
        int blue = rnd.nextInt(256);
        g2d.setColor(newColor(red, green, blue));

        int rndX = rnd.nextInt(getSize().width);
        int rndY = rnd.nextInt(getSize().height);

        g2d.drawLine(rndX, rndY, rndX, rndY);
    }
  }

  publicstaticvoid main(String[] args) {
    // create frame for MainJFrame frame = newJFrame("java2s.com");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    Main Main = new Main();
    frame.add(Main);
    frame.setSize(300, 210);
    frame.setVisible(true);
  }
}
```

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

- Java AWT CardLayout control by JComboBox
- Java AWT Color class
- Java AWT Color create from hexadecimal integer value
- Java AWT Color make color darker
- Java AWT Color predefined color constant value
