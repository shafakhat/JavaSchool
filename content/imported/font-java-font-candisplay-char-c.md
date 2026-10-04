---
title: Java Tutorial - Java Font.canDisplay(char c)
nav: Java Tutorial - Java Font....
description: In the following code shows how to use Font.canDisplay(char c) method.
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/Java_Font_canDisplay_char_c_.htm
---
### Syntax

Font.canDisplay(char c) has the following syntax.

```java title=Example.java
publicboolean canDisplay(char c)
```

### Example

In the following code shows how to use Font.canDisplay(char c) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    int fontSize = 20;
    Font font = new Font("TimesRoman", Font.PLAIN, fontSize);
    g.setFont(font);
    font.canDisplay('A');
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
