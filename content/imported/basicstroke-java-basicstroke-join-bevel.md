---
title: Java BasicStroke JOIN_BEVEL
nav: Java BasicStroke JOIN_BEVEL
description: BasicStroke JOIN_BEVEL joins path segments by connecting the outer corners of their wide outlines with a straight segment.
section: Imported - java2s Archive
order: 1154
source: https://web.archive.org/web/20140418155107/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_JOIN_BEVEL.htm
---
In this chapter you will learn:

- Get to know BasicStroke.JOIN_BEVEL
- Syntax for BasicStroke.JOIN_BEVEL
- Example - BasicStroke.JOIN_BEVEL

### Description

BasicStroke JOIN_BEVEL joins path segments by connecting the outer corners of their wide outlines with a straight segment.

### Syntax

BasicStroke.JOIN_BEVEL has the following syntax.

```java title=Example.java
public static final int JOIN_BEVEL
```

### Example

In the following code shows how to use BasicStroke.JOIN_BEVEL field.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.GeneralPath;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    RenderingHints rh = g2.getRenderingHints();
    rh.put(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setRenderingHints(rh);
    BasicStroke bs = new BasicStroke(36.0f, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL);
    g2.setStroke(bs);
    GeneralPath path = new GeneralPath();
    path.moveTo(30.0f, 90.0f);
    path.lineTo(150.0f, 20.0f);
    path.lineTo(270.0f, 90.0f);
    g2.draw(path);
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- Get to know BasicStroke.JOIN_MITER
- Syntax for BasicStroke.JOIN_MITER
- Example - BasicStroke.JOIN_MITER
