---
title: Java Tutorial - Java Font ITALIC
nav: Java Tutorial - Java Font ...
description: BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphics
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/Java_Font_ITALIC.htm
---
### Syntax

Font.ITALIC has the following syntax.

```java title=Example.java
publicstaticfinalint ITALIC
```

### Example

In the following code shows how to use Font.ITALIC field.

```java title=Example.java
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    int fontSize = 20;
    g.setFont(new Font("TimesRoman", Font.ITALIC, fontSize));
    String s = "JavaSchool";
    g.setColor(Color.black);
    g.drawString(s, 30, 30);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200,200);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
