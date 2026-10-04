---
title: Another GradientPaint Demo
nav: Another GradientPaint Demo
description: Another GradientPaint Demo : Java examples (example source code) » 2D Graphics GUI » Gradient Paint
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20060506182544/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/AnotherGradientPaintDemo.htm
---
Another GradientPaint Demo : Java examples (example source code) » 2D Graphics GUI » Gradient Paint

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class GradientPaintDemo extends JPanel {
  public void init() {
    setBackground(Color.white);
  }
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    g2.setPaint(new GradientPaint(0, 0, Color.lightGray, 200,
        200, Color.blue, false));
    Rectangle r = new Rectangle(5,5,200,200);
    g2.fill(r);
  }
  public static void main(String s[]) {
    JFrame f = new JFrame();
    f.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    GradientPaintDemo p = new GradientPaintDemo();
    f.getContentPane().add("Center", p);
    p.init();
    f.pack();
    f.setSize(new Dimension(250, 250));
    f.show();
  }
}
```

Related examples in the same category
---
1. GradientPaint demo
2. GradientPaint Ellipse
3. Text effect: rotation and transparent
4. Text effect: image texture
5. Texture paint
6. Round GradientPaint Fill demo
7. GradientPaint: iron
8. Color gradient
9. Paints
