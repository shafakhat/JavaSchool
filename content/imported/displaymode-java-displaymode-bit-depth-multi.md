---
title: Java Tutorial - Java DisplayMode BIT_DEPTH_MULTI
nav: Java Tutorial - Java Displ...
description: In the following code shows how to use DisplayMode.BIT_DEPTH_MULTI field.
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/DisplayMode/Java_DisplayMode_BIT_DEPTH_MULTI.htm
---
### Syntax

DisplayMode.BIT_DEPTH_MULTI has the following syntax.

```java title=Example.java
publicstaticfinalint BIT_DEPTH_MULTI
```

### Example

In the following code shows how to use DisplayMode.BIT_DEPTH_MULTI field.

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
      if(dmodes[i].getBitDepth() == DisplayMode.BIT_DEPTH_MULTI){
        System.out.println("DisplayMode.BIT_DEPTH_MULTI");
      }
    }
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
