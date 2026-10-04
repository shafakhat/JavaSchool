---
title: Java Swing Tutorial - Java BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) Constructor
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructor.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0240__BasicStroke.BasicStroke_float_width_int_cap_int_join_float_miterlimit_float_dash_float_dash_phase_.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Example

In the following code shows how to use BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructor.

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
    Stroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0,
        newfloat[] { 3, 1 }, 0);
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

- Back to BasicStroke ↑
