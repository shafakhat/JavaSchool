---
title: Java Tutorial - Java Graphics.getFont()
nav: Java Tutorial - Java Graph...
description: In the following code shows how to use Graphics.getFont() method.
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_getFont_.htm
---
### Syntax

Graphics.getFont() has the following syntax.

```java title=Example.java
publicabstract Font getFont()
```

### Example

In the following code shows how to use Graphics.getFont() method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.drawString(g.getFont()+"", 10, 30);
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
