---
title: A dashed stroke
nav: A dashed stroke
description: BasicStroke stroke = new BasicStroke(strokeThickness, BasicStroke.CAP_BUTT, BasicStroke.JOIN_MITER,
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20090426081319/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Adashedstroke.htm
---
A dashed stroke

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import javax.swing.JComponent;
import javax.swing.JFrame;
public class BasicDraw {
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new MyComponent());
    frame.setSize(300, 300);
    frame.setVisible(true);
  }
}
class MyComponent extends JComponent {
  public void paint(Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    float strokeThickness = 5.0f;
    float miterLimit = 10f;
    float[] dashPattern = { 10f };
    float dashPhase = 5f;
    BasicStroke stroke = new BasicStroke(strokeThickness, BasicStroke.CAP_BUTT, BasicStroke.JOIN_MITER,
        miterLimit, dashPattern, dashPhase);
    g2d.setStroke(stroke);
    g2d.draw(new Rectangle(20,20,200,200));
  }
}
```

1.  Dashed rectangle
---  ---
2.  Stroking or Filling with a Texture
3.  Basic stroke
4.  Thick stroke demo
5.  Dashed stroke
6.  Stroke with iron effect
7.  Smokey effect
8.  Custom Strokes
9.  Stroke Test
10.  Changing the Thickness of the Stroking Pen
