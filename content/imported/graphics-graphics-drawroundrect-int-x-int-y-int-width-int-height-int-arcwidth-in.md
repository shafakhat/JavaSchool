---
title: Java Swing Tutorial - Java Graphics.drawRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight)
nav: Java Swing Tutorial - Java...
description: Graphics.drawRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight) has the following syntax.
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0500__Graphics.drawRoundRect_int_x_int_y_int_width_int_height_int_arcWidth_int_arcHeight_.htm
---
## Syntax

Graphics.drawRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight) has the following syntax.

```java title=Example.java
publicabstractvoid drawRoundRect(int x,   int y,   int width,   int height,   int arcWidth,   int arcHeight)
```

## Example

In the following code shows how to use Graphics.drawRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight) method.

```java title=Example.java
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.drawRoundRect(25, 50, 100, 100, 25, 50);
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
