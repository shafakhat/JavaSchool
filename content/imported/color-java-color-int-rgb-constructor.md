---
title: Java Tutorial - Java Color(int rgb) Constructor
nav: Java Tutorial - Java Color...
description: Color(int rgb) constructor from Color has the following syntax.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/Java_Color_int_rgb_Constructor.htm
---
### Syntax

Color(int rgb) constructor from Color has the following syntax.

```java title=Example.java
public Color(int rgb)
```

### Example

In the following code shows how to use Color.Color(int rgb) constructor.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    Color myColor = new Color(0XFFFFFF);
    JLabel label = new JLabel("First Name");
    label.setForeground(myColor);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
