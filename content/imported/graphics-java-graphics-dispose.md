---
title: Java Tutorial - Java Graphics.dispose()
nav: Java Tutorial - Java Graph...
description: In the following code shows how to use Graphics.dispose() method.
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_dispose_.htm
---
### Syntax

Graphics.dispose() has the following syntax.

```java title=Example.java
publicabstractvoid dispose()
```

### Example

In the following code shows how to use Graphics.dispose() method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.setColor (Color.red);
    Graphics clippedGraphics = g.create();
    clippedGraphics.drawRect (0,0,100,100);
    clippedGraphics.clipRect (25, 25, 50, 50);
    clippedGraphics.drawLine (0,0,100,100);
    clippedGraphics.dispose();
    clippedGraphics=null;
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
