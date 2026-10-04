---
title: Java Swing Tutorial - Java BasicStroke JOIN_MITER
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.JOIN_MITER field.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0120__BasicStroke.JOIN_MITER.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Syntax

BasicStroke.JOIN_MITER has the following syntax.

```java title=Example.java
publicstaticfinalint JOIN_MITER
```

## Example

In the following code shows how to use BasicStroke.JOIN_MITER field.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.GeneralPath;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    RenderingHints rh = g2.getRenderingHints();
    rh.put(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setRenderingHints(rh);
    BasicStroke bs = new BasicStroke(36.0f, BasicStroke.CAP_BUTT, BasicStroke.JOIN_MITER);
    g2.setStroke(bs);
    GeneralPath path = new GeneralPath();
    path.moveTo(30.0f, 90.0f);
    path.lineTo(150.0f, 20.0f);
    path.lineTo(270.0f, 90.0f);
    g2.draw(path);
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
