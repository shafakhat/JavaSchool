---
title: Java Tutorial - Java Graphics.drawOval(int x, int y, int width, int height)
nav: Java Tutorial - Java Graph...
description: Graphics.drawOval(int x, int y, int width, int height) has the following syntax.
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_drawOval_int_x_int_y_int_width_int_height_.htm
---
### Syntax

Graphics.drawOval(int x, int y, int width, int height) has the following syntax.

```java title=Example.java
publicabstractvoid drawOval(int x,  int y,  int width,  int height)
```

### Example

In the following code shows how to use Graphics.drawOval(int x, int y, int width, int height) method.

```java title=Example.java
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.drawOval(25, 25, 120, 120);
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
