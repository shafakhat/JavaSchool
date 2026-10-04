---
title: Java Swing Tutorial - Java Graphics.clipRect(int x, int y, int width, int height)
nav: Java Swing Tutorial - Java...
description: Graphics.clipRect(int x, int y, int width, int height) has the following syntax.
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0080__Graphics.clipRect_int_x_int_y_int_width_int_height_.htm
---
## Syntax

Graphics.clipRect(int x, int y, int width, int height) has the following syntax.

```java title=Example.java
publicabstractvoid clipRect(int x,  int y,  int width,  int height)
```

## Example

In the following code shows how to use Graphics.clipRect(int x, int y, int width, int height) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.setColor (Color.red);
    g.drawRect (0,0,100,100);
    g.clipRect (25, 25, 50, 50);
    g.drawLine (0,100,100,0);
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
