---
title: Java Tutorial - Java FlowLayout TRAILING
nav: Java Tutorial - Java FlowL...
description: In the following code shows how to use FlowLayout.TRAILING field.
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/Java_FlowLayout_TRAILING.htm
---
### Syntax

FlowLayout.TRAILING has the following syntax.

```java title=Example.java
publicstaticfinalint TRAILING
```

### Example

In the following code shows how to use FlowLayout.TRAILING field.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  public Main() {
    super(new FlowLayout(FlowLayout.TRAILING, 10, 3));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
