---
title: Java AWT ConvolveOp filter image
nav: Java AWT ConvolveOp filter...
description: BufferedImage srcImg = gc.createCompatibleImage(width, height, Transparency.TRANSLUCENT);
section: Imported
order: 20072
source: http://www.java2s.com/ref/java/java-awt-convolveop-filter-image.html
---
- java.awt.image
- java.awt.image BufferedImage ConvolveOp

## Description

Java AWT ConvolveOp filter image

```java title=Example.java
import java.awt.AlphaComposite;
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GraphicsConfiguration;
import java.awt.RenderingHints;
import java.awt.Shape;
import java.awt.Transparency;
import java.awt.geom.Ellipse2D;
import java.awt.image.BufferedImage;
import java.awt.image.ConvolveOp;
import java.awt.image.Kernel;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {

  privatevoid createDropShadow(Graphics g, Shape s) {

    int margin = 10;
    int padding = 5;
    int width = s.getBounds().width + padding + margin;
    int height = s.getBounds().height + padding + margin;
    Graphics2D g2d = (Graphics2D) g;
    GraphicsConfiguration gc = g2d.getDeviceConfiguration();
    BufferedImage srcImg = gc.createCompatibleImage(width, height, Transparency.TRANSLUCENT);
    BufferedImage destImg = gc.createCompatibleImage(width, height, Transparency.TRANSLUCENT);
    Graphics2D g2 = srcImg.createGraphics();

    g2.setComposite(AlphaComposite.Clear);
    g2.fillRect(0, 0, width, height);//fromwww.java2s.com

    g2.setComposite(AlphaComposite.Src);
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setStroke(newBasicStroke(3.0f));
    g2.setPaint(Color.BLUE);
    g2.translate(-s.getBounds().x, -s.getBounds().y);
    int centerX = (width - s.getBounds().width) / 2;
    int centerY = (height - s.getBounds().height) / 2;
    g2.translate(centerX, centerY);

    g2.draw(s);
    float blurValue = 1.0f / 49.0f;
    float data[] = newfloat[49];
    for (int i = 0; i < 49; i++) {
      data[i] = blurValue;
    }

    Kernel kernel = newKernel(7, 7, data);
    ConvolveOp convolve = newConvolveOp(kernel, ConvolveOp.EDGE_ZERO_FILL, null);
    convolve.filter(srcImg, destImg);

    g2.dispose();

    g2d.drawImage(destImg, s.getBounds().y - padding, s.getBounds().x - padding, null);

  }

  @Overrideprotectedvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    // set color and thickness of stroke
    g2d.setPaint(Color.BLACK);
    g2d.setStroke(newBasicStroke(2));

    Ellipse2D bigCircle = new Ellipse2D.Float(50, 50, 100, 75);
    createDropShadow(g2d, bigCircle);
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

- Java AWT BufferedImage create from existing image
- Java AWT BufferedImage load from URL
- Java AWT BufferedImage matte
- Java AWT PrinterJob set print dialog box type
- Java AWT PrinterJob print custom component
