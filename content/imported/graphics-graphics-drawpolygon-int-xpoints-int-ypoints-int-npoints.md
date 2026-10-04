---
title: Java Swing Tutorial - Java Graphics.drawPolygon(int[] xPoints, int[] yPoints, int nPoints)
nav: Java Swing Tutorial - Java...
description: Graphics.drawPolygon(int[] xPoints, int[] yPoints, int nPoints) has the following syntax.
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0420__Graphics.drawPolygon_int_xPoints_int_yPoints_int_nPoints_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.drawPolygon(int[] xPoints, int[] yPoints, int nPoints) has the following syntax.

```java title=Example.java
publicabstractvoid drawPolygon(int[] xPoints,  int[] yPoints,  int nPoints)
```

## Example

In the following code shows how to use Graphics.drawPolygon(int[] xPoints, int[] yPoints, int nPoints) method.

```java title=Example.java
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    int xpoints[] = {25, 145, 25, 145, 25};
    int ypoints[] = {25, 25, 145, 145, 25};
    int npoints = 5;
    g.drawPolygon(xpoints, ypoints, npoints);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

- Back to Graphics ↑
