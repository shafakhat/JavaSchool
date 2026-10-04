---
title: Java Swing Tutorial - Java GradientPaint.getPoint1()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use GradientPaint.getPoint1() method.
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GradientPaint/0180__GradientPaint.getPoint1_.htm
---
```java title=Example.java
Back to GradientPaint  ↑
```

## Syntax

GradientPaint.getPoint1() has the following syntax.

```java title=Example.java
public Point2D getPoint1()
```

## Example

In the following code shows how to use GradientPaint.getPoint1() method.

```java title=Example.java
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    super.paint(g);
    Graphics2D g2d = (Graphics2D) g;
    GradientPaint gp1 = new GradientPaint(5, 5, Color.red, 20, 20, Color.yellow, true);
    System.out.println(gp1.getPoint1());
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
