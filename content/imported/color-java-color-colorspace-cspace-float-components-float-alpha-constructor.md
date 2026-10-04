---
title: Java Tutorial - Java Color(ColorSpace cspace, float[] components, float alpha) Constructor
nav: Java Tutorial - Java Color...
description: Color(ColorSpace cspace, float[] components, float alpha) constructor from Color has the following syntax.
section: Imported - java2s Archive
order: 1244
source: https://web.archive.org/web/20140829194504/http://www.java2s.com/Tutorials/Java/java.awt/Color/Java_Color_ColorSpace_cspace_float_components_float_alpha_Constructor.htm
---
### Syntax

Color(ColorSpace cspace, float[] components, float alpha) constructor from Color has the following syntax.

```java title=Example.java
public Color(ColorSpace cspace,  float[] components,  float alpha)
```

### Example

In the following code shows how to use Color.Color(ColorSpace cspace, float[] components, float alpha) constructor.

```java title=Example.java
import java.awt.Color;
import java.awt.color.ColorSpace;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Color myColor = new Color(ColorSpace.getInstance(ColorSpace.CS_CIEXYZ),new float[]{0.1F,0.2F,0.3F},0.4F);
    System.out.println(Arrays.toString(myColor.getColorComponents(null)));
  }
}
```

The code above generates the following result.

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
