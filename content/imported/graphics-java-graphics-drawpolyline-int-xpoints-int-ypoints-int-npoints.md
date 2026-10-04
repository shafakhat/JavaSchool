---
title: Java Tutorial - Java Graphics.drawPolyline(int[] xPoints, int[] yPoints, int nPoints)
nav: Java Tutorial - Java Graph...
description: Graphics.drawPolyline(int[] xPoints, int[] yPoints, int nPoints) has the following syntax.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_drawPolyline_int_xPoints_int_yPoints_int_nPoints_.htm
---
### Syntax

Graphics.drawPolyline(int[] xPoints, int[] yPoints, int nPoints) has the following syntax.

```java title=Example.java
publicabstractvoid drawPolyline(int[] xPoints,  int[] yPoints,  int nPoints)
```

### Example

In the following code shows how to use Graphics.drawPolyline(int[] xPoints, int[] yPoints, int nPoints) method.

```java title=Example.java
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    int[] xs = {25, 75, 125, 85, 125, 75, 25, 65};
    int[] ys = {50, 90, 50, 100, 150, 110, 150, 100};
    g.drawPolyline(xs, ys, 8);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
