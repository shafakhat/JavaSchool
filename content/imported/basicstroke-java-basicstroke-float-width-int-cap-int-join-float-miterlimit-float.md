---
title: Java BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) Constructor
nav: Java BasicStroke(float wid...
description: BasicStroke BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructs a new BasicStroke with the specified attributes.
section: Imported - java2s Archive
order: 1155
source: https://web.archive.org/web/20140418095906/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_float_width_int_cap_int_join_float_miterlimit_float_dash_float_dash_phase_Constructor.htm
---
In this chapter you will learn:

- Get to know BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
- Syntax for BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructor from BasicStroke
- Parameter for BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
- Exceptions from BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
- Example - BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)

### Description

BasicStroke BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructs a new BasicStroke with the specified attributes.

### Syntax

BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructor from BasicStroke has the following syntax.

```java title=Example.java
@ConstructorProperties(value ={"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"})public BasicStroke(float width,          int cap,          int join,          float miterlimit,          float[] dash,          float dash_phase)
```

### Parameters

BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) constructor has the following parameters.

- width - the width of this BasicStroke . The width must be greater than or equal to 0.0f. If width is set to 0.0f, the stroke is rendered as the thinnest possible line for the target device and the antialias hint setting.
- cap - the decoration of the ends of a BasicStroke
- join - the decoration applied where path segments meet
- miterlimit - the limit to trim the miter join. The miterlimit must be greater than or equal to 1.0f.
- dash - the array representing the dashing pattern
- dash_phase - the offset to start the dashing pattern

### Exceptions

BasicStroke.BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase) throws the following exceptions.

- IllegalArgumentException - if width is negative
- IllegalArgumentException - if cap is not either CAP_BUTT, CAP_ROUND or CAP_SQUARE
- IllegalArgumentException - if miterlimit is less than 1 and join is JOIN_MITER
- IllegalArgumentException - if join is not either JOIN_ROUND, JOIN_BEVEL, or JOIN_MITER
- IllegalArgumentException - if dash_phase is negative and dash is not null
- IllegalArgumentException - if the length of dash is zero
- IllegalArgumentException - if dash lengths are all zero.

### Example

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
public class Main extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    Stroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0,
        new float[] { 3, 1 }, 0);
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

- Get to know BasicStroke.createStrokedShape(Shape s)
- Syntax for BasicStroke.createStrokedShape(Shape s)
- Parameter for BasicStroke.createStrokedShape(Shape s)
- Returns for BasicStroke.createStrokedShape(Shape s)
- Example - BasicStroke.createStrokedShape(Shape s)
