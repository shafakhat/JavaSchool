---
title: Java BasicStroke(float width, int cap, int join) Constructor
nav: Java BasicStroke(float wid...
description: BasicStroke BasicStroke(float width, int cap, int join) constructs a solid BasicStroke with the specified attributes. The miterlimit parameter is unnecessary in cases whe
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20140418100353/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_float_width_int_cap_int_join_Constructor.htm
---
In this chapter you will learn:

- Get to know BasicStroke.BasicStroke(float width, int cap, int join)
- Syntax for BasicStroke(float width, int cap, int join) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width, int cap, int join)
- Exceptions from BasicStroke.BasicStroke(float width, int cap, int join)
- Example - BasicStroke.BasicStroke(float width, int cap, int join)

### Description

BasicStroke BasicStroke(float width, int cap, int join) constructs a solid BasicStroke with the specified attributes. The miterlimit parameter is unnecessary in cases where the default is allowable or the line joins are not specified as JOIN_MITER.

### Syntax

BasicStroke(float width, int cap, int join) constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke(float width,   int cap,   int join)
```

### Parameters

BasicStroke.BasicStroke(float width, int cap, int join) constructor has the following parameters.

- width - the width of the BasicStroke
- cap - the decoration of the ends of a BasicStroke
- join - the decoration applied where path segments meet

### Exceptions

BasicStroke.BasicStroke(float width, int cap, int join) throws the following exceptions.

- IllegalArgumentException - if width is negative
- IllegalArgumentException - if cap is not either CAP_BUTT, CAP_ROUND or CAP_SQUARE
- IllegalArgumentException - if join is not either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

### Example

In the following code shows how to use BasicStroke.BasicStroke(float width, int cap, int join) constructor.

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
    g2.setStroke(new BasicStroke(8,BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL));
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

- Get to know BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
- Syntax for BasicStroke(float width, int cap, int join, float miterlimit) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
- Exceptions from BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
- Example - BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
