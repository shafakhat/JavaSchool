---
title: Java Swing Tutorial - Java BasicStroke(float width) Constructor
nav: Java Swing Tutorial - Java...
description: BasicStroke(float width) constructor from BasicStroke has the following syntax.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0180__BasicStroke.BasicStroke_float_width_.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Syntax

BasicStroke(float width) constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke(float width)
```

## Example

In the following code shows how to use BasicStroke.BasicStroke(float width) constructor.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
/*fromwww.java2s.com*/import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extends JPanel {

  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;

    g2.setPaint(Color.black);
    g2.setStroke(new BasicStroke(8));
    g2.draw(new Ellipse2D.Double(20,20, 50, 50));
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
