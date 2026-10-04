---
title: Java Tutorial - Java GraphicsEnvironment .preferProportionalFonts ()
nav: Java Tutorial - Java Graph...
description: GraphicsEnvironment.preferProportionalFonts() has the following syntax.
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsEnvironment/Java_GraphicsEnvironment_preferProportionalFonts_.htm
---
### Syntax

GraphicsEnvironment.preferProportionalFonts() has the following syntax.

```java title=Example.java
publicvoid preferProportionalFonts()
```

### Example

In the following code shows how to use GraphicsEnvironment.preferProportionalFonts() method.

```java title=Example.java
import java.awt.GraphicsEnvironment;
publicclass Main {
  publicstaticvoid main(String[] args) {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    ge.preferProportionalFonts();
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
