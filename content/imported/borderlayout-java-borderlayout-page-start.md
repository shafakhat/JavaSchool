---
title: Java Tutorial - Java BorderLayout PAGE_START
nav: Java Tutorial - Java Borde...
description: In the following code shows how to use BorderLayout.PAGE_START field.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BorderLayout/Java_BorderLayout_PAGE_START.htm
---
### Syntax

BorderLayout.PAGE_START has the following syntax.

```java title=Example.java
publicstaticfinal String PAGE_START
```

### Example

In the following code shows how to use BorderLayout.PAGE_START field.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
publicclass Main {
  publicstaticvoid main(String[] a) {
    JFrame frame = new JFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JPanel outerPanel = new JPanel(new BorderLayout());
    JPanel topPanel = new JPanel(new BorderLayout());
    JLabel label = new JLabel("Name:");
    JTextField text = new JTextField();
    topPanel.add(label, BorderLayout.PAGE_START);
    topPanel.add(text, BorderLayout.CENTER);
    outerPanel.add(topPanel, BorderLayout.AFTER_LAST_LINE);
    frame.add(outerPanel);
    frame.setSize(300, 200);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
