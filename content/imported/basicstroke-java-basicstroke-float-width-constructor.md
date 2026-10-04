---
title: Java BasicStroke(float width) Constructor
nav: Java BasicStroke(float wid...
description: BasicStroke BasicStroke(float width) constructs a solid BasicStroke with the specified line width and with default values for the cap and join styles.
section: Imported - java2s Archive
order: 1147
source: https://web.archive.org/web/20140418092035/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_float_width_Constructor.htm
---
In this chapter you will learn:

- Get to know BasicStroke.BasicStroke(float width)
- Syntax for BasicStroke(float width) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width)
- Exceptions from BasicStroke.BasicStroke(float width)
- Example - BasicStroke.BasicStroke(float width)

### Description

BasicStroke BasicStroke(float width) constructs a solid BasicStroke with the specified line width and with default values for the cap and join styles.

### Syntax

BasicStroke(float width) constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke(float width)
```

### Parameters

BasicStroke.BasicStroke(float width) constructor has the following parameters.

- width - the width of the BasicStroke

### Exceptions

BasicStroke.BasicStroke(float width) throws the following exceptions.

- IllegalArgumentException - if width is negative

### Example

In the following code shows how to use BasicStroke.BasicStroke(float width) constructor.

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
    g2.setStroke(new BasicStroke(8));
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

- Get to know BasicStroke.BasicStroke(float width, int cap, int join)
- Syntax for BasicStroke(float width, int cap, int join) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width, int cap, int join)
- Exceptions from BasicStroke.BasicStroke(float width, int cap, int join)
- Example - BasicStroke.BasicStroke(float width, int cap, int join)
