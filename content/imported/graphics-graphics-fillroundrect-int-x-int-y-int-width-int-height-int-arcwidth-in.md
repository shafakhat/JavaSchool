---
title: Java Swing Tutorial - Java Graphics.fillRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight)
nav: Java Swing Tutorial - Java...
description: Graphics.fillRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight) has the following syntax.
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0680__Graphics.fillRoundRect_int_x_int_y_int_width_int_height_int_arcWidth_int_arcHeight_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.fillRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight) has the following syntax.

```java title=Example.java
publicabstractvoid fillRoundRect(int x,   int y,   int width,   int height,   int arcWidth,   int arcHeight)
```

## Example

In the following code shows how to use Graphics.fillRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight) method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.fillRoundRect(150, 50, 100, 100, 50, 25);
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
