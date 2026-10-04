---
title: Java Swing Tutorial - Java GradientPaint .createContext (ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform xform, RenderingHints hints)
nav: Java Swing Tutorial - Java...
description: GradientPaint.createContext(ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform xform, RenderingHints hints) has the following syntax.
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GradientPaint/0120__GradientPaint.createContext_ColorModel_cm_Rectangle_deviceBounds_Rectangle2D_userBounds_AffineTransform_xform_RenderingHints_hints_.htm
---
```java title=Example.java
Back to GradientPaint  ↑
```

## Syntax

GradientPaint.createContext(ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform xform, RenderingHints hints) has the following syntax.

```java title=Example.java
public PaintContext createContext(ColorModel cm,    Rectangle deviceBounds,    Rectangle2D userBounds,    AffineTransform xform,    RenderingHints hints)
```

## Example

In the following code shows how to use GradientPaint.createContext(ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform xform, RenderingHints hints) method.

```java title=Example.java
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.geom.AffineTransform;
import java.awt.image.ColorModel;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    super.paint(g);
    Graphics2D g2d = (Graphics2D) g;
    GradientPaint gp1 = new GradientPaint(5, 5, Color.red, 20, 20, Color.yellow, true);
    gp1.createContext(ColorModel.getRGBdefault(), new Rectangle(0,0,30,40), new Rectangle(0,0,30,40),
        new AffineTransform(), null);
    System.out.println(gp1.getTransparency());
    g2d.setPaint(gp1);
    g2d.fillRect(20, 20, 300, 40);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame("GradientsRedYellow");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.add(new Main());
    frame.setSize(350, 350);
    frame.setLocationRelativeTo(null);
    frame.setVisible(true);
  }
}
```

- Back to GradientPaint ↑
