---
title: Java Swing Tutorial - Java GradientPaint(float x1, float y1, Color color1, float x2, float y2, Color color2, boolean cyclic) Constructor
nav: Java Swing Tutorial - Java...
description: GradientPaint(float x1, float y1, Color color1, float x2, float y2, Color color2, boolean cyclic) constructor from GradientPaint has the following syntax.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GradientPaint/0060__GradientPaint.GradientPaint_float_x1_float_y1_Color_color1_float_x2_float_y2_Color_color2_boolean_cyclic_.htm
---
## Syntax

GradientPaint(float x1, float y1, Color color1, float x2, float y2, Color color2, boolean cyclic) constructor from GradientPaint has the following syntax.

```java title=Example.java
public GradientPaint(float x1,    float y1,    Color color1,    float x2,    float y2,    Color color2,    boolean cyclic)
```

## Example

In the following code shows how to use GradientPaint.GradientPaint(float x1, float y1, Color color1, float x2, float y2, Color color2, boolean cyclic) constructor.

```java title=Example.java
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    super.paint(g);
    Graphics2D g2d = (Graphics2D) g;
    GradientPaint gp1 = new GradientPaint(5, 5, Color.red, 20, 20, Color.yellow, true);
    g2d.setPaint(gp1);
    g2d.fillRect(20, 20, 300, 40);
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame("GradientsRedYellow");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.add(new Main());
    frame.setSize(350, 350);
    frame.setLocationRelativeTo(null);
    frame.setVisible(true);
  }
}
```
