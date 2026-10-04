---
title: Java Swing Tutorial - Java GraphicsConfiguration .createCompatibleImage (int width, int height, int transparency)
nav: Java Swing Tutorial - Java...
description: GraphicsConfiguration.createCompatibleImage(int width, int height, int transparency) has the following syntax.
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/0080__GraphicsConfiguration.createCompatibleImage_int_width_int_height_int_transparency_.htm
---
## Syntax

GraphicsConfiguration.createCompatibleImage(int width, int height, int transparency) has the following syntax.

```java title=Example.java
public BufferedImage createCompatibleImage(int width,     int height,     int transparency)
```

## Example

In the following code shows how to use GraphicsConfiguration.createCompatibleImage(int width, int height, int transparency) method.

```java title=Example.java
import java.awt.Graphics;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.HeadlessException;
import java.awt.Image;
import java.awt.Transparency;
import java.awt.image.BufferedImage;
import java.awt.image.ColorModel;
import java.awt.image.PixelGrabber;
import javax.swing.ImageIcon;
publicclass Main {
    publicstaticboolean hasAlpha(Image image) {
        // If buffered image, the color model is readily available
if (image instanceof BufferedImage) {
            BufferedImage bimage = (BufferedImage)image;
            return bimage.getColorModel().hasAlpha();
        }
        // Use a pixel grabber to retrieve the image's color model;
// grabbing a single pixel is usually sufficient
         PixelGrabber pg = new PixelGrabber(image, 0, 0, 1, 1, false);
        try {
            pg.grabPixels();
        } catch (InterruptedException e) {
        }
        // Get the image's color model
        ColorModel cm = pg.getColorModel();
        return cm.hasAlpha();
    }
  /**
   * This method returns a buffered image with the contents of an image
   * This snippet was taken from: http://www.exampledepot.com/egs/java.awt.image/Image2Buf.html
   * @param image
   * @return The buffered image
   */publicstatic BufferedImage toBufferedImage(Image image) {
        if (image instanceof BufferedImage) {
            return (BufferedImage)image;
        }
        // This code ensures that all the pixels in the image are loaded
        image = new ImageIcon(image).getImage();
        // Determine if the image has transparent pixels; for this method's
// implementation, see e661 Determining If an Image Has Transparent Pixels
boolean hasAlpha = hasAlpha(image);
        // Create a buffered image with a format that's compatible with the screen
        BufferedImage bimage = null;
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        try {
            // Determine the type of transparency of the new buffered image
int transparency = Transparency.OPAQUE;
            if (hasAlpha) {
                transparency = Transparency.BITMASK;
            }
            // Create the buffered image
            GraphicsDevice gs = ge.getDefaultScreenDevice();
            GraphicsConfiguration gc = gs.getDefaultConfiguration();
            bimage = gc.createCompatibleImage(
                image.getWidth(null), image.getHeight(null), transparency);
        } catch (HeadlessException e) {
            // The system does not have a screen
        }
        if (bimage == null) {
            // Create a buffered image using the default color model
int type = BufferedImage.TYPE_INT_RGB;
            if (hasAlpha) {
                type = BufferedImage.TYPE_INT_ARGB;
            }
            bimage = new BufferedImage(image.getWidth(null), image.getHeight(null), type);
        }
        // Copy image to buffered image
        Graphics g = bimage.createGraphics();
        // Paint the image onto the buffered image
        g.drawImage(image, 0, 0, null);
        g.dispose();
        return bimage;
    }
}
```
