---
title: Java AWT BufferedImage copy image
nav: Java AWT BufferedImage cop...
description: }/*fromwww.java2s.com*/publicstaticBufferedImage copyImage(BufferedImage image, int type) {
section: Imported
order: 20060
source: http://www.java2s.com/ref/java/java-awt-bufferedimage-copy-image.html
---
- java.awt.image
- java.awt.image BufferedImage ConvolveOp

## Description

Java AWT BufferedImage copy image

```java title=Example.java
//package com.demo2s;import java.awt.Graphics2D;

import java.awt.image.BufferedImage;

publicclass Main {
    publicstaticBufferedImage copyImage(BufferedImage image) {
        return copyImage(image, image.getType());
    }/*fromwww.java2s.com*/publicstaticBufferedImage copyImage(BufferedImage image, int type) {
        BufferedImage copy = newBufferedImage(image.getWidth(), image.getHeight(), type);
        Graphics2D graphics2D = copy.createGraphics();
        graphics2D.drawImage(image, 0, 0, null);
        graphics2D.dispose();
        return copy;
    }
}
```

PreviousNext

## Related

- Java AWT BufferedImage save to PNG image file
- Java AWT BufferedImage set image pixel
- Java AWT BufferedImage zoom image on mouse wheel event
- Java AWT BufferedImage copy or create Image
- Java AWT BufferedImage create from existing image
