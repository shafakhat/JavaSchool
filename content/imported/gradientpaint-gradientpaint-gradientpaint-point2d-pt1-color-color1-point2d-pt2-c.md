---
title: Java Swing Tutorial - Java GradientPaint(Point2D pt1, Color color1, Point2D pt2, Color color2, boolean cyclic) Constructor
nav: Java Swing Tutorial - Java...
description: GradientPaint(Point2D pt1, Color color1, Point2D pt2, Color color2, boolean cyclic) constructor from GradientPaint has the following syntax.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GradientPaint/0100__GradientPaint.GradientPaint_Point2D_pt1_Color_color1_Point2D_pt2_Color_color2_boolean_cyclic_.htm
---
```java title=Example.java
Back to GradientPaint  ↑
```

## Syntax

GradientPaint(Point2D pt1, Color color1, Point2D pt2, Color color2, boolean cyclic) constructor from GradientPaint has the following syntax.

```java title=Example.java
@ConstructorProperties(value ={"point1","color1","point2","color2","cyclic"})public GradientPaint(Point2D pt1,           Color color1,           Point2D pt2,           Color color2,          boolean cyclic)
```

## Example

In the following code shows how to use GradientPaint.GradientPaint(Point2D pt1, Color color1, Point2D pt2, Color color2, boolean cyclic) constructor.

```java title=Example.java
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.geom.Rectangle2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  public Main() {
  }
  publicvoid paint(Graphics g) {
    Graphics2D g2D = (Graphics2D) g;
    Point2D.Float p1 = new Point2D.Float(150.f, 75.f);
    Point2D.Float p2 = new Point2D.Float(250.f, 75.f);
    float width = 300;
    float height = 50;
    GradientPaint g1 = new GradientPaint(p1, Color.WHITE, p2, Color.DARK_GRAY,
        true);
    Rectangle2D.Float rect1 = new Rectangle2D.Float(p1.x - 100, p1.y - 25,
        width, height);
    g2D.setPaint(g1);
    g2D.fill(rect1);
    g2D.setPaint(Color.BLACK);
    g2D.draw(rect1);
    g2D.draw(new Line2D.Float(p1, p2));
    g2D.drawString("Cyclic Gradient Paint", p1.x - 100, p1.y - 50);
    g2D.drawString("p1", p1.x - 20, p1.y);
    g2D.drawString("p2", p2.x + 10, p2.y);
    p1.setLocation(150, 200);
    p2.setLocation(250, 200);
    GradientPaint g2 = new GradientPaint(p1, Color.WHITE, p2, Color.DARK_GRAY,
        false);
    rect1.setRect(p1.x - 100, p1.y - 25, width, height);
    g2D.setPaint(g2);
    g2D.fill(rect1);
    g2D.setPaint(Color.BLACK);
    g2D.draw(rect1);
    g2D.draw(new Line2D.Float(p1, p2));
    g2D.drawString("Acyclic Gradient Paint", p1.x - 100, p1.y - 50);
    g2D.drawString("p1", p1.x - 20, p1.y);
    g2D.drawString("p2", p2.x + 10, p2.y);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```

- Back to GradientPaint ↑
