---
title: Java Tutorial - Java Graphics.setClip(int x, int y, int width, int height)
nav: Java Tutorial - Java Graph...
description: Graphics.setClip(int x, int y, int width, int height) has the following syntax.
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_setClip_int_x_int_y_int_width_int_height_.htm
---
### Syntax

Graphics.setClip(int x, int y, int width, int height) has the following syntax.

```java title=Example.java
publicabstractvoid setClip(int x,  int y,  int width,  int height)
```

### Example

In the following code shows how to use Graphics.setClip(int x, int y, int width, int height) method.

```java title=Example.java
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.drawString(g.getClipBounds().toString(), 10, 30);
    g.clipRect(10, 40, getSize().width - 20, getSize().height - 80);
    g.fillOval(0, 0, getSize().width, getSize().height);
    String newClip = g.getClipBounds().toString();
    g.setClip(0, 0, getSize().width, getSize().height);
    g.drawString(newClip, 10, getSize().height - 10);
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
