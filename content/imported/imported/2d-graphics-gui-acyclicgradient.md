---
title: A cyclic gradient
nav: A cyclic gradient
description: GradientPaint gradient = new GradientPaint(startX, startY, startColor, endX, endY, endColor,true);
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20090615220743/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Acyclicgradient.htm
---
A cyclic gradient

```java title=Example.java
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import javax.swing.JComponent;
import javax.swing.JFrame;
public class BasicDraw {
  public static void main(String[] args) {
    new BasicDraw();
  }
  BasicDraw() {
    JFrame frame = new JFrame();
    frame.add(new MyComponent());
    frame.setSize(300, 300);
    frame.setVisible(true);
  }
}
class MyComponent extends JComponent {
  public void paint(Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    Color startColor = Color.red;
    Color endColor = Color.blue;
    int startX = 10, startY = 20, endX = 30, endY = 40;
    GradientPaint gradient = new GradientPaint(startX, startY, startColor, endX, endY, endColor,true);
    g2d.setPaint(gradient);
    g2d.draw(new Rectangle(20, 20, 200, 200));
  }
}
```

1.  Gradients: a smooth blending of shades from light to dark or from one color to another
---  ---
2.  Gradient Shapes
3.  GradientPaint demo
4.  GradientPaint Ellipse
5.  Another GradientPaint Demo
6.  Text effect: rotation and transparent
7.  Text effect: image texture
8.  Texture paint
9.  Round GradientPaint Fill demo
10.  GradientPaint: iron
11.  Color gradient
12.  Drawing with a Gradient Color
13.  A non-cyclic gradient
14.  Paints
15.  Horizontal Gradients
16.  Vertical Gradient Paint
17.  Gradients in the middle
18.  Control the direction of Gradients
