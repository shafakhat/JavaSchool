---
title: Java BasicStroke CAP_SQUARE
nav: Java BasicStroke CAP_SQUARE
description: BasicStroke CAP_SQUARE ends unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the lin
section: Imported - java2s Archive
order: 1145
source: https://web.archive.org/web/20140417005954/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_CAP_SQUARE.htm
---
In this chapter you will learn:

- Get to know BasicStroke.CAP_SQUARE
- Syntax for BasicStroke.CAP_SQUARE
- Example - BasicStroke.CAP_SQUARE

### Description

BasicStroke CAP_SQUARE ends unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

### Syntax

BasicStroke.CAP_SQUARE has the following syntax.

```java title=Example.java
public static final int CAP_SQUARE
```

### Example

In the following code shows how to use BasicStroke.CAP_SQUARE field.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    BasicStroke bs = new BasicStroke(16.0f, BasicStroke.CAP_SQUARE, BasicStroke.JOIN_BEVEL);
    g2.setStroke(bs);
    g.drawLine(30, 20, 270, 20);
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

- Get to know BasicStroke.JOIN_BEVEL
- Syntax for BasicStroke.JOIN_BEVEL
- Example - BasicStroke.JOIN_BEVEL
