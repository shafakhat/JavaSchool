---
title: Java BasicStroke(float width, int cap, int join, float miterlimit) Constructor
nav: Java BasicStroke(float wid...
description: BasicStroke BasicStroke(float width, int cap, int join, float miterlimit) constructs a solid BasicStroke with the specified attributes.
section: Imported - java2s Archive
order: 1149
source: https://web.archive.org/web/20140418095800/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_float_width_int_cap_int_join_float_miterlimit_Constructor.htm
---
In this chapter you will learn:

- Get to know BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
- Syntax for BasicStroke(float width, int cap, int join, float miterlimit) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
- Exceptions from BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)
- Example - BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit)

### Description

BasicStroke BasicStroke(float width, int cap, int join, float miterlimit) constructs a solid BasicStroke with the specified attributes.

### Syntax

BasicStroke(float width, int cap, int join, float miterlimit) constructor from BasicStroke has the following syntax.

```java title=Example.java
public BasicStroke(float width,   int cap,   int join,   float miterlimit)
```

### Parameters

BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit) constructor has the following parameters.

- width - the width of the BasicStroke
- cap - the decoration of the ends of a BasicStroke
- join - the decoration applied where path segments meet
- miterlimit - the limit to trim the miter join

### Exceptions

BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit) throws the following exceptions.

- IllegalArgumentException - if width is negative
- IllegalArgumentException - if cap is not either CAP_BUTT, CAP_ROUND or CAP_SQUARE
- IllegalArgumentException - if miterlimit is less than 1 and join is JOIN_MITER
- IllegalArgumentException - if join is not either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER

### Example

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
public class Main extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    Stroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F
        );
    g2.setStroke(stroke);
    g2.setPaint(Color.black);
    g2.draw(new Rectangle2D.Float(10, 10, 200, 200));
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

- Get to know BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
- Syntax for BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
- Exceptions from BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
- Example - BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
