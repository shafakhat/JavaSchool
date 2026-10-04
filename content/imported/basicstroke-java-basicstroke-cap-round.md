---
title: Java Tutorial - Java BasicStroke CAP_ROUND
nav: Java Tutorial - Java Basic...
description: In the following code shows how to use BasicStroke.CAP_ROUND field.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_CAP_ROUND.htm
---
### Syntax

BasicStroke.CAP_ROUND has the following syntax.

```java title=Example.java
publicstaticfinalint CAP_ROUND
```

### Example

In the following code shows how to use BasicStroke.CAP_ROUND field.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    BasicStroke bs = new BasicStroke(16.0f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_BEVEL);
    g2.setStroke(bs);
    g.drawLine(30, 20, 270, 20);
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
