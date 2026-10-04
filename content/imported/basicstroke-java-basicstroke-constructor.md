---
title: Java BasicStroke() Constructor
nav: Java BasicStroke() Constru...
description: BasicStroke BasicStroke() constructs a new BasicStroke with defaults for all attributes. The default attributes are a solid line of width 1.0, CAP_SQUARE, JOIN_MITER, a m
section: Imported - java2s Archive
order: 1152
source: https://web.archive.org/web/20140418091920/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_Constructor.htm
---
In this chapter you will learn:

- Get to know BasicStroke.BasicStroke()
- Syntax for BasicStroke() constructor from BasicStroke
- Example - BasicStroke.BasicStroke()

### Description

BasicStroke BasicStroke() constructs a new BasicStroke with defaults for all attributes. The default attributes are a solid line of width 1.0, CAP_SQUARE, JOIN_MITER, a miter limit of 10.0.

### Syntax

BasicStroke() constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke()
```

### Example

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
```

#### Next chapter...

What you will learn in the next chapter:

- Get to know BasicStroke.BasicStroke(float width)
- Syntax for BasicStroke(float width) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width)
- Exceptions from BasicStroke.BasicStroke(float width)
- Example - BasicStroke.BasicStroke(float width)
