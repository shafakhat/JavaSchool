---
title: A line is drawn using two points
nav: A line is drawn using two ...
description: Imported from the java2s.com archive: A line is drawn using two points
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20090903231020/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Alineisdrawnusingtwopoints.htm
---
A line is drawn using two points

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class LinesDashes1 extends JPanel {
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g;
    float[] dash1 = { 2f, 0f, 2f };
    g2d.drawLine(20, 40, 250, 40);
    BasicStroke bs1 = new BasicStroke(1,
        BasicStroke.CAP_BUTT,
        BasicStroke.JOIN_ROUND,
        1.0f,
        dash1,
        2f);
    g2d.setStroke(bs1);
    g2d.drawLine(20, 80, 250, 80);
    }
  public static void main(String[] args) {
    LinesDashes1 lines = new LinesDashes1();
    JFrame frame = new JFrame("Lines");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.add(lines);
    frame.setSize(280, 270);
    frame.setLocationRelativeTo(null);
    frame.setVisible(true);
  }
}
```

1.  Drawing a Line using Java 2D Graphics API
---  ---
2.  Line Styles
3.  Dash style line
4.  Line dashes style 2
5.  Lines Dashes style 3
6.  Line Dash Style 4
7.  Program to draw grids
8.  Xsplinefun displays colorful moving splines in a window
9.  Draw a point: use a drawLine() method
10.  Line-graph drawable
11.  Draw Dashed
12.  Draw Optimized Line
