---
title: Java Swing Tutorial - Java BasicStroke(float width, int cap, int join, float miterlimit) Constructor
nav: Java Swing Tutorial - Java...
description: BasicStroke(float width, int cap, int join, float miterlimit) constructor from BasicStroke has the following syntax.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0220__BasicStroke.BasicStroke_float_width_int_cap_int_join_float_miterlimit_.htm
---
## Syntax

BasicStroke(float width, int cap, int join, float miterlimit) constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke(float width,   int cap,   int join,   float miterlimit)
```

## Example

In the following code shows how to use BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit) constructor.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Stroke;
import java.awt.geom.Rectangle2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    Stroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F
        );
    g2.setStroke(stroke);
    g2.setPaint(Color.black);
    g2.draw(new Rectangle2D.Float(10, 10, 200, 200));
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```
