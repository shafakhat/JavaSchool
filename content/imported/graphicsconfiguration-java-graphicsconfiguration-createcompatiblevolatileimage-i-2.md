---
title: Java Tutorial - Java GraphicsConfiguration .createCompatibleVolatileImage (int width, int height)
nav: Java Tutorial - Java Graph...
description: GraphicsConfiguration.createCompatibleVolatileImage(int width, int height) has the following syntax.
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/Java_GraphicsConfiguration_createCompatibleVolatileImage_int_width_int_height_.htm
---
### Syntax

GraphicsConfiguration.createCompatibleVolatileImage(int width, int height) has the following syntax.

```java title=Example.java
public VolatileImage createCompatibleVolatileImage(int width,      int height)
```

### Example

In the following code shows how to use GraphicsConfiguration.createCompatibleVolatileImage(int width, int height) method.

```java title=Example.java
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.HeadlessException;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.awt.image.VolatileImage;
import javax.swing.ImageIcon;
publicclass Main {
    publicstatic BufferedImage toBufferedImage(Image image) {
        if (image instanceof BufferedImage) {
            return (BufferedImage)image;
        }
        // This code ensures that all the pixels in the image are loaded
        image = new ImageIcon(image).getImage();
        // Create a buffered image with a format that's compatible with the screen
        BufferedImage bimage = null;
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        try {
            GraphicsDevice gs = ge.getDefaultScreenDevice();
            GraphicsConfiguration gc = gs.getDefaultConfiguration();
            VolatileImage vbimage = gc.createCompatibleVolatileImage(200,200);
        } catch (HeadlessException e) {
            // The system does not have a screen
        }
        return bimage;
    }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
