---
title: Java Tutorial - Java FontMetrics.charWidth(int codePoint)
nav: Java Tutorial - Java FontM...
description: FontMetrics.charWidth(int codePoint) has the following syntax.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FontMetrics/Java_FontMetrics_charWidth_int_codePoint_.htm
---
### Syntax

FontMetrics.charWidth(int codePoint) has the following syntax.

```java title=Example.java
publicint charWidth(int codePoint)
```

### Example

In the following code shows how to use FontMetrics.charWidth(int codePoint) method.

```java title=Example.java
import java.awt.FontMetrics;
import javax.swing.JFrame;
publicclass Main {
  publicstaticvoid main(String args[]) {
    JFrame f = new JFrame("JColorChooser Sample");
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setSize(300, 200);
    f.setVisible(true);
    FontMetrics metrics = f.getFontMetrics(f.getFont());
    int widthX = metrics.charWidth((int)'C');
    System.out.println(widthX);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
