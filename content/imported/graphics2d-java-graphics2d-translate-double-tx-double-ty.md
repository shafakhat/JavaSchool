---
title: Java Tutorial - Java Graphics2D.translate(double tx, double ty)
nav: Java Tutorial - Java Graph...
description: Graphics2D.translate(double tx, double ty) has the following syntax.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics2D/Java_Graphics2D_translate_double_tx_double_ty_.htm
---
### Syntax

Graphics2D.translate(double tx, double ty) has the following syntax.

```java title=Example.java
public abstract void translate(double tx,  double ty)
```

### Example

In the following code shows how to use Graphics2D.translate(double tx, double ty) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    g.fillRect(0, 0, 20, 20);
    Graphics2D g2 = (Graphics2D) g;
    g2.translate(5.3, 5.4);
    g2.rotate(30.0 * Math.PI / 180.0);
    g2.scale(2.0, 2.0);
    g.setColor(Color.red);
    g.fillRect(0, 0, 20, 20);
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20, 20, 500, 500);
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
