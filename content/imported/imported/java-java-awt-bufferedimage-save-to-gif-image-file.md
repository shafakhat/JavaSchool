---
title: Java AWT BufferedImage save to GIF image file
nav: Java AWT BufferedImage sav...
description: // draw 2D rounded rectangle with a buffered backgroundBufferedImage buffImage = newBufferedImage(10, 10, BufferedImage.TYPE_INT_RGB);
section: Imported
order: 20062
source: http://www.java2s.com/ref/java/java-awt-bufferedimage-save-to-gif-image-file.html
---
- java.awt.image
- java.awt.image BufferedImage ConvolveOp

## Description

Java AWT BufferedImage save to GIF image file

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

publicclass Main {
  publicstaticvoid main(String[] args) {
    // draw 2D rounded rectangle with a buffered backgroundBufferedImage buffImage = newBufferedImage(10, 10, BufferedImage.TYPE_INT_RGB);

    // obtain Graphics2D from buffImage and draw on itGraphics2D gg = buffImage.createGraphics();
    gg.setColor(Color.YELLOW);/*fromwww.java2s.com*/
    gg.fillRect(0, 0, 10, 10);
    gg.setColor(Color.BLACK);
    gg.drawRect(1, 1, 6, 6);

    try {
      ImageIO.write(buffImage, "gif", newFile( "image.gif"));
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

PreviousNext

## Related

- Java AWT BufferedImage create transparent image
- Java AWT BufferedImage get/set image RGB/ARGB image data
- Java AWT BufferedImage load from file
- Java AWT BufferedImage save to JPG image file
- Java AWT BufferedImage save to PNG image file
