---
title: Java Tutorial - Java Graphics.setClip(Shape clip)
nav: Java Tutorial - Java Graph...
description: In the following code shows how to use Graphics.setClip(Shape clip) method.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_setClip_Shape_clip_.htm
---
### Syntax

Graphics.setClip(Shape clip) has the following syntax.

```java title=Example.java
publicabstractvoid setClip(Shape clip)
```

### Example

In the following code shows how to use Graphics.setClip(Shape clip) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    int w = getSize().width;
    int h = getSize().height;
    Ellipse2D e = new Ellipse2D.Float(w / 4.0f, h / 4.0f, w / 2.0f, h / 2.0f);
    g.setClip(e);
    g.setColor(Color.red);
    g.fillRect(0, 0, w, h);
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
