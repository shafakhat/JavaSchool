---
title: Java Tutorial - Java Color darkGray
nav: Java Tutorial - Java Color...
description: BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphics
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/Java_Color_darkGray.htm
---
### Syntax

Color.darkGray has the following syntax.

```java title=Example.java
public static final Color darkGray
```

### Example

In the following code shows how to use Color.darkGray field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.darkGray);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
