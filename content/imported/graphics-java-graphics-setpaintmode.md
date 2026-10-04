---
title: Java Tutorial - Java Graphics.setPaintMode()
nav: Java Tutorial - Java Graph...
description: In the following code shows how to use Graphics.setPaintMode() method.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/Java_Graphics_setPaintMode_.htm
---
### Syntax

Graphics.setPaintMode() has the following syntax.

```java title=Example.java
public abstract void setPaintMode()
```

### Example

In the following code shows how to use Graphics.setPaintMode() method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    int w = getSize().width;
    int midW = w / 2;
    g.drawString("XOR Mode", 0, 30);
    g.drawOval(7, 37, 50, 50);
    g.setXORMode(Color.white);
    for (int i = 0; i < 15; i += 3) {
        g.drawOval(10 + i, 40 + i, 50, 50);
    }
    g.setPaintMode();
    g.drawString("Paint Mode", midW, 30);
    g.drawOval(midW + 7, 37, 50, 50);
    for (int i = 0; i < 15; i += 3) {
        g.drawOval(midW + 10 + i, 40 + i, 50, 50);
    }
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
