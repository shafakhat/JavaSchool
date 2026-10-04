---
title: Java Tutorial - Java Graphics.setColor(Color c)
nav: Java Tutorial - Java Graph...
description: In the following code shows how to use Graphics.setColor(Color c) method.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_setColor_Color_c_.htm
---
### Syntax

Graphics.setColor(Color c) has the following syntax.

```java title=Example.java
publicabstractvoid setColor(Color c)
```

### Example

In the following code shows how to use Graphics.setColor(Color c) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.setColor (Color.red);
    g.drawRect (0,0,100,100);
    g.clipRect (25, 25, 50, 50);
    g.drawLine (0,100,100,0);
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
