---
title: Java Tutorial - Java GraphicsConfiguration .getBufferCapabilities ()
nav: Java Tutorial - Java Graph...
description: GraphicsConfiguration.getBufferCapabilities() has the following syntax.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/Java_GraphicsConfiguration_getBufferCapabilities_.htm
---
### Syntax

GraphicsConfiguration.getBufferCapabilities() has the following syntax.

```java title=Example.java
public BufferCapabilities getBufferCapabilities()
```

### Example

In the following code shows how to use GraphicsConfiguration.getBufferCapabilities() method.

```java title=Example.java
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
publicclass Main {
    publicstaticvoid main(String[] argv) {
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice gs = ge.getDefaultScreenDevice();
        GraphicsConfiguration gc = gs.getDefaultConfiguration();
        System.out.println(gc.getBufferCapabilities());
    }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
