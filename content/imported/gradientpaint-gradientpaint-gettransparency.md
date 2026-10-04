---
title: Java Swing Tutorial - Java GradientPaint .getTransparency ()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use GradientPaint.getTransparency() method.
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GradientPaint/0220__GradientPaint.getTransparency_.htm
---
```java title=Example.java
Back to GradientPaint  ↑
```

## Syntax

GradientPaint.getTransparency() has the following syntax.

```java title=Example.java
publicint getTransparency()
```

## Example

In the following code shows how to use GradientPaint.getTransparency() method.

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
