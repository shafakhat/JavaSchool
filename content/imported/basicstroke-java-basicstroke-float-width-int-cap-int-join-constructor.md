---
title: Java Tutorial - Java BasicStroke(float width, int cap, int join) Constructor
nav: Java Tutorial - Java Basic...
description: BasicStroke(float width, int cap, int join) constructor from BasicStroke has the following syntax.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_float_width_int_cap_int_join_Constructor.htm
---
### Syntax

BasicStroke(float width, int cap, int join) constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke(float width,   int cap,   int join)
```

### Example

In the following code shows how to use BasicStroke.BasicStroke(float width, int cap, int join) constructor.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    g2.setPaint(Color.black);
    g2.setStroke(new BasicStroke(8,BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL));
    g2.draw(new Ellipse2D.Double(20,20, 50, 50));
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
