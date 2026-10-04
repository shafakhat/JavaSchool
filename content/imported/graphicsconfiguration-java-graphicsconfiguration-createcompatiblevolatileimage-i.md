---
title: Java Tutorial - Java GraphicsConfiguration .createCompatibleVolatileImage (int width, int height, int transparency)
nav: Java Tutorial - Java Graph...
description: GraphicsConfiguration.createCompatibleVolatileImage(int width, int height, int transparency) has the following syntax.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/Java_GraphicsConfiguration_createCompatibleVolatileImage_int_width_int_height_int_transparency_.htm
---
### Syntax

GraphicsConfiguration.createCompatibleVolatileImage(int width, int height, int transparency) has the following syntax.

```java title=Example.java
public VolatileImage createCompatibleVolatileImage(int width,      int height,      int transparency)
```

### Example

In the following code shows how to use GraphicsConfiguration.createCompatibleVolatileImage(int width, int height, int transparency) method.

```java title=Example.java
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.Transparency;
import java.awt.image.BufferedImage;
public class Main {
  public static void main(String[] argv) throws Exception {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    GraphicsDevice gs = ge.getDefaultScreenDevice();
    GraphicsConfiguration gc = gs.getDefaultConfiguration();
    // Create an image that does not support transparency
    BufferedImage bimage = gc.createCompatibleImage(100, 100, Transparency.OPAQUE);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
