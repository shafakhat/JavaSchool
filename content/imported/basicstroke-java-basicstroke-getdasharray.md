---
title: Java Tutorial - Java BasicStroke.getDashArray()
nav: Java Tutorial - Java Basic...
description: In the following code shows how to use BasicStroke.getDashArray() method.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_getDashArray_.htm
---
### Syntax

BasicStroke.getDashArray() has the following syntax.

```java title=Example.java
publicfloat[] getDashArray()
```

### Example

In the following code shows how to use BasicStroke.getDashArray() method.

```java title=Example.java
import java.awt.BasicStroke;
import java.util.Arrays;
publicclass Main {
  publicstaticvoid main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(Arrays.toString(stroke.getDashArray()));
  }
}
```

The code above generates the following result.

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
