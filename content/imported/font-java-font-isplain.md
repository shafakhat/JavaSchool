---
title: Java Tutorial - Java Font.isPlain()
nav: Java Tutorial - Java Font....
description: In the following code shows how to use Font.isPlain() method.
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/Java_Font_isPlain_.htm
---
### Syntax

Font.isPlain() has the following syntax.

```java title=Example.java
publicboolean isPlain()
```

### Example

In the following code shows how to use Font.isPlain() method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
publicclass Main extends JFrame {
  publicstaticvoid main(String[] a) {
    Main f = new Main();
    f.setSize(300, 300);
    f.setVisible(true);
  }
  publicvoid paint(Graphics g) {
    Font f = g.getFont();
    System.out.println(f.isPlain());
    g.drawString("JavaSchool", 4, 16);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
