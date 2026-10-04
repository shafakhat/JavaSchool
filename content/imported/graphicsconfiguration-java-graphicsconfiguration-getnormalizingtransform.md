---
title: Java Tutorial - Java GraphicsConfiguration .getNormalizingTransform ()
nav: Java Tutorial - Java Graph...
description: GraphicsConfiguration.getNormalizingTransform() has the following syntax.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/Java_GraphicsConfiguration_getNormalizingTransform_.htm
---
### Syntax

GraphicsConfiguration.getNormalizingTransform() has the following syntax.

```java title=Example.java
publicabstract AffineTransform getNormalizingTransform()
```

### Example

In the following code shows how to use GraphicsConfiguration.getNormalizingTransform() method.

```java title=Example.java
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
publicclass Main {
    publicstaticvoid main(String[] argv) {
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice gs = ge.getDefaultScreenDevice();
        GraphicsConfiguration gc = gs.getDefaultConfiguration();
        System.out.println(gc.getNormalizingTransform());
    }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
