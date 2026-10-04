---
title: Java Tutorial - Java DisplayMode.getBitDepth()
nav: Java Tutorial - Java Displ...
description: In the following code shows how to use DisplayMode.getBitDepth() method.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/DisplayMode/Java_DisplayMode_getBitDepth_.htm
---
### Syntax

DisplayMode.getBitDepth() has the following syntax.

```java title=Example.java
publicint getBitDepth()
```

### Example

In the following code shows how to use DisplayMode.getBitDepth() method.

```java title=Example.java
import java.awt.DisplayMode;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    GraphicsDevice gs = ge.getDefaultScreenDevice();
    DisplayMode[] dmodes = gs.getDisplayModes();
    for (int i = 0; i < dmodes.length; i++) {
      int bitDepth = dmodes[i].getBitDepth();
    }
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
