---
title: Java Tutorial - Java Cursor E_RESIZE_CURSOR
nav: Java Tutorial - Java Curso...
description: In the following code shows how to use Cursor.E_RESIZE_CURSOR field.
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Cursor/Java_Cursor_E_RESIZE_CURSOR.htm
---
### Syntax

Cursor.E_RESIZE_CURSOR has the following syntax.

```java title=Example.java
publicstaticfinalint E_RESIZE_CURSOR
```

### Example

In the following code shows how to use Cursor.E_RESIZE_CURSOR field.

```java title=Example.java
import java.awt.Cursor;
import javax.swing.JFrame;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JFrame aWindow = new JFrame();
    aWindow.setBounds(200, 200, 200, 200);
    aWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    aWindow.setCursor(Cursor.getPredefinedCursor(Cursor.E_RESIZE_CURSOR));
    aWindow.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
