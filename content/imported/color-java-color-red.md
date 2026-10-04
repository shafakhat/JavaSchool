---
title: Java Tutorial - Java Color RED
nav: Java Tutorial - Java Color...
description: BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphics
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/Java_Color_red.htm
---
### Syntax

Color.RED has the following syntax.

```java title=Example.java
publicstaticfinal Color RED
```

### Example

In the following code shows how to use Color.RED field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.RED);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
