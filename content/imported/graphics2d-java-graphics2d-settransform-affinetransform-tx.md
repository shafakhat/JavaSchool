---
title: Java Tutorial - Java Graphics2D .setTransform (AffineTransform Tx)
nav: Java Tutorial - Java Graph...
description: Graphics2D.setTransform(AffineTransform Tx) has the following syntax.
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics2D/Java_Graphics2D_setTransform_AffineTransform_Tx_.htm
---
### Syntax

Graphics2D.setTransform(AffineTransform Tx) has the following syntax.

```java title=Example.java
publicabstractvoid setTransform(AffineTransform Tx)
```

### Example

In the following code shows how to use Graphics2D.setTransform(AffineTransform Tx) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setPaint(Color.black);
    g2.draw(new Rectangle2D.Float(10, 20, 30, 40));
    AffineTransform at = AffineTransform.getTranslateInstance(75, 75);
    g2.setTransform(at);
    g2.setPaint(Color.red);
    g2.draw(new Rectangle2D.Float(10, 20, 30, 40));
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
