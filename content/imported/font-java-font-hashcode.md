---
title: Java Tutorial - Java Font.hashCode()
nav: Java Tutorial - Java Font....
description: In the following code shows how to use Font.hashCode() method.
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/Java_Font_hashCode_.htm
---
### Syntax

Font.hashCode() has the following syntax.

```java title=Example.java
publicint hashCode()
```

### Example

In the following code shows how to use Font.hashCode() method.

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
    System.out.println(f.hashCode());
    g.drawString("JavaSchool", 4, 16);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
