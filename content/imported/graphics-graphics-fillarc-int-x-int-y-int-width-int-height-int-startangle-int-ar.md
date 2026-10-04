---
title: Java Swing Tutorial - Java Graphics.fillArc(int x, int y, int width, int height, int startAngle, int arcAngle)
nav: Java Swing Tutorial - Java...
description: Graphics.fillArc(int x, int y, int width, int height, int startAngle, int arcAngle) has the following syntax.
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0580__Graphics.fillArc_int_x_int_y_int_width_int_height_int_startAngle_int_arcAngle_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.fillArc(int x, int y, int width, int height, int startAngle, int arcAngle) has the following syntax.

```java title=Example.java
publicabstractvoid fillArc(int x,  int y,  int width,  int height,  int startAngle,  int arcAngle)
```

## Example

In the following code shows how to use Graphics.fillArc(int x, int y, int width, int height, int startAngle, int arcAngle) method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.fillArc (5, 15, 50, 75, 25, 165);
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
