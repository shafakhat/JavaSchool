---
title: Java Swing Tutorial - Java Graphics.fill3DRect(int x, int y, int width, int height, boolean raised)
nav: Java Swing Tutorial - Java...
description: Graphics.fill3DRect(int x, int y, int width, int height, boolean raised) has the following syntax.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0560__Graphics.fill3DRect_int_x_int_y_int_width_int_height_boolean_raised_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.fill3DRect(int x, int y, int width, int height, boolean raised) has the following syntax.

```java title=Example.java
publicvoid fill3DRect(int x,  int y,  int width,  int height,  boolean raised)
```

## Example

In the following code shows how to use Graphics.fill3DRect(int x, int y, int width, int height, boolean raised) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.setColor (Color.gray);
    g.draw3DRect (25, 10, 50, 75, true);
    g.draw3DRect (25, 110, 50, 75, false);
    g.fill3DRect (100, 10, 50, 75, true);
    g.fill3DRect (100, 110, 50, 75, false);
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
