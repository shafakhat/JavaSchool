---
title: Java Swing Tutorial - Java BasicStroke() Constructor
nav: Java Swing Tutorial - Java...
description: BasicStroke() constructor from BasicStroke has the following syntax.
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20150325071110/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0160__BasicStroke.BasicStroke_.htm
---
## Syntax

BasicStroke() constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke()
```

## Example

In the following code shows how to use BasicStroke.BasicStroke() constructor.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    g2.setPaint(Color.black);
    g2.setStroke(new BasicStroke());
    g2.draw(new Ellipse2D.Double(20,20, 50, 50));
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
