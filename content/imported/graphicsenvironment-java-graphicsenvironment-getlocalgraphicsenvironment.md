---
title: Java Tutorial - Java GraphicsEnvironment .getLocalGraphicsEnvironment ()
nav: Java Tutorial - Java Graph...
description: GraphicsEnvironment.getLocalGraphicsEnvironment() has the following syntax.
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsEnvironment/Java_GraphicsEnvironment_getLocalGraphicsEnvironment_.htm
---
### Syntax

GraphicsEnvironment.getLocalGraphicsEnvironment() has the following syntax.

```java title=Example.java
publicstatic GraphicsEnvironment getLocalGraphicsEnvironment()
```

### Example

In the following code shows how to use GraphicsEnvironment.getLocalGraphicsEnvironment() method.

```java title=Example.java
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
publicclass Main {
  publicstaticvoid main(String[] args) {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    GraphicsDevice defaultScreen = ge.getDefaultScreenDevice();
    GraphicsConfiguration[] configurations = defaultScreen.getConfigurations();
    System.out.println("Default screen device: " + defaultScreen.getIDstring());
    for (int i = 0; i < configurations.length; i++) {
      System.out.println("  Configuration " + (i + 1));
      System.out.println("  " + configurations[i].getColorModel());
    }
  }
}
```

The code above generates the following result.

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
