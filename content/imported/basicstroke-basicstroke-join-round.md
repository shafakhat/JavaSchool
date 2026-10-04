---
title: Java Swing Tutorial - Java BasicStroke JOIN_ROUND
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.JOIN_ROUND field.
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0140__BasicStroke.JOIN_ROUND.htm
---
## Syntax

BasicStroke.JOIN_ROUND has the following syntax.

```java title=Example.java
public static final int JOIN_ROUND
```

## Example

In the following code shows how to use BasicStroke.JOIN_ROUND field.

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
    BasicStroke bs = new BasicStroke(36.0f, BasicStroke.CAP_BUTT, BasicStroke.JOIN_ROUND);
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
java title=Example.java
```
