---
title: Java Tutorial - Java BasicStroke CAP_SQUARE
nav: Java Tutorial - Java Basic...
description: In the following code shows how to use BasicStroke.CAP_SQUARE field.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_CAP_SQUARE.htm
---
Next »BasicStroke (3202/9945)« Previous

### Syntax

BasicStroke.CAP_SQUARE has the following syntax.

```java title=Example.java
publicstaticfinalint CAP_SQUARE
```

### Example

In the following code shows how to use BasicStroke.CAP_SQUARE field.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
/*fromwww.java2s.com*/import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extends JPanel {

  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;

    BasicStroke bs = new BasicStroke(16.0f, BasicStroke.CAP_SQUARE, BasicStroke.JOIN_BEVEL);
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

Next »« PreviousHome » Java Tutorial » java.awt »

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
