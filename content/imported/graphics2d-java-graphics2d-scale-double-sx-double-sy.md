---
title: Java Tutorial - Java Graphics2D.scale(double sx, double sy)
nav: Java Tutorial - Java Graph...
description: Graphics2D.scale(double sx, double sy) has the following syntax.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics2D/Java_Graphics2D_scale_double_sx_double_sy_.htm
---
### Syntax

Graphics2D.scale(double sx, double sy) has the following syntax.

```java title=Example.java
publicabstractvoid scale(double sx,  double sy)
```

### Example

In the following code shows how to use Graphics2D.scale(double sx, double sy) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.fillRect(0, 0, 20, 20);
    Graphics2D g2 = (Graphics2D) g;
    g2.translate(50, 50);
    g2.rotate(30.0 * Math.PI / 180.0);
    g2.scale(2.0, 2.0);
    g.setColor(Color.red);
    g.fillRect(0, 0, 20, 20);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20, 20, 500, 500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
