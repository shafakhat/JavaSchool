---
title: Java AWT BufferedImage zoom image on mouse wheel event
nav: Java AWT BufferedImage zoo...
description: setSize((int) (bi.getWidth() * factor), (int) (bi.getHeight() * factor));
section: Imported
order: 20063
source: http://www.java2s.com/ref/java/java-awt-bufferedimage-zoom-image-on-mouse-wheel-event.html
---
- java.awt.image
- java.awt.image BufferedImage ConvolveOp

## Description

Java AWT BufferedImage zoom image on mouse wheel event

```java title=Example.java
import java.awt.Graphics;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.JFrame;

publicclass Main extendsJFrame {
  privateBufferedImage bi;

  privateint zoom = 0;

  privatestaticfinaldouble ZOOM_AMOUNT = 1.1;

  publicstaticvoid main(String[] args) {
      new Main("icon.png").setVisible(true);
  }/*www.java2s.com*/privatevoid sizeToZoom() {
    double factor = Math.pow(ZOOM_AMOUNT, zoom);
    setSize((int) (bi.getWidth() * factor), (int) (bi.getHeight() * factor));
  }

  public Main(String filename) {
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    try {
      bi = ImageIO.read(newFile(filename));
    } catch (Exception e) {
      e.printStackTrace();
    }

    sizeToZoom();

    addMouseWheelListener(newMouseWheelListener() {
      publicvoid mouseWheelMoved(MouseWheelEvent e) {
        int steps = e.getWheelRotation();
        zoom += steps;
        sizeToZoom();
      }
    });
  }

  publicvoid paint(Graphics g) {
    g.drawImage(bi, 0, 0, getWidth(), getHeight(), this);
  }
}
```

PreviousNext

## Related

- Java AWT BufferedImage save to JPG image file
- Java AWT BufferedImage save to PNG image file
- Java AWT BufferedImage set image pixel
- Java AWT BufferedImage copy image
- Java AWT BufferedImage copy or create Image
