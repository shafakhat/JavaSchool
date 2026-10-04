---
title: Java Tutorial - Java Color DARK_GRAY
nav: Java Tutorial - Java Color...
description: In the following code shows how to use Color.DARK_GRAY field.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/Java_Color_DARK_GRAY.htm
---
### Syntax

Color.DARK_GRAY has the following syntax.

```java title=Example.java
public static final Color DARK_GRAY
```

### Example

In the following code shows how to use Color.DARK_GRAY field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.DARK_GRAY);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
