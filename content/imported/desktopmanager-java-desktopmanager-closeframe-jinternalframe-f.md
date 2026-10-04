---
title: Java Tutorial - Java DesktopManager .closeFrame (JInternalFrame f)
nav: Java Tutorial - Java Deskt...
description: DesktopManager.closeFrame(JInternalFrame f) has the following syntax.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/DesktopManager/Java_DesktopManager_closeFrame_JInternalFrame_f_.htm
---
### Syntax

DesktopManager.closeFrame(JInternalFrame f) has the following syntax.

```java title=Example.java
void closeFrame(JInternalFrame f)
```

### Example

In the following code shows how to use DesktopManager.closeFrame(JInternalFrame f) method.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JDesktopPane;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JLabel;
publicclass Main {
  publicstaticvoid main(final String[] args) {
    JFrame frame = new JFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JDesktopPane desktop = new JDesktopPane();
    JInternalFrame internalFrame = new JInternalFrame("Can Do All", true, true, true, true);
    desktop.add(internalFrame);
    internalFrame.setBounds(25, 25, 200, 100);
    JLabel label = new JLabel(internalFrame.getTitle(), JLabel.CENTER);
    internalFrame.add(label, BorderLayout.CENTER);
    internalFrame.setVisible(true);
    desktop.getDesktopManager().closeFrame(internalFrame);
    frame.add(desktop, BorderLayout.CENTER);
    frame.setSize(500, 300);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
