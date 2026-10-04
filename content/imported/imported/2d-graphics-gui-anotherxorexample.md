---
title: Another XOR example
nav: Another XOR example
description: 1. Layers - Try to use alpha values (transparency) to draw in layers
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20060903002913/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/AnotherXORexample.htm
---
```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class XORRectangles extends JPanel{
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    // using white as the XOR color.
    g2.setXORMode(Color.white);
    // Paint a red rectangle.
    Rectangle2D r = new Rectangle2D.Double(50, 50, 150, 100);
    g2.setPaint(Color.red);
    g2.fill(r);
    g2.transform(AffineTransform.getTranslateInstance(25, 25));
    // Draw a blue rectangle.
    g2.setPaint(Color.blue);
    g2.fill(r);
  }
  public static void main(String[] args) {
    JFrame f = new JFrame();
    f.getContentPane().add(new XORRectangles());
    f.setSize(300, 200);
    f.setVisible(true);
  }
}
```

Related examples in the same category
1. Layers - Try to use alpha values (transparency) to draw in layers
