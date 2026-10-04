---
title: Java AWT BufferedImage draw on created BufferedImage
nav: Java AWT BufferedImage dra...
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20061
source: http://www.java2s.com/ref/java/java-awt-bufferedimage-draw-on-created-bufferedimage.html
---
- java.awt.image
- java.awt.image BufferedImage ConvolveOp

## Description

Java AWT BufferedImage draw on created BufferedImage

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.TexturePaint;
import java.awt.geom.RoundRectangle2D;
import java.awt.image.BufferedImage;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g; // cast g to Graphics2D// draw 2D rounded rectangle with a buffered backgroundBufferedImage buffImage = newBufferedImage(10, 10, BufferedImage.TYPE_INT_RGB);

    // obtain Graphics2D from buffImage and draw on itGraphics2D gg = buffImage.createGraphics();
    gg.setColor(Color.YELLOW);
    gg.fillRect(0, 0, 10, 10);
    gg.setColor(Color.BLACK);
    gg.drawRect(1, 1, 6, 6);

    // paint buffImage onto the JFrame
    g2d.setPaint(newTexturePaint(buffImage, newRectangle(10, 10)));
    g2d.fill(new RoundRectangle2D.Double(155, 30, 75, 100, 50, 50));
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

- Java AWT Rectangle2D class
- Java AWT RoundRectangle2D class
- Java AWT BufferedImage create
- Java AWT BufferedImage create transparent image
- Java AWT BufferedImage get/set image RGB/ARGB image data
