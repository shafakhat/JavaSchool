---
title: Java AWT Graphics2D draw image
nav: Java AWT Graphics2D draw i...
description: @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
section: Imported
order: 20132
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-image.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw image

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();
  @Override/*www.java2s.com*/publicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.BLACK);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    //image loading should be outside paintComponent(Graphics g) method//this is just for illustration purposeBufferedImage image;
    try {
      image = ImageIO.read(newFile("icon.png"));
      g2d.setBackground(Color.WHITE);
      g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
      if (image != null) {
          g2d.drawImage(image, 0, 0, image.getWidth(), image.getHeight(), null);
      }
    } catch (IOException e) {
      e.printStackTrace();
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

PreviousNext

## Related

- Java AWT Graphics2D draw cubic curve
- Java AWT Graphics2D draw dashed line
- Java AWT Graphics2D draw ellipse with Ellipse2D
- Java AWT Graphics2D draw line
- Java AWT Graphics2D draw line with Line2D
