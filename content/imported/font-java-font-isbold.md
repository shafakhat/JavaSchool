---
title: Java Tutorial - Java Font.isBold()
nav: Java Tutorial - Java Font....
description: /*from ww w . j av a 2 s .c om*/import javax.swing.JFrame;
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/Java_Font_isBold_.htm
---
### Syntax

Font.isBold() has the following syntax.

```java title=Example.java
public boolean isBold()
```

### Example

In the following code shows how to use Font.isBold() method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
public class Main extends JFrame {
  public static void main(String[] a) {
    Main f = new Main();
    f.setSize(300, 300);
    f.setVisible(true);
  }
  public void paint(Graphics g) {
    Font f = g.getFont();
    System.out.println(f.isBold());
    g.drawString("JavaSchool", 4, 16);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
